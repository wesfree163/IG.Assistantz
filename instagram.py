#!/usr/bin/env Python3
# from pywinauto import Application
from time import sleep
# import json
# import os
# import autoit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from pywinauto import Application


# Variables
driver = ""


def launch_inst():
    global driver
    print("Opening instagram")

    # Chrome browser options
    mobile_emulation = {"deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    opts = webdriver.ChromeOptions()
    opts.add_argument("window-size=1,765")
    opts.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=opts)


    # Opens Instagram
    main_url = "https://www.instagram.com"
    driver.get(main_url)
    sleep(10)


def login():
    # Logs into instagram
    print("Logging into Instagram")
    driver.find_element_by_class_name("sqdOP").click()
    username = driver.find_element_by_name("username")
    username.send_keys("h")
    username.send_keys("i")
    username.send_keys("_")
    username.send_keys("i")
    username.send_keys("m")
    username.send_keys("w")
    username.send_keys("e")
    username.send_keys("s")
    sleep(3)
    password = driver.find_element_by_name("password")
    password.send_keys("Y")
    password.send_keys("o")
    password.send_keys("u")
    password.send_keys("O")
    password.send_keys("n")
    password.send_keys("l")
    password.send_keys("y")
    password.send_keys("l")
    password.send_keys("i")
    password.send_keys("v")
    password.send_keys("e")
    password.send_keys("1")
    password.send_keys("c")
    password.send_keys("e", Keys.ENTER)
    # password.send_keys(Keys.RETURN)
    sleep(3)
    # driver.find_element_by_xpath("//a[contains(text(),'Not now')]").click()

def remove_popups():
    print("Removing any popups")
    try:
        driver.find_element_by_xpath("//a[contains(text(),'Not Now')]").click()
    except:
        try:
            driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        except:
            try:
                driver.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
            except:
                pass


# def upload_file(self, filename):
#     path = os.path.join(
#         os.path.realpath('.'),
#         'fixtures',
#         filename
#     )
#     assert os.path.exists(path)

#     for i in range(10):
#         app = Application()
#         app.connect(process=self.get_pid())  # connect to browser
#         dialog = app.top_window_()           # get active top window (Open dialog)
#         if not dialog.Edit.Exists():         # check if Edit field is exists
#             sleep(1)                    # if no do again in 1 second (waiting for dialog after click)
#             continue
#         dialog.Edit.TypeKeys('"{}"'.format(path))   # put file path
#         dialog['&OpenButton'].Click()               # click Open button

#         return

#     raise Exception('"Open File" dialog not found')


def post():
    print("Posting your trials")
    sleep(2)
    driver.find_element_by_class_name("_8-yf5").click()
    sleep(7)
    remove_popups()
    sleep(3)
    # upload_file()

# def postM():
#     app = Application().connect(title_re="File Upload")
#     app.FileUpload.Edit.SetText("test.jpg")
#     sleep(1.5369)

#     app.FileUpload.Button.click()
#     app.FileUpload.Button.click()

launch_inst()
login()

remove_popups()
sleep(15)
remove_popups()
sleep(15)
remove_popups()
sleep(15)
remove_popups()
sleep(15)
remove_popups()
post()