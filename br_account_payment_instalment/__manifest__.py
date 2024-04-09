
{
    'name': "Installment in Payment Terms",
    'version': '17.0.1.0.0',
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'category': 'Accounting',
    'summary': 'Installment in Payment Terms',
    'description': """
    New type 'Installment' in Odoo payment terms, Instalment in Payment Terms,Installment
    """,
    'depends': ['account'],
    'data': [
        'views/account_payment_term_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
}
