# -*- coding: utf-8 -*-

from odoo import models, fields, api

class team(models.Model):
	 _name = 'ksteam.team'

	 name = fields.Char(required=True)
	 description 	= fields.Char()
	 employee_ids 	= fields.Many2many('hr.employee', string='Members')
	 manager_ids 	= fields.Many2many('hr.employee', 'ksteam_team_managers_rel', string='Managers')
	 active			= fields.Boolean('Active?', default=True)
	 
