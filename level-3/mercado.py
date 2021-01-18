from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument(
  "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver', chrome_options=opts)

driver.get('https://listado.mercadolibre.com.mx/repuestos-autos-camioneta-bujias')

while True:
  WebDriverWait(driver, 48).until(
    EC.presence_of_all_elements_located((By.XPATH, '//a[@class="ui-search-result__content ui-search-link"]'))
  )
  links_productos = driver.find_elements(By.XPATH, '//a[@class="ui-search-result__content ui-search-link"]')
  links_de_la_pagina = []

  for a_link in links_productos:
    links_de_la_pagina.append(a_link.get_attribute("href"))


  for link in links_de_la_pagina:
    try:
      driver.get(link)
      titulo = driver.find_element_by_xpath('//h1').text
      precio = driver.find_element(By.XPATH, '//span[@class="price-tag-fraction"]').text
      print(titulo)
      print(precio)
      driver.back()
    except Exception as e:
      print(e)
      print("Error en links")
      driver.back()
      # break

  try:
    boton_siguiente = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
    driver.execute_script("arguments[0].click();", boton_siguiente)
  except Exception as e:
    print(e)
    print('Error en boton')
    break