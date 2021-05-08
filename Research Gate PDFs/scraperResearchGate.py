from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



# INITIALIZING VARIABLES
DRIVER_PATH = '<exact path to your chrome webdriver>'
DOWNLOADS_PATH = '<exact directory to ResearchGate Downloads>'
TIME = 15
KEY = 'cli'



# CREATIGN WEB DRIVER
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{
    "plugins.always_open_pdf_externally": True,
    "download.default_directory": DOWNLOADS_PATH
})
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chromeOptions)
driver.get('https://www.researchgate.net/search')




# WAITING FOR THE PAGE TO LOAD
time.sleep(TIME)




# AFTER THE PAGE IS LOADED
print("Page loaded")


# FINDING TEXT BOX AND WRITING THE CODE WORD TO FIND
searchTextbox = driver.find_elements_by_class_name('search-form__input')[0]
searchTextbox.send_keys(KEY + '\n')


# EXTRACTING URLs from the page
researchMaterials = driver.find_elements_by_class_name('nova-v-publication-item__title')
materialURLs = []
for material in researchMaterials:
    material = material.find_element_by_tag_name('a').get_attribute('href')
    materialURLs.append(material)
print(materialURLs)



# DOWNLOADING FROM INDIVIDUAL URL
for url in materialURLs:
    driver.get(url)
    time.sleep(TIME)
    download_pdf_btn = driver.find_elements_by_class_name('js-lite-click')[2]
    if download_pdf_btn:
        download_pdf_link = download_pdf_btn.get_attribute('href')
        print(download_pdf_link)
        if download_pdf_link:
            driver.get(download_pdf_link)
        else:
            print('downloadable link NA')
            
    else:
        print('PDF btn in the url number ', url.index(), ' does not exist.')


driver.quit()