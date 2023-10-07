from odoo import api, fields, models

class BellSystrayNotification(models.Model):
    _name = 'bell.systray.notification'
    _description = 'Bell Systray Notification Model'
    
    user_id = fields.Many2one(comodel_name='res.users', string='To', required=True)
    status = fields.Selection(string="Status", selection=[('new', 'new'), ('read', 'read')], default='new')
    
    message = fields.Char(string='Message', required=True)
    title = fields.Char(string='Title')
    sticky = fields.Boolean(string='Sticky', default=True)
    type_default = fields.Selection(string="Type", selection=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('info', 'info'), ('default', 'default')], default='default')
    