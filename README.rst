.. -*- coding: utf-8 -*-
==========
Bell Systray Notification Module for Odoo 16
==========

.. |badge1| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

.. |badge2| image:: https://github.com/cramirezmartin/bell_systray_notification/blob/main/static/description/bell_systray_notification.png?raw=true
    :target: https://github.com/cramirezmartin/bell_systray_notification
    :alt: Module: bell_systray_notification

|badge1| |badge2|

**Table of contents**

.. contents::
   :local:

Information
===========

Puts a bell in the systray that shows the number of notifications in a badge and allows them to be displayed when clicked.

Dependencies
============

It use the `web_notify <https://github.com/OCA/web/tree/16.0/web_notify>`_ module for show the notifications.

Usage
=====

To send a notification to the user you just need to create a notification, use this code for example:

.. code-block:: python

  self.env['bell.systray.notification'].create({
      'user_id': user_id.id,
      'message': message,
      'title': title,
      'sticky': sticky,
      'type_default': type_default,
  })

Every minute the notification icon bell will update showing the number of existing notifications

* user_id.id: Id of the user to whom the notification is sent
* message: Notification text
* title: Notification title
* sticky: If the notification remains fixed or disappears after a few seconds, the values accepted are:

  * True
  * False

  Default value: True
* type_default: Notification type. The values that accepted are:

  * success
  * danger
  * warning
  * info
  * default

* Default value: default

Code description
=================

The functionality consists of a counter that counts every minute to a function that returns the number of existing notifications. To do this, only those that belong to the currently logged in user and whose status is 'new' are taken.
The main characteristics are found in the files:

* conrollers/bell_systray_controller.py

The method get_notification_counter return the number of notifications
The method show_notification show the notifications using the `web_notify <https://github.com/OCA/web/tree/16.0/web_notify>`_ module

.. code-block:: python

  @http.route('/get_bell_systray_notification_counter', auth='user', type='json', website=True)
  def get_notification_counter(self, **kw):
      env = http.request.env
      notifications = env['bell.systray.notification'].search([('user_id', '=', env.uid), ('status', '=', 'new')])
      number = len(notifications)
      print('----------- Notifications: '+str(number)+' -----------')
      return number

  @http.route('/show_bell_systray_notification', auth='user', type='json', website=True)
  def show_notification(self, **kw):
      env = http.request.env
      notifications = env['bell.systray.notification'].search([('user_id', '=', env.uid), ('status', '=', 'new')])
      number = len(notifications)
      if number != 0:
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
          env.user.notify_info(message="There are no notifications for you")
      print('----------- Show '+str(number)+' Notifications -----------')
      return True

* static/src/js/systray.js

Inside the 'setup' function in 'bellSystrayNotificationsIcon' class the variables define are:

.. code-block:: javascript

    this.action = useService("action"); 
    this.rpc = useService("rpc");

    const onwillstart = async () => {return await this.rpc("/get_bell_systray_notification_counter", {});};
    const showNotifications = async () => {await this.rpc("/show_bell_systray_notification", {});};
    this.showNotifications = showNotifications;

The next code ask every 60000 ms the number of notifications and show this value in 'bell_systray_notification_counter_badge' element.

.. code-block:: javascript

  setInterval(function(){
      onwillstart().then(function (result) {
          let badge = document.getElementById('bell_systray_notification_counter_badge');
          if(result == 0) result = '';
          if(badge != null) badge.innerHTML = result;
      });
  }, 60000);


To modify the time in which the number of notifications is updated, you must modify the Timer changing the value 60000 to the desired value in ms.

The next code insde the 'setup' function allow obtain the number when page is loaded.

.. code-block:: javascript

  onwillstart().then(function (result) {
      let badge = document.getElementById('bell_systray_notification_counter_badge');
      if(result == 0) result = '';
      if(badge != null) badge.innerHTML = result;
  });

The function '_onClickBellSystrayNotificationIcon' is the action when the bell button is clicked.

.. code-block:: javascript

  _onClickBellSystrayNotificationIcon() {
      this.showNotifications().then(function (result) {
          let badge = document.getElementById('bell_systray_notification_counter_badge');
          if(badge != null) badge.innerHTML = '';
      });
  }

* static/src/xml/systray.xml

Is the xml view for the bell

.. code-block:: xml

  <?xml version="1.0" encoding="UTF-8" ?>
  <templates xml:space="preserve">
    <t t-name="bell_systray_notification_icon" owl="1">
      <div>
        <div class="o_MessagingMenu dropdown">
          <a href="#" title="Notifications" role="button">
            <i class="fa fa-bell" 
              role="img"
              aria-label="Notifications" 
              t-on-click="_onClickBellSystrayNotificationIcon"/>
            <span class="o_MessagingMenu_counter badge" 
              id="bell_systray_notification_counter_badge">
            </span>
          </a>
        </div>
      </div>
    </t>
  </templates>

* fa fa-bell: Icon using for the button
* bell_systray_notification_counter_badge: Element that shows the number of notifications
* _onClickBellSystrayNotificationIcon: Function execute when the button is clicked

.. |badge3| image:: https://github.com/cramirezmartin/bell_systray_notification/blob/main/static/description/screenshot.png?raw=true
            :target: https://github.com/cramirezmartin/bell_systray_notification/blob/main/static/description/screenshot.png
            :alt: Module: Number of notifications

.. |badge4| image:: https://github.com/cramirezmartin/bell_systray_notification/blob/main/static/description/screenshot2.png?raw=true
            :target: https://github.com/cramirezmartin/bell_systray_notification/blob/main/static/description/screenshot2.png
            :alt: Module: Show the notifications

|badge3|

|badge4|