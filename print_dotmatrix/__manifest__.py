# -*- coding: utf-8 -*-
{
    'name': "print_dotmatrix",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account', 'mail', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/invoice.xml',
        'views/web_assets.xml',
        'data/templates.xml',
    ],

    'qweb': [
        'static/src/xml/web_print_button.xml',
    ]
}
