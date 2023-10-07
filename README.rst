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
