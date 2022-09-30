from os import read
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import ctypes
import csv
import sys
import time as t

# ====================================================================================================

srcPath = (__file__)
srcPath = srcPath.replace("\\", "/")
srcPath = srcPath.replace("Bandoku.py", "")

# ====================================================================================================

userData = list()

try : 
    f = open(str(srcPath)+"User.csv",'r',encoding='utf-8-sig')
except :
    ctypes.windll.user32.MessageBoxW(0, "데이터를 불러올 수 없습니다.\nUser.csv에 사용자 정보가 있는지 확인해 주세요.", "Bandoku│실패", 16)
    sys.exit()
else :
    readCSV = csv.reader(f)
    for row in readCSV :
        userData.append(row[0])
        userData.append(row[1])
    f.close
    ctypes.windll.user32.MessageBoxW(0, "새글 피드에서 특정 그룹만 처리됩니다.\n이 프로그램과 관련없는 피드가 올라오지 않도록 설정해 주세요.\n또한, 모든기능이 정상적으로 동작하지 않을 수 있습니다.", "Bandoku│주의", 48)

# ====================================================================================================

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("headless")
driver = webdriver.Chrome(str(srcPath) + "driver/chromedriver.exe", options=options)
driver.get('https://band.us/feed')

# ====================================================================================================

driver.implicitly_wait(5)
driver.find_element_by_id('email_login_a').click()
driver.find_element_by_id('input_email').send_keys(''.join(userData[0]))
driver.find_element_by_xpath('//*[@id="email_login_form"]/button').click()
driver.find_element_by_id('pw').send_keys(''.join(userData[1]))
driver.find_element_by_xpath('//*[@id="email_password_login_form"]/button').click()
driver.find_element_by_xpath('//*[@id="content"]/p[3]/a').click()

readAuth = driver.find_element_by_xpath('//*[@id="hintNumberDiv"]')
textAuth = readAuth.text

ctypes.windll.user32.MessageBoxW(0, "앱에서 2차인증을 완료해 주세요.\n인증번호는 " + str(textAuth) + " 입니다.\n인증 후 확인을 눌러주세요.", "Bandoku│2차인증", 64)
driver.implicitly_wait(5)

ctypes.windll.user32.MessageBoxW(0, "로그인이 완료되었습니다.\n이후의 작업은 백그라운드로 실행됩니다.", "Bandoku│로그인 완료", 64)
driver.implicitly_wait(10)

# ====================================================================================================

while True :
    try :
        newFeed =  driver.find_element_by_xpath('//*[@id="content"]/div/button[2]')
        checkFeed = newFeed.get_attribute('style')

        if checkFeed == "display: none;" :
            print(".")

        else :
            try :
                print("피드를 발견했습니다.")

                driver.find_element_by_xpath('//*[@id="content"]/div/button[2]').click()

                t.sleep(1)
                driver.find_element_by_class_name('feedRecommendWrap').click()

                t.sleep(1)
                element = driver.find_element_by_class_name("etc").click()
                driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/button[4]').click()
                print("작업을 완료했습니다.")

            except :
                ctypes.windll.user32.MessageBoxW(0, "피드를 정상적으로 불러올 수 없습니다.\n프로그램을 재시작해 주세요.", "Bandoku│오류", 16)
                driver.quit()
                sys.quit()
        
        t.sleep(5)

    except :
        ctypes.windll.user32.MessageBoxW(0, "예상치 못한 오류가 발생했습니다.\n프로그램을 재시작해 주세요.", "Bandoku│오류", 16)
        driver.quit()
        sys.quit()