from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/opt/homebrew/Caskroom/chromedriver/102.0.5005.61/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ptt.cc/bbs/DigiCurrency/index.html")
print(driver.title)
search = driver.find_element(By.NAME, "q")
search.clear()
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "r-ent"))
)
posts = driver.find_elements(By.CSS_SELECTOR, "div.r-ent")

for _post in posts:
    state = _post.find_element(
        By.CSS_SELECTOR, "div.nrec>span").get_attribute('class')
    if state != "hl f3":
        title = _post.find_element(By.CSS_SELECTOR, "div.title>a")
        text = title.text
        url = title.get_attribute('href')
        print(text, url)

# for _title in titles:
#     link = driver.find_element_by_link_text(_title.text)
#     link.click()
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main-content"))
#     )
#     driver.back()
driver.quit()
