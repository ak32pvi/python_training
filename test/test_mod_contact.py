# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Robert", middlename="Mozart", lastname="Volf", nickname="anonymous", company="google", title="title", address="ourcountry",
                      homephone="12345", mobilephone="84633", workphone="123456", secondaryphone="09909", fax="77777", homepage="homepage field", byear="1988", ayear="2018",
                      address2="Earth", notes="Hello world!")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_first_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(middlename="New middlename"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
