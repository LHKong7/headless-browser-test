# from selenium import webdriver
# print(1)
# options = webdriver.ChromeOptions()

# prefs={"download.default_directory": "/Users/linghankong/Desktop/pythonProject/headless-browser-test/download"}
# options.add_experimental_option("prefs", prefs)

# # driver=webdriver.Chrome(executable_path='./chromedriver',chrome_options=options)
# driver = webdriver.Chrome(options=options)

# try:
#     print(1)
#     driver.get('www.google.com')
#     downloadcsv=driver.find_element_by_id('downloadPNG')
#     print(2)
#     # gotit=driver.find_element_by_id('accept-cookie-notification')
#     # gotit.click()
#     downloadcsv.click()
#     time.sleep(5)
#     driver.close()
# except:
#     print("Invalid URL")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service = webdriver.ChromeService()
# driver = webdriver.Chrome(service=Service('/Users/linghankong/Desktop/pythonProject/headless-browser-test/chromedriver'))
options = webdriver.ChromeOptions()
# options.binary_location = '/Users/linghankong/Desktop/pythonProject/headless-browser-test/chromedriver'
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service('/Users/linghankong/Desktop/pythonProject/headless-browser-test/chromedriver'), options=options)


driver.get("http://selenium.dev")

# driver.quit()