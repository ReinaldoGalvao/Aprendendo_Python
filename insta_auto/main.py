from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

from selenium import webdriver

# Substitua 'caminho_para_chromedriver' pelo caminho real para o chromedriver.exe no seu sistema
chrome_driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://instagram.com')
driver.maximize_window()

time.sleep(4)


time.sleep(2000)
