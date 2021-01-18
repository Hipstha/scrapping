import requests
import pandas as pd

headers = {
  "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  'referer': 'https://www.udemy.com/courses/search/?src=ukw&q=r'
}

cursos_totales = [

]

for i in range(1, 4):
  url_api = 'https://www.udemy.com/api-2.0/search-courses/?src=ukw&q=r&skip_price=true&p='+str(i)

  response = requests.get(url_api, headers = headers)

  data = response.json()

  cursos = data["courses"]

  for curso in cursos:
    cursos_totales.append({
      "titulo": curso["title"],
      "num_reviews": curso["num_reviews"],
      "rating": curso["rating"]
    })

df = pd.DataFrame(cursos_totales)

print(df)

df.to_csv("cursos_udemy.csv")
# print(cursos)

# print(response.json())