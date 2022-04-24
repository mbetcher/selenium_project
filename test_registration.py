# Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

# Dane testowe
email = "test.pl"
firstname = "Anna"
lastname = "Tester"
password = "Test1234"


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.eobuwie.com.pl/")
        self.driver.implicitly_wait(10)

    def testRegistrationEntered(self):
        # KROKI
        driver = self.driver

        # Akceptacja cookies
        driver.find_element(By.CSS_SELECTOR, 'button.e-button--type-primary:nth-child(1)').click()

        # 1 Polecenie "Zarejestruj się"
        driver.find_element(By.XPATH, '//a[@href="https://www.eobuwie.com.pl/customer/account/create/"]').click()

        # 2. Wpisanie imienia
        driver.find_element(By.ID, 'firstname').send_keys(firstname)

        # 3. Wpisanie nazwiska
        driver.find_element(By.ID, 'lastname').send_keys(lastname)

        # 4. Wpisanie maila
        driver.find_element(By.ID, 'email_address').send_keys(email)

        # 5. Wpisanie hasła
        driver.find_element(By.ID, 'password').send_keys(password)

        # 6. Powtórne wpisanie hasła
        driver.find_element(By.ID, 'confirmation').send_keys(password)

        driver.execute_script("window.scrollTo(0, 1080)")

        # 7. Zaakceptowanie oświadczenia
        driver.find_element(By.XPATH, '//label[@class = "checkbox-wrapper__label"]').click()

        #Wyłączenie wyskakującego okna o przecenie
        driver.find_element(By.ID, 'automated_belka_exit').click()
        driver.find_element(By.XPATH, '//div[@id = "newsletter_banner_exit_salomon"]').click()

        # 8. Kliknięcie "Załóż nowe konto"
        driver.find_element(By.ID, 'create-account').click()

        error = driver.find_element(By.XPATH, '//span[@class = "help-block form-error"]').text
        self.assertEqual("Wprowadzono niepoprawny adres e-mail", error)


        # Poczekaj, aby zobaczyć co się dzieje
        sleep(10)

    def tearDown(self):
        self.driver.quit()