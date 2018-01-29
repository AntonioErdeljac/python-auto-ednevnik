from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://ocjene.skole.hr/")
element = driver.find_element_by_name("user_login")
element.send_keys("EMAIL_GOES_HERE")
elementP = driver.find_element_by_name("user_password")
elementP.send_keys("PASSWORD_GOES_HERE")
driver.find_element_by_css_selector('.button.bold').click()
driver.find_element_by_css_selector("a[href*='/pregled/predmeti/1395529310']").click()
