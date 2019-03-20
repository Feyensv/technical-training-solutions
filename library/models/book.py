# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    author_ids = fields.Many2many(
        comodel_name="library.partner",
        string="Authors"
    )
    edition_date = fields.Date(string='Edition date')
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one(
        'library.publisher',
        string='Publisher')
    rental_ids = fields.One2many(
        'library.rental',
        'book_id',
        string='Rentals')
