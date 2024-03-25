from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.implicitly_wait(30)  # seconds
