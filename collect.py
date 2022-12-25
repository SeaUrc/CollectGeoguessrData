import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageGrab
from googleAddress2LatLong import address2latlong


PATH = "/Users/nick/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.mapcrunch.com/")
driver.fullscreen_window()

button = driver.find_element(By.ID, "go-button")
current_address = driver.find_element(By.ID, "address").text
button.click()

share = driver.find_element(By.ID, "share-button")
share.click()

def take_sc(x):
    share.click()
    time.sleep(1)
    im = ImageGrab.grab().convert('RGB')
    im.save('imgs/' + x + '.jpg')
    time.sleep(1)
    share.click()


for x in range(2):
    while (current_address == driver.find_element(By.ID, "address").text):
        time.sleep(1)
    # take_sc(str(x+1))
    print(driver.find_element(By.XPATH, "//a[@class='gm-iv-marker-link']").get_attribute('href'))
    time.sleep(1)
    button.click()

print(driver.find_element(By.ID, "address").text)