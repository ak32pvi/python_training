# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.helpers.session.login(username="admin", password="secret")
    app.helpers.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname", title="title", country="ukraine"))
    app.helpers.session.logout()


def test_add_empty_contact(app):
    app.helpers.session.login(username="admin", password="secret")
    app.helpers.contact.create(Contact(firstname="", middlename="", lastname="", title="", country=""))
    app.helpers.session.logout()

