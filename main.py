import pandas as pd
import requests
import urllib.request

from pokemon import Pokemon


# request
url = "https://pokemondb.net/pokedex/all"
request = requests.get(url, auth=('user', 'pass'))
html = request.text.lower()

# data parsing
pokemons_list = []
last = 0
for entry in range(2, 1000):
  num = html.split("<tr>")[entry].split('data">')[1].split('</span>')[0]

  if num == last:
    continue

  # ID  / Name  / Type1 / Type2 / Total / HP  / Attack  / Defense / Sp.Attack / Sp.Defense  / Speed / Sprite  / URL
  id = html.split("<tr>")[entry].split('data">')[1].split('</span>')[0]
  name = html.split("<tr>")[entry].split('">')[6].split("</a>")[0]
  type1 = html.split("<tr>")[entry].split('href="/type/')[1].split('">')[1].split('</a>')[0]
  try:
    type2 =   html.split("<tr>")[entry].split('href="/type/')[2].split('">')[1].split('</a>')[0]
  except:
    type2 =   None
  total =     html.split("<tr>")[entry].split('<td class="cell-total">')[1].split('</td>')[0]
  hp =        html.split("<tr>")[entry].split('<td class="cell-num">')[1].split('</td>')[0]
  attack =    html.split("<tr>")[entry].split('<td class="cell-num">')[2].split('</td>')[0]
  defense =   html.split("<tr>")[entry].split('<td class="cell-num">')[3].split('</td>')[0]
  spAttack =  html.split("<tr>")[entry].split('<td class="cell-num">')[4].split('</td>')[0]
  spDefense = html.split("<tr>")[entry].split('<td class="cell-num">')[5].split('</td>')[0]
  speed =     html.split("<tr>")[entry].split('<td class="cell-num">')[6].split('</td>')[0]
  sprite =    html.split("<tr>")[entry].split('data-src="')[1].split('"')[0]
  pkmnURL =   html.split("<tr>")[entry].split('<a class="ent-name" href="/pokedex/')[1].split('"')[0]

  type_ = type1
  if type2:
      type_ += " " + type2

  pokemons_list.append(Pokemon(id, name, type_, total, hp, attack, defense,
                    spAttack, spDefense, speed, sprite))

df = pd.DataFrame(pokemons_list)
df.to_csv('data.csv', index=False)
print("finished sucessfully!")
