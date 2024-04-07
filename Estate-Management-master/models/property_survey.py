from odoo import api, fields, models

class PropertySurvey(models.Model):
    _name = 'property.survey'
    _description = 'Property Survey'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    
    managment_score = fields.Integer(string='Management Score')
    amenities_score = fields.Integer(string='Amenities Score')
    overall_score = fields.Integer(string='Overall Score')
    
    property_id = fields.Many2one('property', string='Property')
    date = fields.Date(string='Date', default=fields.Date.today(), readonly=True)

class PropertySurveyWizard(models.TransientModel):
    _name = 'property.survey.wizard'
    _description = 'Property Survey'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')

    managment_score = fields.Integer(string='Management Score')
    amenities_score = fields.Integer(string='Amenities Score')
    overall_score = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ],string='Overall Score')

    def action_done(self):
        self.ensure_one()
        property = self.env['property'].browse(
            self.env.context.get('active_id'))
        
        survey = self.env['property.survey'].create({
            "property_id": property.id,
            "name": self.name,
            "description": self.description,
            "managment_score": self.managment_score,
            "amenities_score": self.amenities_score,
            "overall_score": self.overall_score
        })

        return survey

