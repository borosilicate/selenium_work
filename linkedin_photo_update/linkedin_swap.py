import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/home/pi/.config/chromium")
#chrome_options.add_argument("--headless")
#'me.linkedin.png'
#dr = webdriver.Chrome(service=Service(ChromeDriverManager().install(),options=chrome_options))
#dr=webdriver.Chrome('/usr/lib/chromium/chromium',options=chrome_options)
dr=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',options=chrome_options)
dr.get('https://linkedin.com/in/michael-hearn-borosilicate/')
time.sleep(10)
dr.find_element(By.CLASS_NAME, "profile-photo-edit__edit-btn").click()
#click ad photo
dr.find_element(by=By.XPATH,value='//span[text()="Add photo"]').click()
time.sleep(5)
elem=dr.find_element(by=By.XPATH,value='//*[@id="image-selector__file-upload-input"]')
time.sleep(5)
elem.send_keys('/home/pi/Pictures/me.linkedin.png')
time.sleep(10)
dr.find_element(by=By.XPATH,value='//span[text()="Save photo"]').click()
time.sleep(20)
print('Should be uploaded!')
dr.close()
dr.quit()
display.stop()
