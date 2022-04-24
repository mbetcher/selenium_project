from selenium.webdriver.common.by import By

class eobuwieHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_input_xpath = '//form[@class="header-search snr"]/input[@type="search"]'
        self.search_button_xpath = '//form[@class="header-search snr"]/button[@type="submit"]'

    def search_in_eobuwie(self, text):
        self.driver.find_element(By.XPATH, self.search_input_xpath).send_keys(text)
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

