from selenium import webdriver
from bs4 import BeautifulSoup
import sys

class Acorn:
    def __init__(self, browser):
        self._browser = browser
        self._test = 'https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch#/courses/0'

    def current_courses(self):
        self._browser.get(self._test)
        soup = BeautifulSoup(self._browser.page_source, 'html.parser')

        data = soup.find_all(attrs={'class': 'enrolment-code'})

        for i in data:
            print(' '.join(i.getText().replace('\n', ' ').split()))

        self._browser.quit()

    def today_event(self):
        url = 'https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch#'
        self._browser.get(url)
        soup = BeautifulSoup(self._browser.page_source, 'html.parser')
        data = soup.find_all('div', attrs={'class': 'event'})

        for item in data:
            it = item.find_all('div', attrs={'class': 'flex-item'})
            self.parse_event(it)
        return

    def parse_event(self, data):
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

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('https://acorn.utoronto.ca/sws/auth/login.do?verify.dispatch')
    usernameStr = 'cheng126'
    passwordStr = 'Cheng!St452196@'
    username = browser.find_element_by_id('username')
    username.send_keys(usernameStr)

    password = browser.find_element_by_id('password')
    password.send_keys(passwordStr)

    login = browser.find_element_by_name('_eventId_proceed')
    login.click()
    test = Acorn(browser)
    test.today_event()
