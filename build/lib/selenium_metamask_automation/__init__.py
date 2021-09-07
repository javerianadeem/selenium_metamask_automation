from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

EXTENSION_PATH = r'C:\Users\javer\Downloads\10.0.2_0.crx'

def food():
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
    # driver.maximize_window()

    driver.set_window_size(300, 700)

    driver.get("https://daraz.pk/")
    print(driver.title)
    print("Biryani")
    driver.quit()

def launchSeleniumWebdriver(driverPath):

    chrome_options = Options()
    chrome_options.add_extension(EXTENSION_PATH)
    global driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)
    driver.maximize_window()
    print("Biryani")
    time.sleep(5)
    return "Extension has been loaded"

def metamaskSetup(recoveryPhrase, password):
    launchSeleniumWebdriver('C:\Drivers\chromedriver_win32\chromedriver.exe')
    #
    driver.get('http://google.com/')
    print("Page Title is : %s" % driver.title)

    driver.switch_to.window(driver.window_handles[0])

    driver.find_element_by_xpath('//button[text()="Get Started"]').click()
    driver.find_element_by_xpath('//button[text()="Import wallet"]').click()
    driver.find_element_by_xpath('//button[text()="No Thanks"]').click()

    time.sleep(5)

    inputs = driver.find_elements_by_xpath('//input')
    inputs[0].send_keys(recoveryPhrase)
    inputs[1].send_keys(password)
    inputs[2].send_keys(password)
    driver.find_element_by_css_selector('.first-time-flow__terms').click()
    driver.find_element_by_xpath('//button[text()="Import"]').click()

    time.sleep(5)

    driver.find_element_by_xpath('//button[text()="All Done"]').click()
    time.sleep(2)

    # closing the message popup after all done metamask screen
    driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
    time.sleep(2)
    print("wallet imported successfully")
    time.sleep(10)

    driver.quit()