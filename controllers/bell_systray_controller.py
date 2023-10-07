from odoo import http
from odoo.http import request

class BellSystrayController(http.Controller):
    
    @http.route('/get_bell_systray_notification_counter', auth='user', type='json', website=True)
    def get_notification_counter(self, **kw):
        env = http.request.env
        notifications = env['bell.systray.notification'].search([('user_id', '=', env.uid), ('status', '=', 'new')])
        return len(notifications)
    
    @http.route('/show_bell_systray_notification', auth='user', type='json', website=True)
    def show_notification(self, **kw):
        env = http.request.env
        notifications = env['bell.systray.notification'].search([('user_id', '=', env.uid), ('status', '=', 'new')])
        if len(notifications) != 0:
            for n in notifications:
                if n.type_default:
                    if n.type_default == 'success':
                        env.user.notify_success(message=n.message, title=n.title, sticky=n.sticky)
                    elif n.type_default == 'danger':
                        env.user.notify_danger(message=n.message, title=n.title, sticky=n.sticky)
                    elif n.type_default == 'warning':
                        env.user.notify_warning(message=n.message, title=n.title, sticky=n.sticky)
                    elif n.type_default == 'info':
                        env.user.notify_info(message=n.message, title=n.title, sticky=n.sticky)
                    elif n.type_default == 'default':
                        env.user.notify_default(message=n.message, title=n.title, sticky=n.sticky)
                else:
                    env.user.notify_default(message=n.message, title=n.title, sticky=n.sticky)
            notifications.write({'status': 'read'})
        else:
            env.user.notify_warning(message="There are no notifications for you")
        return True