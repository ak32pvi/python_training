# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New firstname"))
    app.session.logout()


def test_modify_first_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="New middlename"))
    app.session.logout()
