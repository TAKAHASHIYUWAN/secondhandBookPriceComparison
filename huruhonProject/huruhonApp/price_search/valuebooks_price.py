from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER = './chromedriver'
VALUEBOOKS_URL = 'https://www.valuebooks.jp/'

AUTHER_NAME = ''
WORK_NAME = 'ドストエフスキーとの旅'
PUBLISHER_NAME = ''
SEARCH_WORD = AUTHER_NAME + '　' + WORK_NAME + '　' + PUBLISHER_NAME

def valuebooks_search(workname:str,authername:str=None,publishername:str=None,item_num:int=1):
    output_dict = {}
    SEARCH_WORD = workname + '　' + authername + '　' + publishername 
    options = Options()
    options.add_argument('-headless')

    driver = webdriver.Chrome(CHROMEDRIVER,chrome_options=options)
    driver.implicitly_wait(10)
    driver.get(VALUEBOOKS_URL)
    
    driver.find_element(By.ID,'search-query').send_keys(SEARCH_WORD)
    driver.find_element(By.ID,'search').click()


    crnt_url = driver.current_url
    name_div = driver.find_element(By.XPATH,f'//a[@id="item-{item_num}"]/div')
    work_name = name_div.get_attribute('aria-label')

    if WORK_NAME in work_name :        
        try :
            price_element = driver.find_element(By.XPATH,f'//*[@id="item-{item_num}"]/div/div[3]/span/span/div/div[1]')
            price_word = price_element.text.strip('円')
            output_dict = {
                 'usedOrNew' : '古本',
                 'workname' : work_name,
                 'price' : price_word,
                 'url' : crnt_url
             }
        except :
            output_dict = {
                'usedOrNew' : '新書',
                'workname' : work_name,
                'price' : None,
                'url' : crnt_url

            }
    else :
        output_dict = {
            'usedOrNew' : 'No book',
            'workname' : 'No book',
            'price' : 'No book',
            'url' : crnt_url

        }

    driver.quit()    
    return output_dict
    
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
if __name__ == '__main__' : 
    print(valuebooks_search(WORK_NAME,AUTHER_NAME,PUBLISHER_NAME))
