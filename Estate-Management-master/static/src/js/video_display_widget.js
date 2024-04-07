/** @odoo-module */

import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { CharField, charField} from "@web/views/fields/char/char_field";
import { Component, xml } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class VideoDisplayWidget extends Component {

    get videoUrl() {
        return this.props.record.data.asset_url;
      }

    /**
    * @param {char} newValue
    */
    onChange(newValue) {
        this.props.update(newValue);
    }
}

VideoDisplayWidget.template =xml`
<templates>
    <t>
        <div>
            <video t-att-src="videoUrl" controls="True" width="320" height="240">
                Your browser does not support the video tag.
            </video>
            
        </div>
    </t>
</templates>
`;
VideoDisplayWidget.props = {
    ...standardFieldProps,
};

export const videoDisplayWidget = {
    ...charField,
    component: VideoDisplayWidget,
};

registry.category("fields").add("video_display", videoDisplayWidget);
