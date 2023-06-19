from selene import have, be

from constants.read_env import ReadEnv
from locators.web_locators import WebLocators


class StartPage:
    def __init__(self, setup_browser):
        self.setup_browser = setup_browser
        self.main_logo = self.setup_browser.element(WebLocators.main_logo)
        self.menu = self.setup_browser.element(WebLocators.menu)
        self.delivery = self.setup_browser.element(WebLocators.delivery)
        self.promos = self.setup_browser.element(WebLocators.promos)
        self.news = self.setup_browser.element(WebLocators.news)
        self.addresses = self.setup_browser.element(WebLocators.addresses)
        self.banquets = self.setup_browser.element(WebLocators.banquets)
        self.vacancies = self.setup_browser.element(WebLocators.vacancies)
        self.franchise = self.setup_browser.element(WebLocators.franchise)
        self.home_cooking = self.setup_browser.element(WebLocators.home_cooking)

    def open_browser(self, URL):
        self.setup_browser.open(URL)
        return self

    def check_logo(self, main_page):
        self.setup_browser.should(have.title(main_page))
        return self

    def check_menu(self):
        self.menu.click()

    def check_delivery(self):
        self.delivery.click()

    def check_promos(self):
        self.promos.click()

    def check_news(self):
        self.news.click()

    def check_addresses(self):
        self.addresses.click()

    def check_banquets(self):
        self.banquets.click()

    def check_vacancies(self):
        self.vacancies.click()

    def check_franchise(self):
        self.franchise.click()

    def check_home_cooking(self):
        self.home_cooking.click()

    def check_tabs(self, main_page):
        self.check_logo(main_page)
        self.check_menu()
        self.check_delivery()
        self.check_promos()
        self.check_news()
        self.check_addresses()
        self.check_banquets()
        self.check_vacancies()
        self.check_franchise()
        self.check_home_cooking()
        return self



    # def check_page(self, vk_header):
    #     self.vk_header.should(have.text(vk_header))
    #
    # def get_login(self, login):
    #     self.login.should(be.blank).type(login)
    #
    # def check_box_click(self):
    #     self.check_box.click()
    #
    # def exit_click(self):
    #     self.exit.click()
    #
    # def enter_password(self, check_password):
    #     self.enter_password.should(have.text(check_password))
    #     self.enter_password.click()
    #
    # def get_password(self, password):
    #     self.password.should(be.blank).type(password)
    #
    # def click_continue(self):
    #     self.continue_.click()
    #
    # def authorization(self, vk_header, authorization, check_password):
    #     self.check_page(vk_header)
    #     self.get_login(authorization.login)
    #     self.check_box_click()
    #     self.exit_click()
    #     self.enter_password(check_password)
    #     self.get_password(authorization.password)
    #     self.click_continue()
    #     return self
