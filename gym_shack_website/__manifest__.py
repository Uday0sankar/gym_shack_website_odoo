{
    'name': 'Gym Shack Website',
    'version': '18.0.1.0.0',
    'category': 'Website',
    'summary': 'Premium Gym Shack public website with dynamic content management for Odoo 18.',
    'description': '''
        Gym Shack website rebuild for Odoo 18.
        Includes a responsive homepage, configurable branding, hero, programs, pricing,
        features, contact form, and Odoo-friendly dynamic content records.
    ''',
    'author': 'OpenAI',
    'website': 'https://github.com/Uday0sankar/gym_shack_website_odoo',
    'license': 'AGPL-3',
    'depends': ['website', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/website_demo_data.xml',
        'views/website_templates.xml',
        'views/website_menu.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'gym_shack_website/static/src/css/gym_shack.css',
            'gym_shack_website/static/src/js/gym_shack.js',
        ],
    },
    'installable': True,
    'application': True,
}
