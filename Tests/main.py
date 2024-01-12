from time import sleep
from selenium import webdriver
from pageOps import LoginPage 
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Access environment variables
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# initializes the Firefox driver and sets it to browser.
browser = webdriver.Firefox()
# browser.maximize_window()
loginOps = LoginPage(browser)
loginOps.login(username, password)
sleep(5)
browser.close()


