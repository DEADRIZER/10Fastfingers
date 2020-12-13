from time import sleep

from selenium.webdriver.chrome.service import Service 
from selenium import webdriver

service = Service('D:/Programme/Chromium/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://10fastfingers.com/advanced-typing-test/french');

sleep(3)

for i in range(1, 300):
	html= driver.find_element_by_xpath(f'//*[@id="row1"]/span[{i}]')
	mot= html.text.split()
	inputArea= driver.find_element_by_xpath('//*[@id="inputfield"]')
	inputArea.send_keys(mot)
	inputArea.send_keys(" ")
