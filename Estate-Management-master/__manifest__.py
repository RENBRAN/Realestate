{
    'name': "Estate Management",
    'version': '1.0',
    'depends': ['base', 'mail', 'hr'],
    'author': "Abdelrahman Hanafy",
    'category': 'Category',
    'description': """
    Description text
    """,
    'license': 'LGPL-3',
    # data files always loaded at installation
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'wizard/maintanance_request.xml',  # wizard
        'wizard/property_survey.xml',

        'views/owner_views.xml',    # views
        'views/tenant_views.xml',
        'views/visitor_views.xml',
        'views/property_views.xml',
        'views/property_document.xml',
        'views/property_asset.xml',
        'views/transaction_view.xml',
        'views/agreement_views.xml',
        'views/contract_clause.xml',
        'views/contract_views.xml',
        'views/maintanance_views.xml',

        'report/contract_report.xml', # report

        'views/estate_management_menu.xml', # menu

    ],
    'application': True,
    'assets': {
        'web.assets_backend': [
            'Estate_Management/static/src/js/video_display_widget.js',
            
        ],
    }
}
