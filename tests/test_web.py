import pytest

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

def test_basic_duckduckgo_search(browser,config_base_url):
  # Set up test case data
  PHRASE = 'test'

  # Search for the phrase
  search_page = DuckDuckGoSearchPage(browser, config_base_url)
  search_page.navigate()
  search_page.search(PHRASE)

  # Verify that results appear
  result_page = DuckDuckGoResultPage(browser)
  assert result_page.link_div_count() > 0
  assert result_page.phrase_result_count(PHRASE) > 0
  assert result_page.search_input_value() == PHRASE