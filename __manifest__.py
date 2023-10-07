{
    'name': "Bell Systray Notification",
    'summary': "Push a bell in the systray and show the notifications for the user",
    'description': """
        Puts a bell in the systray that shows the number of notifications in a badge and allows them to be displayed when clicked.
        It use the web_notify module for show the notifications
    """,

    'author': "Carlos Enrique Ramírez Martín",
    'maintainer': '',
    'website': '',
    'license': 'LGPL-3',
    'contributors': [
        '',
    ],
    'category': 'Uncategorized',
    'version': '1',
    'depends': ['base', 'web_notify'],
    'installable': True,
    'auto_install': False,
    'application': True,

    'assets': {
        'web.assets_backend': [
            'bell_systray_notification/static/src/js/systray.js',
            'bell_systray_notification/static/src/xml/systray.xml',
        ],
    },
}
