# coding = utf-8

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://xs.glgoo.com/')

inputBtn = driver.find_element_by_id('gs_hp_tsi')
inputBtn.send_keys('bing xie')
driver.find_element_by_id('gs_hp_tsb').click()
driver.find_element_by_xpath('//*[@id="gs_ccl"]/div[2]/table/tbody/tr/td[2]/h4/a').click()
results = driver.page_source
print(results)