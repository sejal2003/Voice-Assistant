from selenium import webdriver
import time

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
   
    def navigate_to_wikipedia(self, query):
        self.query = query
        self.driver.get(url = "https://www.wikipedia.org")
        search= self.driver.find_element("xpath", '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath",'//*[@id="search-form"]/fieldset/button')
        enter.click()
        time.sleep(60)

'''query is text we want to search'''