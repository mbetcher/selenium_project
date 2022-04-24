import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from page_object_patterns.pages.eobuwie_home_page import eobuwieHomePage
from page_object_patterns.pages.eobuwie_result_page import eobuwieResultPage


class RemoveTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.eobuwie.com.pl/")
        self.driver.implicitly_wait(10)

    def testRemoveItem(self):
        # KROKI
        driver = self.driver
        # Akceptacja cookies
        driver.find_element(By.XPATH, '//div[@class="e-consents-alert__actions"]/button[@type="button"]').click()

        # 1. Wpisanie w wyszukiwarkę "Buty adidas" i kliknięcie w lupkę "Szukaj"
        home_page = eobuwieHomePage(self.driver)
        home_page.search_in_eobuwie("buty adidas")

        #Wyłączenie wyskakującego okna o przecenie
        driver.find_element(By.ID, 'automated_belka_exit').click()
        driver.find_element(By.XPATH, '//div[@id = "newsletter_banner_exit_salomon"]').click()

        # 2. Wybór butów - pierwszych z listy
        result_page = eobuwieResultPage(self.driver)
        result_page.open_first_result()

        # 3. Kliknięcie w "Wybierz rozmiar"
        driver.find_element(By.XPATH, '//button[@class="e-size-picker__select"]').click()
        sleep(5)

        # 4. Wybór rozmiaru
        sizes = driver.find_element(By.XPATH, '//div[@class="e-size-picker__options"]')
        # Sprawdzenie ilości elementów dla sizes
        # print(int(sizes.get_attribute('childElementCount')))
        for i in range(int(sizes.get_attribute('childElementCount'))):
            size_choice = driver.find_element(By.XPATH,
                                              '//div[@class="e-size-picker__options"]/button[{}]'.format(i + 1))
            size_text = driver.find_element(By.XPATH,
                                            '//div[@class="e-size-picker__options"]/button[{}]/span[1]/span'.format(
                                                i + 1)).get_attribute('innerHTML')
            # Wybranie dostępnego rozmiaru
            name = size_choice.get_attribute("className")
            if name == 'e-size-picker__option e-size-picker-option e-size-picker-option--disabled':
                print('Brak rozmiaru {}'.format(size_text))
                continue
            elif name == 'e-size-picker__option e-size-picker-option':
                print('Wybrano rozmiar {}'.format(size_text))
                size_choice.click()
                break
            else:
                print('Błędna nazwa klasy')
                break

        sleep(5)
        driver.execute_script("window.scrollTo(0, 1080)")

        # 5. Dodanie do koszyka
        driver.find_element(By.XPATH, '//button[@data-testid = "product-add-to-cart-button"]').click()

        # 6. Kontynuowanie zakupów
        driver.find_element(By.XPATH, '//div[@class="precart-popup__actions"]/button[@type="button"]').click()

        # 7. Wpisanie w wyszukiwarkę "torebka" i kliknięcie w lupkę "Szukaj"
        home_page = eobuwieHomePage(self.driver)
        home_page.search_in_eobuwie("torebka")

        # 8. Wybór torebki - pierwszej z listy
        result_page = eobuwieResultPage(self.driver)
        result_page.open_first_result()

        # 9. Dodanie do koszyka
        driver.find_element(By.XPATH, '//button[@data-testid = "product-add-to-cart-button"]').click()

        # 10. Przejście do koszyka
        driver.find_element(By.XPATH, '//a[@data-testid ="product-go-to-cart-link"]').click()

        #11. Usunięcie butów z koszyka
        driver.find_element(By.XPATH, '//a[@class="cart-item__remove"]').click()

        # Sprawdzenie
        shopping = driver.find_element(By.XPATH, '//span[@class="header-count"]').get_attribute('innerHTML')
        print("Ilość obiektów w koszyku" + shopping)
        self.assertEqual("\n  (1)\n", shopping)

        price_total = driver.find_element(By.XPATH, '//span[@class = "e-cart-total-item__value"]').text
        price_item = driver.find_element(By.XPATH, '//div[@class = "cart-item__price-wrapper"]').text
        print("Cena obiektu wynosi " + price_item)
        print("Cena całkowita za obiekt wynosi " + price_total)
        self.assertEqual(price_total, price_item)

        # Poczekaj, aby zobaczyć co się dzieje
        sleep(5)

    def tearDown(self):
        self.driver.quit()



