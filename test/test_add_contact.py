# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname", title="title", country="ukraine"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", title="", country=""))

