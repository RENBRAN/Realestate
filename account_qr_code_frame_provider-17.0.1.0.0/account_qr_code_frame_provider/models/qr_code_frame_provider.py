###################################################################################
#
#    Copyright (c) 2022 Data Dance s.r.o.
#
#    Data Dance Proprietary License v1.0
#
#    This software and associated files (the "Software") may only be used
#    (executed, modified, executed after modifications) if you have
#    purchased a valid license from Data Dance s.r.o.
#
#    The above permissions are granted for a single database per purchased
#    license. Furthermore, with a valid license it is permitted to use the
#    software on other databases as long as the usage is limited to a testing
#    or development environment.
#
#    You may develop modules based on the Software or that use the Software
#    as a library (typically by depending on it, importing it and using its
#    resources), but without copying any source code or material from the
#    Software. You may distribute those modules under the license of your
#    choice, provided that this license is compatible with the terms of the
#    Data Dance Proprietary License (For example: LGPL, MIT, or proprietary
#    licenses similar to this one).
#
#    It is forbidden to publish, distribute, sublicense, or sell copies of
#    the Software or modified copies of the Software.
#
#    The above copyright notice and this permission notice must be included
#    in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
###################################################################################


import base64
import io

import qrcode
from odoo import api, models
from odoo.tools.image import image_data_uri
from PIL import Image
from qrcode.image import pil


class FrameProvider(models.Model):
    _inherit = "res.partner.bank"

    def _get_qr_code_base64(
        self,
        qr_method,
        amount,
        currency,
        debtor_partner,
        free_communication,
        structured_communication,
    ):
        res = super()._get_qr_code_base64(
            qr_method,
            amount,
            currency,
            debtor_partner,
            free_communication,
            structured_communication,
        )

        params = self._get_qr_code_frame_generation_params(qr_method)
        if params is None:
            return res

        back_color = "transparent"
        fill_color = "black"

        frame = params["frame"]
        if frame:
            frame = frame.resize(params["frame_size"])

        qr = qrcode.QRCode(
            box_size=params["box_size"],
            border=params["border"],
            image_factory=pil.PilImage,
        )
        data = self._get_qr_code_generation_params(
            qr_method,
            amount,
            currency,
            debtor_partner,
            free_communication,
            structured_communication,
        )
        qr.add_data(data["value"])
        qr.make()

        qr_image = qr.make_image(
            fill_color=fill_color,
            back_color=back_color,
            image_factory=pil.PilImage,
        )

        qr_image = qr_image.resize(params["resize_values"], Image.LANCZOS)

        x, y = params["x_y"]
        result = Image.new("RGBA", params["frame_size"])
        if frame:
            result.paste(frame, (0, 0))
        result.paste(qr_image, (x, y))

        buffered = io.BytesIO()
        result.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        return image_data_uri(img_str)

    def _get_qr_code_frame_generation_params(self, qr_method):
        """Hook for extension"""
        return None
