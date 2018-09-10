# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Publisher(models.Model):
    _name = 'library.publisher'
    _description = 'Publisher'

    name = fields.Char()
