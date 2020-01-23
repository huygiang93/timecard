from selenium import webdriver

driver = webdriver.Firefox()
# login = driver
driver.get("https://westvalley.fastime.com")

#assert "west" in driver.title

# Assignment Number and Employee ID to login
ass_number = driver.find_element_by_id("txtOrderNumber")
ass_number.clear()
ass_number.send_keys("") ## assignment number
emp_id = driver.find_element_by_name("txtSSN")
emp_id.clear()
emp_id.send_keys("") ## employee id
# click Login button
driver.find_element_by_id("btnSubmit").click()
# terms page
driver.find_element_by_id("btnAccept").click()

# time entry page
#
# Monday
monday_in = driver.find_element_by_id("TCC_txt_6_0_MON_IN")
monday_in.clear()
monday_in.send_keys("09:00")
monday_in = driver.find_element_by_id("TCC_optAMPM_6_0_MON_IN")
monday_in.send_keys("AM")

monday_lunch = driver.find_element_by_id("TCC_txt_6_0_MON_OUT")
monday_lunch.send_keys("12:00")
monday_lunch = driver.find_element_by_id("TCC_optAMPM_6_0_MON_OUT")
monday_lunch.send_keys("PM")

monday_lunch = driver.find_element_by_id("TCC_txt_6_1_MON_IN")
monday_lunch.send_keys("12:30")
monday_lunch = driver.find_element_by_id("TCC_optAMPM_6_1_MON_IN")
monday_lunch.send_keys("PM")

monday_out = driver.find_element_by_id("TCC_txt_6_1_MON_OUT")
monday_out.send_keys("05:30")
monday_out = driver.find_element_by_id("TCC_optAMPM_6_1_MON_OUT")
monday_out.send_keys("PM")

# Tuesday
tuesday_in = driver.find_element_by_id("TCC_txt_5_0_TUE_IN")
tuesday_in.clear()
tuesday_in.send_keys("09:00")
tuesday_in = driver.find_element_by_id("TCC_optAMPM_5_0_TUE_IN")
tuesday_in.send_keys("AM")

tuesday_lunch = driver.find_element_by_id("TCC_txt_5_0_TUE_OUT")
tuesday_lunch.send_keys("12:00")
tuesday_lunch = driver.find_element_by_id("TCC_optAMPM_5_0_TUE_OUT")
tuesday_lunch.send_keys("PM")

tuesday_lunch = driver.find_element_by_id("TCC_txt_5_1_TUE_IN")
tuesday_lunch.send_keys("12:30")
tuesday_lunch = driver.find_element_by_id("TCC_optAMPM_5_1_TUE_IN")
tuesday_lunch.send_keys("PM")

tuesday_out = driver.find_element_by_id("TCC_txt_5_1_TUE_OUT")
tuesday_out.send_keys("05:30")
tuesday_out = driver.find_element_by_id("TCC_optAMPM_5_1_TUE_OUT")
tuesday_out.send_keys("PM")

# Wednesday
wednesday_in = driver.find_element_by_id("TCC_txt_4_0_WED_IN")
wednesday_in.clear()
wednesday_in.send_keys("09:00")
wednesday_in = driver.find_element_by_id("TCC_optAMPM_4_0_WED_IN")
wednesday_in.send_keys("AM")

wednesday_lunch = driver.find_element_by_id("TCC_txt_4_0_WED_OUT")
wednesday_lunch.send_keys("12:00")
wednesday_lunch = driver.find_element_by_id("TCC_optAMPM_4_0_WED_OUT")
wednesday_lunch.send_keys("PM")

wednesday_lunch = driver.find_element_by_id("TCC_txt_4_1_WED_IN")
wednesday_lunch.send_keys("12:30")
wednesday_lunch = driver.find_element_by_id("TCC_optAMPM_4_1_WED_IN")
wednesday_lunch.send_keys("PM")

wednesday_out = driver.find_element_by_id("TCC_txt_4_1_WED_OUT")
wednesday_out.send_keys("05:30")
wednesday_out = driver.find_element_by_id("TCC_optAMPM_4_1_WED_OUT")
wednesday_out.send_keys("PM")

# Thursday
thursday_in = driver.find_element_by_id("TCC_txt_3_0_THU_IN")
thursday_in.clear()
thursday_in.send_keys("09:00")
thursday_in = driver.find_element_by_id("TCC_optAMPM_3_0_THU_IN")
thursday_in.send_keys("AM")

thursday_lunch = driver.find_element_by_id("TCC_txt_3_0_THU_OUT")
thursday_lunch.send_keys("12:00")
thursday_lunch = driver.find_element_by_id("TCC_optAMPM_3_0_THU_OUT")
thursday_lunch.send_keys("PM")

thursday_lunch = driver.find_element_by_id("TCC_txt_3_1_THU_IN")
thursday_lunch.send_keys("12:30")
thursday_lunch = driver.find_element_by_id("TCC_optAMPM_3_1_THU_IN")
thursday_lunch.send_keys("PM")

thursday_out = driver.find_element_by_id("TCC_txt_3_1_THU_OUT")
thursday_out.send_keys("05:30")
thursday_out = driver.find_element_by_id("TCC_optAMPM_3_1_THU_OUT")
thursday_out.send_keys("PM")

# Friday
friday_in = driver.find_element_by_id("TCC_txt_2_0_FRI_IN")
friday_in.clear()
friday_in.send_keys("09:00")
friday_in = driver.find_element_by_id("TCC_optAMPM_2_0_FRI_IN")
friday_in.send_keys("AM")

friday_lunch = driver.find_element_by_id("TCC_txt_2_0_FRI_OUT")
friday_lunch.send_keys("12:00")
friday_lunch = driver.find_element_by_id("TCC_optAMPM_2_0_FRI_OUT")
friday_lunch.send_keys("PM")

friday_lunch = driver.find_element_by_id("TCC_txt_2_1_FRI_IN")
friday_lunch.send_keys("12:30")
friday_lunch = driver.find_element_by_id("TCC_optAMPM_2_1_FRI_IN")
friday_lunch.send_keys("PM")

friday_out = driver.find_element_by_id("TCC_txt_2_1_FRI_OUT")
friday_out.send_keys("05:30")
friday_out = driver.find_element_by_id("TCC_optAMPM_2_1_FRI_OUT")
friday_out.send_keys("PM")

# click review
driver.find_element_by_id("btnReview").click()
driver.find_element_by_id("saveLater").click()

#driver.find_element_by_id("con").click()
