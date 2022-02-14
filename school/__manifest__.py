{
    'name': "shool_management",
    'version': '1.0',
    'author': "Aswanth",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'depends' : [
        'mail',
        # 'contact',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/school_manage_view.xml',
        'views/school_menu.xml',
        'views/student_manage_view.xml',
        'views/employe_manage_view.xml',
        'views/teacher_detail_view.xml',
        'views/nonteaching_detail_view.xml',
        'views/lower_class_view.xml',
        'views/uper_class_view.xml',
        # 'views/employe_wizard_view.xml',
        'views/hs_view.xml',
        'views/hss_view.xml',
        'views/student_report_wizard_view.xml',
        'report/report.xml',
        'report/employe_report_view.xml',
        'report/employe_mail_template.xml',


    ],
    # data files containing optionally loaded demonstration data
    'demo': [

    ],
    'application':True
}
