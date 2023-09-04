{
    'name': 'Customer Sequence',
    'version': '15.0.1.0.0',
    'category': 'customer',
    'summery': 'This app will create a sequence code with contact, while creating new contacts.',
    'author': 'INKERP',
    'website': "http://www.INKERP.com",
    'depends': [],
    
    'data': [
        'views/res_partner_view.xml',
        'data/ir_sequence_data.xml'
    ],
    
    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
