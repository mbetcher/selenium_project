from selenium.webdriver.common.by import By

class eobuwieResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_result_xpath = "//li[@class='products-list__item'][1]"

    def open_first_result(self):
        self.driver.find_element(By.XPATH, self.search_result_xpath).click()