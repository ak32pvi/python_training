# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Robert", middlename="Mozart", lastname="Volf", nickname="anonymous", company="google", title="title", address="ourcountry",
                      homephone="12345", mobilephone="84633", workphone="123456", secondaryphone="09909", fax="77777", homepage="homepage field", byear="1988", ayear="2018",
                      address2="Earth", notes="Hello world!")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.create(Contact(firstname="", middlename="", lastname="", title="", address=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)

