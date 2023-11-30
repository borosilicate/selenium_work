import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/home/pi/.config/chromium")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--headless")
#####dr=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver') #,options=chrome_options)
dr=webdriver.Chrome(service=ChromeService('/usr/bin/chromedriver'),options=chrome_options)
#/usr/lib/chromium-browser/chromedriver
time.sleep(10)
dr.get('https://linkedin.com/in/michael-hearn-borosilicate/')
time.sleep(10)
if('borosilicate' not in dr.current_url or dr.current_url != 'https://linkedin.com/in/michael-hearn-borosilicate/'):
    print('ERROR Didnt go to profile! ',dr.current_url)
    exit()
if(   len(dr.find_elements(by=By.XPATH,value='//button[@class="profile-photo-edit__edit-btn"]'))>0 ):
    dr.find_element(by=By.XPATH,value='//button[@class="profile-photo-edit__edit-btn"]').click()
elif( len(dr.find_elements(by=By.XPATH,value='//*[@class="profile-photo-edit__edit-btn"]'))>0 ):
    dr.find_element(by=By.XPATH,value='//*[@class="profile-photo-edit__edit-btn"]').click()
else:
    print('fix find button ')
    exit()
#click ad photo
time.sleep(5)
dr.find_element(by=By.XPATH,value='//span[text()="Add photo"]').click()
time.sleep(5)
elem=dr.find_element(by=By.XPATH,value='//*[@id="image-selector__file-upload-input"]')
time.sleep(5)
elem.send_keys('/home/pi/Pictures/me.linkedin.png')
time.sleep(10)
dr.find_element(by=By.XPATH,value='//span[text()="Save photo"]').click()
time.sleep(25)
dr.find_element(by=By.XPATH,value='//button[@aria-label="Edit profile background"]').click()
time.sleep(5)
dr.find_element(by=By.XPATH,value='//span[text()="Change photo"]').click()
time.sleep(5)
elem=dr.find_element(by=By.XPATH,value='//input[@class="background-image-chooser-modal__input"]')
time.sleep(5)
elem.send_keys('/home/pi/Pictures/data_science_out.png')
time.sleep(10)
dr.find_element(by=By.XPATH,value='//span[text()="Apply"]').click()
time.sleep(10)
dr.close()
display.stop()
