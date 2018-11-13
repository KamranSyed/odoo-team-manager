# -*- coding: utf-8 -*-
# Part of Teams App. See LICENSE and COPYRIGHT files for full copyright and licensing details.
{
    'name': "Team",
    'version': '0.6',
    'summary': """
        Organizes employees into Teams.
        Team management App""",

    'description': """
        Team APP organizes employees into teams for easy grouping of employees according to specific needs of organization. 
    """,

    'author': "Kamran Syed",
    'website': "http://agilesolutionspk.com",
	'license': "GPL-3",
	'installable': True,
    'application': True,
	'auto_install': True,
    'category': 'Human Resources',
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/team_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
