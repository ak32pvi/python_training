# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, db):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts_in_group = orm.get_contacts_in_group(group)
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    if len(contacts_in_group) == 0:
        app.contact.add_to_group(contact_id=contact.id, group_id=group.id)
        app.contact.del_contact_from_group(contact_id=contact.id, group_id=group.id)
        for contact in contacts_in_group:
            if contact.id != contact.id:
                assert True
    else:
        contact_from_group = random.choice(contacts_in_group)
        app.contact.del_contact_from_group(contact_id=contact.id, group_id=group.id)
        for contact in contacts_in_group:
            if contact.id != contact_from_group.id:
                assert True
