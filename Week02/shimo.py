from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im')
    time.sleep(1)
    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]')
    btm1.click()
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('18893497960')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/input').send_keys('zzymlyhKemmt520')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    cookies = browser.get_cookies()
    print('.............',cookies)
    time.sleep(3)
    

except Exception as e:
    print(e)
finally:
    #browser.close()
    pass
    
