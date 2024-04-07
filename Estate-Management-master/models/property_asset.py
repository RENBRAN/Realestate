from odoo import models, fields, api


class PropertyAsset(models.Model):
    _name = 'property.asset'
    _description = 'Property Asset'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    asset = fields.Binary(string='Asset', required=True)
    asset_url = fields.Char(string='Asset URL', readonly=True)
    asset_type = fields.Selection([
        ('image', 'Image'),
        ('video', 'Video'),
    ], required=True)
    
    # The type of the asset
    tag_id = fields.Many2many('property.asset.tag', string='Tag')
    category_id = fields.Many2many(
        'property.asset.category', string='Category')

    # The property that the asset belongs to
    property_id = fields.Many2one('property', string='Property', required=True)

    @api.model
    def create(self, vals):
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        asset: PropertyAsset = super().create(vals)
        
        asset.asset_url = f"{base_url}/web/image?model=property.asset&id={asset.id}&field=asset"
        return asset


class PropertyAssetTag(models.Model):
    _name = 'property.asset.tag'
    _description = 'Property Asset Tag'

    name = fields.Char(string='Name')


class PropertyAssetCategory(models.Model):
    _name = 'property.asset.category'
    _description = 'Property Asset Category'

    name = fields.Char(string='Name')
