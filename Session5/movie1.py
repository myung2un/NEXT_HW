from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains

#디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'chromedriver'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (네이버 영화)
driver.get("https://movie.naver.com/index.html")

# 영화랭킹 버튼 클릭
rankbtn = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div/ul/li[3]/a')
rankbtn.click()

# 1위부터 20위까지 가져오기
# time.sleep(2)
# for i in range(2, 12):
#    t = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a").text
#    print(t)

# time.sleep(3)
# for i in range(13, 23):
#    t = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a").text
#    print(t)

# csv 파일로 변환
import csv
file = open('movie1.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["rank", "title"])

time.sleep(3)
for i in range(2, 12):
    rank = i-1
    title = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a").text
    time.sleep(0.5)
    print("1-10위",rank,title)
    writer.writerow([rank, title])
for i in range(13, 23):
    rank = i-2
    title = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a").text
    time.sleep(0.5)
    print("11-20위",rank,title)

    # print(rank, title)
    writer.writerow([rank, title])
file.close()