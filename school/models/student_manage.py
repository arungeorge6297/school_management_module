# -*- coding: utf-8 -*-

from odoo import fields,models,api
from datetime import datetime


class StudentTable(models.Model):

    _name = "studenttable.model"



    school_name = fields. Char(String="School Name")
    class_number = fields.Integer(String="Class")
    roll_number = fields.Integer(String="Roll Number")
    name = fields.Char(String="Name")
    guardian_name = fields.Char(String="Guardian Name")
    gender = fields.Char(String="Gender")
    address = fields.Text(String="Address")
    student_img = fields.Binary(String="student image")
    street = fields.Char(String="Street")
    street2 = fields.Char(String="Street2")
    city = fields.Char(String="City")
    state_id = fields.Many2one('res.partner', String="State id")
    zip = fields.Char(String="Zip")
    country_id = fields.Many2one('res.country', String="country id")

    physics = fields.Integer(string="physics")
    chemistry = fields.Integer(string="Chemistry")
    maths = fields.Integer(string="Maths")
    english = fields.Integer(string="English")
    total = fields.Integer(string="Total")
    date_result = fields.Date(String="Date")

    def action_result_card(self):

         print("")




