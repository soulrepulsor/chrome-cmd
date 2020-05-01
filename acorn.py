from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from recent_academic_history import RecentAcademicHistory

import os

from dotenv import load_dotenv

class Acorn:
    def __init__(self, browser):
        self._browser = browser
        self._test = 'https://acorn.utoronto.ca/sws/#/courses/0'

    def current_courses(self):

        finish = False

        url = 'https://acorn.utoronto.ca/sws/#/courses/'
        index = 0

        while finish is False:
            new_url = url + str(index)
            self._browser.get(new_url)
            wait = WebDriverWait(self._browser, 1)
            wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, 'enrolment-code'))
            )

            try:
                soup = BeautifulSoup(self._browser.page_source, 'html.parser')
                data = soup.find_all(attrs={'class': 'enrolment-code'})
                title = soup.find_all(attrs={'class': 'tab-heading'})

                print(title[index].get_text())

                for i in data:
                    print(' '.join(i.getText().replace('\n', ' ').split()))
                print('\n')
                if index + 1 >= len(title):
                    break

                index += 1

            except Exception:
                return

        self._browser.quit()

    def today_event(self):
        url = 'https://acorn.utoronto.ca/sws/#'
        self._browser.get(url)
        soup = BeautifulSoup(self._browser.page_source, 'html.parser')
        data = soup.find_all('div', attrs={'class': 'event'})

        if not data:
            print('You don\'t have any activities scheduled for today')

        for item in data:
            it = item.find_all('div', attrs={'class': 'flex-item'})
            self._parse_event(it)
        return

    def _parse_event(self, data):
        info = {
            'Start Time': '',
            'End Time': '',
            'Course Code': '',
            'Lecture Code': '',
            'Location': ''
        }
        result = ''

        for item in data:
            raw_str = ' '.join(item.text.strip('\n').split())
            result += raw_str + ' '

        partition = result[:result.find(',')].split(' - Room: ')

        query_item = partition[0].split()
        query_item.append(partition[1])
        for i in query_item:
            if ':' in i:
                if not info['Start Time']:
                    info['Start Time'] = i
                else:
                    info['End Time'] = i
            elif i[0:2].isupper() and i[2] == ' ':
                    info['Location'] = i
            elif i[0:3].isupper() and i[3].isnumeric():
                if not i[0:3] == 'LEC':
                    info['Course Code'] = i
                else:
                    info['Lecture Code'] = i

        message = ''
        for key in info:
            message +=  key + ': ' + info[key] + '\n'

        print(message)

    def recent_academic_history(self):
        rah = RecentAcademicHistory(self._browser)
        rah.recent_academic_history()

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('https://acorn.utoronto.ca/sws/#')
    load_dotenv(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.env'))

    usernameStr = os.getenv('UOFT_UTORID')
    passwordStr = os.getenv('UOFT_PASSWORD')

    username = browser.find_element_by_id('username')
    username.send_keys(usernameStr)

    password = browser.find_element_by_id('password')
    password.send_keys(passwordStr)

    login = browser.find_element_by_name('_eventId_proceed')
    login.click()
    test = Acorn(browser)
    test.recent_academic_history()
