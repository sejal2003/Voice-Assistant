from selenium import webdriver
import time


class music():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element("xpath", '//*[@id="dismissible"]')
        video.click()

        time.sleep(10)

