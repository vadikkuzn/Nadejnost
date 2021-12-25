import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://sclouddownloader.net/'
music = 'https://soundcloud.com/someone-872656359/bring-me-the-horizon-can-you'
driver.get(url)
time.sleep(2)
inputarea = driver.find_element_by_css_selector('.input-group-field')
inputarea.send_keys(music)
driver.find_element_by_css_selector('.button').click()
time.sleep(2)
driver.find_element_by_xpath("//a[text()='Download Track ']").click()
time.sleep(5)
driver.close()