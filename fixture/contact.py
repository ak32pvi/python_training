class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(contact)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contact_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.title)
        self.change_field_value("address", contact.country)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_link_text("home").click()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        # modify first contact
        wd.find_element_by_link_text("home").click()
        self.edit_first_contact()
        # fill changes into the form
        self.fill_contact_form(new_contact_data)
        # submit changes
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()

    def edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[3]/td[8]/a').click()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()