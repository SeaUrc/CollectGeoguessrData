from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pyperclip
import time
from PIL import Image
import os


""" PATH = "/Users/nick/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.mapcrunch.com/")
driver.fullscreen_window()

button = driver.find_element(By.ID, "go-button")
current_address = driver.find_element(By.ID, "address").text
button.click()

google_address = driver.find_element(By.XPATH, "//div[@class='gm-iv-address-link']/a").get_attribute('href')
 """
pyautogui.PAUSE = 1

def share():
    pyautogui.moveTo(370, 167)
    pyautogui.click()

def getShare():
    pyautogui.moveTo(170, 312)
    pyautogui.click()
    pyautogui.rightClick()
    pyautogui.moveTo(270, 354)
    pyautogui.click()

def go():
    pyautogui.moveTo(456, 164)
    pyautogui.click()

def screenshot():
    im = pyautogui.screenshot(region=(0,388, 2880, 1202))
    return im.convert('RGB')

def take_screenshots(lat, long, x, y, z, iter):
    save_dir = "./imgs/" + str(iter) + "/"
    try:
        os.mkdir(save_dir)
    except:
        print(save_dir + " dir already exists")
    sc = screenshot()
    sc.save(save_dir + "0.jpg")
    for i in range(3):
        x += 90
        url = 'http://www.mapcrunch.com/p/'+ str(lat) + '_' + str(long) + '_' + str(x) + '_' + str(y) + '_' + str(z)
        pyautogui.moveTo(223, 61)
        pyautogui.click()
        pyautogui.write(url)
        pyautogui.press('enter')
        time.sleep(2)
        sc = screenshot()
        sc.save(save_dir + str(i+1) + ".jpg")

def main():
    time.sleep(2)
    print(pyautogui.size())

    for i in range(1):
        share()
        getShare()
        share()

        address = pyperclip.paste()
        truncated_start_address = address.split('/')[-1]
        address_info_str = truncated_start_address.split('_')
        address_info = [eval(i) for i in address_info_str]

        take_screenshots(address_info[0], address_info[1], address_info[2], address_info[3], address_info[4], i)
        go()

if __name__ == "__main__":
    main()
