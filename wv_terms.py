from selenium import webdriver

terms_page = webdriver.Firefox()
terms_page.get("https://westvalley.fastime.com/Individual/TermsofUse.aspx?type=0")

terms_page.find_element_by_id("btnAccept").click()
