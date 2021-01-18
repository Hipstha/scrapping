from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument(
  "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver', options=opts)
driver.get('https://twitter.com/login')

user = ""
password = ""

input_user = driver.find_element(By.XPATH, '//main//input[@name="session[username_or_email]"]')
input_pass = driver.find_element(By.XPATH, '//main//input[@name="session[password]"]')

input_user.send_keys(user)
input_pass.send_keys(password)

boton = driver.find_element(By.XPATH, '//main//div[@data-testid="LoginForm_Login_Button"]/div[@dir="auto"]')

boton.click()

tweets = WebDriverWait(driver, 10).until(
  EC.presence_of_all_elements_located((By.XPATH, '//section//article//div[@dir="auto"]'))
)

for tweet in tweets:
  print(tweet.text)