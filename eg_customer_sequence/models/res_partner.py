from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    code = fields.Char(string='Code')

    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        for rec in res:
            code = self.env['ir.sequence'].next_by_code(
                'res.partner')
            rec.code = code
        return res
