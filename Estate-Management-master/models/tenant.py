from odoo import models, fields


class Tenant(models.Model):
    """
    Model representing a tenant.

    This class contains the information about a tenant,
    such as their name, contact information, lease start and end dates,
    and their monthly rent.
    """
    _name = 'tenant'
    _description = 'Tenant'

    name = fields.Char(string='Name',
                       help='The name of the tenant.')
    contact_information = fields.Char(string='Phone',
                                      help='The contact information of the tenant.')

    # Relationl fields

    property_ids = fields.One2many('property', 'tenant_id', string='Property')
    aggreement_ids = fields.One2many(
        'lease.agreement', 'tenant_id', string='Agreements')

    user_id = fields.Many2one('res.users', string='User', required=True)

    # SQL constraints

    _sql_constraints = [
        ('phone_number_length_check', "CHECK (contact_information ~ '^\\d{11}$')",
         'Checks if the contact information is exactly 11 digits long.')
    ]
