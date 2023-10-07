# bell_systray_notification
Bell Systray Notification Module for Odoo 16

Puts a bell in the systray that shows the number of notifications in a badge and allows them to be displayed when clicked.
It use the web_notify module for show the notifications. See: https://github.com/OCA/web/tree/16.0/web_notify

To send a notification to the user you just need to create a notification, use this code for example:
self.env['bell.systray.notification'].create({
    'user_id': user_id.id,
    'message': message,
    'title': title,
    'sticky': sticky,
    'type_default': type_default,
})

user_id.id: Id of the user to whom the notification is sent
message: Notification text
title: Notification title
sticky: If the notification remains fixed or disappears after a few seconds, the values accepted are:
  - True
  - False
  Default value: True
type_default: Notification type. The values that accepted are:
  - success
  - danger
  - warning
  - info
  - default
Default value: default
