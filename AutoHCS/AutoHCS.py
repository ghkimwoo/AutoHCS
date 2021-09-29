#-*- coding:utf-8 -*-
import json
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver.exe') #크롬 드라이버 찾기
driver.get('https://hcs.eduro.go.kr/#/loginHome') #페이지 오픈

wait = WebDriverWait(driver, 1) #대기시간 설정

with open('setting.json', "r", encoding="utf-8") as json_file: #사용자 정보 json 오픈
    json_data = json.load(json_file)

#사용자 정보 변수화
city = json_data['city']
school_level = json_data['school_level']
school_name = json_data['school_name']
username = json_data['username']
birthday = json_data['birthday']
password = json_data['password']

driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click() #xpath로 자가진단 참여하기 버튼 클릭



driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button').click() #학교 찾기 클릭
#select box에서 지역을 선택하기 위한 설정
select = Select(driver.find_element_by_xpath('//*[@id="sidolabel"]'))
select.select_by_visible_text(city)
#select box에서 지역을 선택하기 위한 설정
select = Select(driver.find_element_by_xpath('//*[@id="crseScCode"]'))
select.select_by_visible_text(school_level)
#input로 되어 있는 학교 이름 박스에 입력
driver.find_element_by_xpath('//*[@id="orgname"]').send_keys(school_name)
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click() #검색 클릭
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a'))) #페이지 로딩 대기
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a').click() #학교 이름 클릭
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click() #확인 클릭



driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(username) #이름 입력
driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(birthday) #생년월일 6자리 입력
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click() #정보 입력 후 확인을 클릭
driver.implicitly_wait(3) #비밀번호 창 확인 대기
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
driver.find_element_by_xpath('//*[@id="password"]').click() #xpath로 자가진단 참여하기 버튼 클릭
for i in password:
    password_xpath="//a[@aria-label='{}']".format(i) #비밀번호의 aria-label을 추적
    driver.find_element_by_xpath(password_xpath).click() #추적으로 된 xpath를 클릭

driver.find_element_by_xpath('//*[@id="btnConfirm"]').click() #xpath로 자가진단 참여하기 버튼 클릭
wait = WebDriverWait(driver, 2)
driver.implicitly_wait(1)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em')))
driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em').click() #button은 정상이라고 된 온도계임.
driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click() #아니요
driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click() #아니요
driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click() #아니요
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click() #확인
driver.quit()
sys.exit(0)