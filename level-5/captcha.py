from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument(
  "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver', options=opts)
driver.get('https://google.com/recaptcha/api2/demo')

try:

  driver.switch_to.frame(driver.find_element_by_xpath('//iframe'))
  captcha = driver.find_element_by_xpath('//div[@class="recaptcha-checkbox-border"]')
  captcha.click()

  input()

  driver.switch_to.default_content()

  submit = driver.find_element_by_xpath('//input[@id="recaptcha-demo-submit"]')
  submit.click()
except Exception as e:
  print(e)

# yo ya estoy en la siguiente página
contenido = driver.find_element_by_class_name('recaptcha-success')
print(contenido.text)