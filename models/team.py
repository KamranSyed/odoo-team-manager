# -*- coding: utf-8 -*-

from odoo import models, fields, api

class team(models.Model):
	 _name = 'ksteam.team'

	 name = fields.Char(required=True)
	 description 	= fields.Char()
	 employee_ids 	= fields.Many2many('hr.employee', string='Employees')
	 manager_ids 	= fields.Many2many('hr.employee', string='Managers')
	 active			= fields.Boolean('Active?', default=True)
	 
