from odoo import models, fields


class Faculty(models.Model):
    _name = "college_erp.faculty"
    _description = "Faculty"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    course_ids = fields.One2many('college_erp.course', 'faculty_id', string="Courses")


class Course(models.Model):
    _name = "college_erp.course"
    _description = "Course"

    name = fields.Char(string="Course Name", required=True)
    code = fields.Char(string="Code")
    faculty_id = fields.Many2one('college_erp.faculty', string="Faculty")
    student_ids = fields.Many2many('college_erp.student', string="Students")


class Student(models.Model):
    _name = "college_erp.student"
    _description = "Student"

    name = fields.Char(string="Student Name", required=True)
    email = fields.Char(string="Email")
    dob = fields.Date(string="Date of Birth")
    course_ids = fields.Many2many('college_erp.course', string="Courses")
