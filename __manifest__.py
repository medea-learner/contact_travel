{
    'name': 'Contact Travel',
    'version': '1.0',
    'summary': 'Manage user travels and reward levels',
    'category': 'Tools',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/voyage_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}