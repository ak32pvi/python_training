# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    app.contact.add_to_group(contact_id=contact.id, group_id=group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    for contact in contacts_in_group:
        if contact.id == contact.id:
            assert True