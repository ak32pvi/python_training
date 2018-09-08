from model.contact import Contact


def test_assert_contact(app, db):
    contacts_ui = app.contact.get_contact_list()
    contacts_db = db.get_contact_list()
    assert sorted(contacts_ui, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)