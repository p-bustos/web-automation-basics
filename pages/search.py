from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:
  URL = ''

  SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

  def __init__(self, browser, config_base_url):
    self.browser = browser
    self.base_url = config_base_url

  def navigate(self):
    self.browser.get(self.base_url + self.URL)

  def search(self, phrase):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase + Keys.RETURN)