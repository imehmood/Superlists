from selenium import webdriver

browser = webdriver.Firefox()
#browser = webdriver.Firefox(firefox_profile='/home/imran/.mozilla/firefox/65h4g630.development_profile')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
