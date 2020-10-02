import pandas as pd
import requests
import urllib.request
from IPython.display import Image, display


url = "https://pokemondb.net/pokedex/all"

request = requests.get(url, auth=('user', 'pass'))

start = 1
finish = 151
html = request.text

last = 0
  # Headers
data = {"#":[],
        'Name':[],
        'Type1':[],
        'Type2':[],
        'Total':[],
        'HP':[],
        'Attack':[],
        'Defense':[],
        'Sp.Attack':[],
        'Sp.Defence':[],
        'Speed':[],
        'Sprite':[],
        'URL':[]}

for entry in range(start+1, 1000):
  num = html.split("<tr>")[entry].split('data">')[1].split('</span>')[0]

  if num == last:
    continue

  # Appending:
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

  data['#'].append(id)
  data['Name'].append(name)
  data['Type1'].append(type1)
  data['Type2'].append(type2)
  data['Total'].append(total)
  data['HP'].append(hp)
  data['Attack'].append(attack)
  data['Defense'].append(defense)
  data['Sp.Attack'].append(spAttack)
  data['Sp.Defence'].append(spDefense)
  data['Speed'].append(speed)
  data['Sprite'].append(sprite)
  data['URL'].append(pkmnURL)


df = pd.DataFrame.from_dict(data)
df.to_csv('pokemon.csv')

print("!")
