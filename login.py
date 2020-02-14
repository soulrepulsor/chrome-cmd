from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from acorn import Acorn
from dotenv import load_dotenv

import sys
import os

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.env'))

usernameStr = os.getenv('UOFT_UTORID')
passwordStr = os.getenv('UOFT_PASSWORD')

arg = str(sys.argv[1])
option = str(sys.argv[2])

options = Options()

options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)

if arg == 'acorn':
    browser.get('https://acorn.utoronto.ca/sws/auth/login.do?verify.dispatch')

elif arg == 'quercus':
    browser.get('http://q.utoronto.ca/')
elif arg == 'degree':
    browser.get('https://degreeexplorer.utoronto.ca/degreeExplorer/')

username = browser.find_element_by_id('username')
username.send_keys(usernameStr)

password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

login = browser.find_element_by_name('_eventId_proceed')
login.click()

if option == 'cc':
    test = Acorn(browser)
    test.current_courses()

elif option == 'tt':
    test = Acorn(browser)
    test.today_event()
