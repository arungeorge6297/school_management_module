# -*- coding: utf-8 -*-

from odoo import fields, models, api
from  datetime import datetime
from odoo.exceptions import ValidationError

class Employee(models.Model):

    _name = "employee.table"
    _inherit = 'school.table'



    school_name = fields.Char(String="School Name")
    employe_name = fields.Char(String="Employe Name")
    employee_id = fields.Integer(String="EmployeId")
    position = fields.Selection([('teacher', 'teacher'), ('driver', 'driver'), ('cleark', 'cleark')], string="Position")
    place = fields.Char(String="Place")
    empimage = fields.Binary(String="Image")
    address = fields.Text(String="Address")
    salary = fields.Float(String="Salary")
    age = fields.Char(String="Age", compute="_get_age_from_student", store=True)
    dob = fields.Date(String="Date of Birth", required=True)
    street = fields.Char(String="Street")
    street2 = fields.Char(String="Street2")
    city = fields.Char(String="City")
    state_id = fields.Many2one('res.partner', String="State id")
    zip = fields.Char(String="Zip")
    country_id = fields.Many2one('res.country', String="country id")
    state = fields.Selection([('new', 'new'), ('canceled', 'canceled')], default='new')
    phone = fields.Char(String="Phone", size=10)
    email = fields.Char(string="Email")


    @api.depends('dob', 'age')
    def _get_age_from_student(self):
        today_date = datetime.today()
        for stud in self:
            if stud.dob:
                dob = fields.Datetime.to_datetime(stud.dob)
                total_age = str(int((today_date - dob).days / 365))
                stud.age = total_age


    def cancel_action(self):
        for record in self:
            record.state = "canceled"
        return True


    @api.constrains('phone')
    def is_valid(self):
        l = len(self.phone)
        for ch in self.phone:
            letter = ch.isalpha()
            if letter :
                raise ValidationError("Enter only number")
            elif l != 10:
                raise ValidationError("Enter 10 number")

    def action_send_card(self):
        print("sending mail")
        template_id = self.env.ref('school.email_employe_template').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)


class SchoolInherit(models.Model):

    _inherit = 'school.table'

    student_refence_no = fields.Char(string="Student Reference")