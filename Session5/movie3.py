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

# 본인이 좋아하는 영화 검색
search = driver.find_element(By.XPATH, '//*[@id="search_placeholder"]' )
ActionChains(driver).send_keys_to_element(search, '위대한 쇼맨' ).perform()
btn = driver.find_element(By.XPATH, '//*[@id="jSearchArea"]/div/button' )
ActionChains(driver).click(btn).perform()

# 제목, 감독, 평점, 리뷰 개수
time.sleep(3)
fav_title = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li/dl/dt/a/strong').text
fav_director = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li/dl/dd[3]/a[1]').text
fav_score = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li/dl/dd[1]/em[1]').text
fav_review = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li/dl/dd[1]/em[2]').text
print(fav_title, fav_director, fav_score, fav_review)