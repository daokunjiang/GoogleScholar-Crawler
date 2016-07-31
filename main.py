# coding = utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://scholar.google.com/citations?hl=zh-CN&user=gM5i-iYAAAAJ&view_op=list_works&sortby=pubdate')
f = open('xue.txt', 'w', encoding='utf-8')
results = ''
re_len_before = 0
while 1:
    inputBtn = driver.find_element_by_id('gsc_bpf_more').click()
    results = driver.page_source
    re_len = len(results)
    if (re_len_before != 0) & (re_len == re_len_before):
        break
    re_len_before = re_len

f.write(results)

# inputBtn.send_keys('bing xie')
# driver.find_element_by_id('gs_hp_tsb').click()
# driver.find_element_by_xpath('//*[@id="gs_ccl"]/div[2]/table/tbody/tr/td[2]/h4/a').click()