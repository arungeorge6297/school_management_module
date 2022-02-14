# -*- coding: utf-8 -*-

from odoo import fields,models


class SchoolTable(models.Model):

    _name = "school.table"


    name = fields. Char(String="School Name")
    school_id = fields.Integer(String="school Id")
    pin_code = fields.Integer(String="Pin Code")
    phone = fields. Char(String="phone Number")
    schoolimg = fields.Binary(String="Image")
    street = fields.Char(String="Street")
    street2 = fields.Char(String="Street2")
    city = fields.Char(String="City")
    state_id = fields.Many2one('res.partner', String="State id")
    zip = fields.Char(String="Zip")
    country_id = fields.Many2one('res.country', String="country id")








