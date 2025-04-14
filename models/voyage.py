from odoo import models, fields

class Voyage(models.Model):
    """
    Represents a Voyage linked to a contact (res.partner).
    Fields:
    - name: Voyage name.
    - departure_date: Date of departure.
    - destination: Travel destination.
    - partner_id: Linked contact.
    - amount: Travel cost.
    """
    _name = 'contact_travel.voyage'
    _description = 'Voyage'

    name = fields.Char(string='Nom du voyage', required=True)
    departure_date = fields.Date(string='Date de départ')
    destination = fields.Char(string='Destination')
    partner_id = fields.Many2one(
        'res.partner',
        string='Contact',
        ondelete='cascade'
    )
    amount = fields.Float(string='Montant du voyage')
