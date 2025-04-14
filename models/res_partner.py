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
    reward_level = fields.Selection(
        selection=[
            ('argent', 'Argent'),
            ('or', 'Or'),
            ('platine', 'Platine')
        ],
        string='Niveau de récompense',
        compute='_compute_reward_level',
        store=True
    )

    explanation = fields.Char(
        string='Explication',
        compute='_compute_explanation',
        store=False
    )

    @api.depends('voyage_ids')
    def _compute_voyage_count(self):
        for partner in self:
            partner.voyage_count = len(partner.voyage_ids)

    @api.depends('voyage_ids.amount')
    def _compute_reward_level(self):
        for partner in self:
            total = sum(voyage.amount for voyage in partner.voyage_ids)
            if total >= 100000:
                partner.reward_level = 'platine'
            elif total >= 50000:
                partner.reward_level = 'or'
            else:
                partner.reward_level = 'argent'
    
    @api.depends('reward_level')
    def _compute_explanation(self):
        for rec in self:
            if rec.reward_level == 'platine':
                rec.explanation = "Platine (total ≥ 100 000€)"
            elif rec.reward_level == 'or':
                rec.explanation = "Or (50 000€ ≤ total < 100 000€)"
            elif rec.reward_level == 'argent':
                rec.explanation = "Argent (total < 50 000€)"
            else:
                rec.explanation = "Non défini"
