# -*- coding: utf-8 -*-

from odoo import fields,models

class StudentResult(models.TransientModel):

    _name = 'result.table'
    _inherit = 'studenttable.model'

    student_name = fields.Many2one('studenttable.model', string="Student Name")
    date_from = fields.Date(string="starting date")
    date_upto = fields.Date(string="Ending Date", comput="_get_result_student")
    final = fields.Many2one('studenttable.model', string="final")

    @api.depence('date_upto','student_name','')
    def _get_result_student(self):






