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
driver.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")

# csv 파일로 변환
import csv
file = open('movie_2.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["outline", "director", "score"])

# 각 영화 클릭
time.sleep(3)
for i in range(2, 23):
    try:
        rankbtn = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div/ul/li[3]/a')
        rankbtn.click()

        time.sleep(2)
        moviebtn = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a")
        moviebtn.click()
      
        time.sleep(2)
        outline = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]").text
        director = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p/a").text
        score = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a/div/span/span").text

        print(outline, director, score)
        time.sleep(1)
    except:
        print("없음")
        outline = "."
        director="."
        score="."
    writer.writerow([outline, director, score])
file.close()
