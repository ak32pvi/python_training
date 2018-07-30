from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.helpers import Helpers


class Application:

    def __init__ (self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.helpers = Helpers(self)

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()