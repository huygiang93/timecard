from selenium import webdriver

login = webdriver.Firefox()
login.get("https://westvalley.fastime.com")

#assert "west" in driver.title

# Assignment Number and Employee ID to login
ass_number = login.find_element_by_id("txtOrderNumber")
ass_number.clear()
ass_number.send_keys("94337")
emp_id = login.find_element_by_name("txtSSN")
emp_id.clear()
emp_id.send_keys("194528")

# click Login button
terms = login.find_element_by_id("btnSubmit").click()
accept = terms.find_element_by_id("btnAccept").click()
