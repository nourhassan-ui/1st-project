from odoo import models, fields 

class CollegeErpModel(models.Model):
    _name = "college_erp.model"
    _description = "College ERP Model"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
