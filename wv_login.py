from selenium import webdriver
from bs4 import BeautifulSoup as bs

start_url = 'https://westvalley.fastime.com'
 


login = webdriver.Firefox()
login.get(start_url)

#assert "west" in driver.title

# Assignment Number and Employee ID to login
def login_web():
    ass_number = login.find_element_by_id("txtOrderNumber")
    ass_number.clear()
    ass_number.send_keys("94263")
    emp_id = login.find_element_by_name("txtSSN")
    emp_id.clear()
    emp_id.send_keys("194512")
    login.find_element_by_id("btnSubmit").click()
    login.find_element_by_id("btnAccept").click()

login_web()

# click Login button

#navigate to the time input page


#filling times



def monday_in():
    # coming in
    monday_first_in  = login.find_element_by_id("TCC_txt_6_0_MON_IN")
    monday_first_in.clear()
    monday_first_in.send_keys("09:00")

    monday_second_in  = login.find_element_by_id("TCC_txt_6_1_MON_IN")
    monday_second_in.clear()
    monday_second_in.send_keys("12:30")
    login.find_element_by_id("TCC_optAMPM_6_0_MON_OUT").send_keys("PM")
monday_in()


def monday_out():
    monday_first_out  = login.find_element_by_id("TCC_txt_6_0_MON_OUT")
    monday_first_out.clear()
    monday_first_out.send_keys("12:00")
    

    monday_second_out  = login.find_element_by_id("TCC_txt_6_1_MON_OUT")
    monday_second_out.clear()
    monday_second_out.send_keys("05:30")
monday_out()










# Tuesday fill


def tuesday_in():
    tuesday_first_in  = login.find_element_by_id("TCC_txt_5_0_TUE_IN")
    tuesday_first_in.clear()
    tuesday_first_in.send_keys("09:00")

    tuesday_second_in  = login.find_element_by_id("TCC_txt_5_1_TUE_IN")
    tuesday_second_in.clear()
    tuesday_second_in.send_keys("12:30")
tuesday_in()


def tuesday_out():
    tuesday_first_out  = login.find_element_by_id("TCC_txt_5_0_TUE_OUT")
    tuesday_first_out.clear()
    tuesday_first_out.send_keys("12:00")
    login.find_element_by_id("TCC_optAMPM_5_0_TUE_OUT").send_keys("PM")

    tuesday_second_out  = login.find_element_by_id("TCC_txt_5_1_TUE_OUT")
    tuesday_second_out.clear()
    tuesday_second_out.send_keys("05:30")
tuesday_out()




# Wednesday fill


def wednesday_in():
    wednesday_first_in  = login.find_element_by_id("TCC_txt_4_0_WED_IN")
    wednesday_first_in.clear()
    wednesday_first_in.send_keys("09:00")

    wednesday_second_in  = login.find_element_by_id("TCC_txt_4_1_WED_IN")
    wednesday_second_in.clear()
    wednesday_second_in.send_keys("12:30")
wednesday_in()


def wednesday_out():
    wednesday_first_out  = login.find_element_by_id("TCC_txt_4_0_WED_OUT")
    wednesday_first_out.clear()
    wednesday_first_out.send_keys("12:00")
    login.find_element_by_id("TCC_optAMPM_4_0_WED_OUT").send_keys("PM")

    wednesday_second_out  = login.find_element_by_id("TCC_txt_4_1_WED_OUT")
    wednesday_second_out.clear()
    wednesday_second_out.send_keys("05:30")
wednesday_out()



# Thursday fill


def thursday_in():
    thursday_first_in  = login.find_element_by_id("TCC_txt_3_0_THU_IN")
    thursday_first_in.clear()
    thursday_first_in.send_keys("09:00")

    thursday_second_in  = login.find_element_by_id("TCC_txt_3_1_THU_IN")
    thursday_second_in.clear()
    thursday_second_in.send_keys("12:30")
thursday_in()


def thursday_out():
    thursday_first_out  = login.find_element_by_id("TCC_txt_3_0_THU_OUT")
    thursday_first_out.clear()
    thursday_first_out.send_keys("12:00")
    login.find_element_by_id("TCC_optAMPM_3_0_THU_OUT").send_keys("PM")

    thursday_second_out  = login.find_element_by_id("TCC_txt_3_1_THU_OUT")
    thursday_second_out.clear()
    thursday_second_out.send_keys("05:30")
thursday_out()





# Friday fill


def friday_in():
    friday_first_in  = login.find_element_by_id("TCC_txt_2_0_FRI_IN")
    friday_first_in.clear()
    friday_first_in.send_keys("09:00")

    friday_second_in  = login.find_element_by_id("TCC_txt_2_1_FRI_IN")
    friday_second_in.clear()
    friday_second_in.send_keys("12:30")
friday_in()


def friday_out():
    friday_first_out  = login.find_element_by_id("TCC_txt_2_0_FRI_OUT")
    friday_first_out.clear()
    friday_first_out.send_keys("12:00")
    login.find_element_by_id("TCC_optAMPM_2_0_FRI_OUT").send_keys("PM")

    friday_second_out  = login.find_element_by_id("TCC_txt_2_1_FRI_OUT")
    friday_second_out.clear()
    friday_second_out.send_keys("05:30")
friday_out()







# Review


login.find_element_by_id("btnReview").click()