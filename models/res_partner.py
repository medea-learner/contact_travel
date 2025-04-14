from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    voyage_ids = fields.One2many(
        'contact_travel.voyage',
        'partner_id',
        string='Voyages'
    )
    voyage_count = fields.Integer(
        string='Nombre de voyages',
        compute='_compute_voyage_count'
    )

    @api.depends('voyage_ids')
    def _compute_voyage_count(self):
        for partner in self:
            partner.voyage_count = len(partner.voyage_ids)
