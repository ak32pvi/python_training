# # -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_modify_some_contact(app, db, check_ui):
    contact = Contact(firstname="Robert", middlename="Mozart", lastname="Volf", nickname="anonymous", company="google",
                      title="title", address="ourcountry",
                          homephone="12345", mobilephone="84633", workphone="123456", secondaryphone="09909", fax="77777",
                          email="abc@gmail.com", email2="support@gmail.com", email3="contact@gmail.com", homepage="homepage field", byear="1988",
                          ayear="2018", address2="Earth", notes="Hello world!")
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    old_contacts.remove(random_contact)
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(random_contact.id, contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
# from model.contact import Contact
# from random import randrange
#
#
# def test_modify_first_contact_firstname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(firstname="Robert", middlename="Mozart", lastname="Volf", nickname="anonymous", company="google", title="title", address="ourcountry",
#                       homephone="12345", mobilephone="84633", workphone="123456", secondaryphone="09909", fax="77777",
#                       email="abc@gmail.com", email2="support@gmail.com", email3="contact@gmail.com", homepage="homepage field", byear="1988",
#                       ayear="2018", address2="Earth", notes="Hello world!")
#     contact.id = old_contacts[index].id
#     app.contact.modify_contact_by_index(index, contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#
#
# def test_modify_first_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(middlename="New middlename"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
