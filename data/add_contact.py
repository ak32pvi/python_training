from model.contact import Contact
import random
import string


constant = [

    Contact(firstname="firstname1", lastname="lastname1", address="address1"),
    Contact(firstname="firstname", lastname="lastname2", address="address2"),
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", title="", address="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10), company=random_string("company", 10),
            title="title", address=random_string("address", 30),
            homephone="12345", mobilephone="84633", workphone="123456", secondaryphone="09909", fax="77777",
            email="abc@gmail.com", email2="support@gmail.com", email3="contact@gmail.com",
            homepage="homepage field", byear="1988",
            ayear="2018", address2="Earth", notes="Hello world!")
    for i in range(5)
]