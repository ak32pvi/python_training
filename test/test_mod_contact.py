# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="firstname", middlename="middlename", lastname="lastname", title="title", country="ukraine"))
    app.session.logout()