import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

scrollingScript = """
  document.getElementsByClassName('section-layout section-scrollbox scrollable-y scrollable-show')[0].scroll(0, 20000)
"""

opts = Options()
opts.add_argument(
  "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver', chrome_options=opts)
driver.get("https://www.google.com/maps/place/Restaurante+Amazonico/@40.4237431,-3.6873174,17z/data=!4m7!3m6!1s0xd422899dc90366b:0xce28a1dc0f39911d!8m2!3d40.4237431!4d-3.6851287!9m1!1b1")

sleep(random.uniform(4.0, 5.0))

SCROLLS = 0

while (SCROLLS != 3):
  driver.execute_script(scrollingScript)
  sleep(random.uniform(5, 6))
  SCROLLS += 1

reviews_restaurante = driver.find_elements(By.XPATH, '//div[contains(@class, "section-review-content")]')

for review in reviews_restaurante:
  userLink = review.find_element(By.XPATH, './/div[@class="section-review-title"]')
  try:
    userLink.click()
    driver.switch_to.window(driver.window_handles[1])
    boton_opiniones = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//button[@class="section-tab-bar-tab ripple-container section-tab-bar-tab-selected"]'))
    )
    boton_opiniones.click()

    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//div[@class="section-layout section-scrollbox scrollable-y scrollable-show"]'))
    )

    USER_SCROLLS = 0
    while (USER_SCROLLS != 3):
      driver.execute_script(scrollingScript)
      sleep(random.uniform(5, 6))
      USER_SCROLLS += 1

    userReviews = driver.find_elements(By.XPATH, '//div[contains(@class, "section-review-content")]')

    for userReview in userReviews:
      texto = userReview.find_element(By.XPATH, './/span[@class="section-review-text"]').text
      rating = userReview.find_element(By.XPATH, './/span[@class="section-review-stars"]').get_attribute('aria-label')

      print(texto)
      print(rating)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

  except Exception as e:
    print('Error aqui')
    print(e)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # break