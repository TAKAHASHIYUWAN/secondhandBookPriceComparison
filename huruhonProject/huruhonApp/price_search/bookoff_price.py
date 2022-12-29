from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER = './chromedriver'
AMAZON_URL = 'https://www.amazon.co.jp/'
BOOKOFF_URL = 'https://www.bookoffonline.co.jp//book/CSfTop.jsp?bg=12'

AUTHER_NAME = ''
WORK_NAME = 'ドストエフスキーとの旅'
PUBLISHER_NAME = ''

def bookoff_search(workname:str,authername:str=None,publishername:str=None,item_num:int=1):
    output_dict = {}
    SEARCH_WORD = workname + '　' + authername + '　' + publishername
    
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(CHROMEDRIVER,chrome_options=options)
    driver.implicitly_wait(10)
    driver.get(BOOKOFF_URL)
    
    driver.find_element(By.ID,'zsSearchFormInput').send_keys(SEARCH_WORD)
    driver.find_element(By.ID,'zsSearchFormButton').click()
    
    usedOrNew = driver.find_element(By.XPATH,f'//*[@id="anchor_link_{item_num}"]/img').get_attribute('alt')
    bookname_elements = driver.find_elements(By.XPATH,f'//*[@id="resList"]/form/div["{item_num + 3}"]/div[1]/p/a')
    price_elements = driver.find_elements(By.CLASS_NAME,'mainprice')
    price_word = price_elements[item_num - 1].text
    # //*[@id="resList"]/form/div[4]/div[1]
    # //*[@id="resList"]/form/div[5]/div[1]
    for i,word in enumerate(price_word) :
        if word == '（' :
            price_word = price_word[:i]
            break
    
    price_word = price_word.strip('￥') # price_word.strip('￥')はそのままではダメで、price_word = price_word.strip('￥')
    price_word = price_word.strip(',') #と代入する必要がある。

    

    # find_elements ではないので一番上の本だけが取得される。
    # //*[@id="resList"]/form/div[4]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td/text()
    if workname == None :
        print('Name is nessesary.')
    if WORK_NAME in bookname_elements[item_num - 1].text :
          
        output_dict = {
            'usedOrNew' : usedOrNew,
            'workname' : bookname_elements[item_num - 1].text,
            'price' : price_word,
        }
    else :
        output_dict = {
            'usedOrNew' : 'No book',
            'workname' : 'No book',
            'price' : 'No book',
        }
    driver.quit()
    return output_dict

    

    # if WORK_NAME in work_name :    
    #     try :
    #         price_element = driver.find_element(By.XPATH,f'//*[@id="item-{item_num}"]/div/div[3]/span/span/div/div[1]')
    #     except :
    #         print('No')
    # //*[@id="item-2"]/div/div[3]/span/span/div/div[1]
    # //*[@id="item-3"]/div/div[3]/span/span/div/div[1]


    


    


    # AMAZON
    # driver.find_element(By.ID,"twotabsearchtextbox").send_keys(SEARCH_WORD)
    # driver.find_element(By.ID,'nav-search-submit-button').click()
    # element = driver.find_elements(By.CLASS_NAME,'a-declarative')
    
    
    

    
"""
btn = driver.find_element(By.ID,'nav-search-submit-button')
btn.click()

はダメで

btn = driver.find_element(By.ID,'nav-search-submit-button').click()

にする必要がある。
"""

