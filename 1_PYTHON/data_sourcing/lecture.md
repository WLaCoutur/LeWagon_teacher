Data Sourcing
Finding Data
I can export it from a software (CSV)
I know it exists somewhere in a database (SQL)
It's on this website I visit daily (Scraping)
I have found a service (API) that gives access to it
...
Plan
Reading/Writing CSV (the hard way)
Consuming an API
Scraping a website
Next lectures
Databases & SQL
CSV
A comma-separated values file is a delimited text file that uses a comma to separate values. A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record. Each record consists of one or more fields, separated by commas.
Source: Wikipedia
Example
👉 On https://people.sc.fsu.edu/~jburkardt, let's look at the addresses.csv
%%bash
mkdir -p data
curl -s https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv > data/addresses.csv
cat data/addresses.csv
John,Doe,120 jefferson st.,Riverside, NJ, 08075
Jack,McGinnis,220 hobo Av.,Phila, PA,09119
"John ""Da Man""",Repici,120 Jefferson St.,Riverside, NJ,08075
Stephen,Tyler,"7452 Terrace ""At the Plaza"" road",SomeTown,SD, 91234
,Blankman,,SomeTown, SD, 00298
"Joan ""the bone"", Anne",Jet,"9th, at Terrace plc",Desert City,CO,00123
CSV Reading
import csv

with open('data/addresses.csv') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        # row is a `list`
        print(row)
['John', 'Doe', '120 jefferson st.', 'Riverside', 'NJ', '08075']
['Jack', 'McGinnis', '220 hobo Av.', 'Phila', 'PA', '09119']
['John "Da Man"', 'Repici', '120 Jefferson St.', 'Riverside', 'NJ', '08075']
['Stephen', 'Tyler', '7452 Terrace "At the Plaza" road', 'SomeTown', 'SD', '91234']
['', 'Blankman', '', 'SomeTown', 'SD', '00298']
['Joan "the bone", Anne', 'Jet', '9th, at Terrace plc', 'Desert City', 'CO', '00123']
CSV with Headers
%%bash
curl -s https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv > data/biostats.csv
head -n 3 data/biostats.csv
"Name",     "Sex", "Age", "Height (in)", "Weight (lbs)"
"Alex",       "M",   41,       74,      170
"Bert",       "M",   42,       68,      166
CSV with Headers
import csv

with open('data/biostats.csv') as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    for row in reader:
         # row is a dict
        print(row['Name'], row['Sex'], int(row['Age']))
Alex M 41
Bert M 42
Carl M 32
Dave M 39
Elly F 30
Fran F 33
Gwen F 26
Hank M 30
Ivan M 53
Jake M 32
Kate F 47
Luke M 34
Myra F 23
Neil M 36
Omar M 38
Page F 31
Quin M 29
Ruth F 28
Writing a CSV
beatles = [
    { 'first_name': 'John', 'last_name': 'lennon', 'instrument': 'guitar'},
    { 'first_name': 'Ringo', 'last_name': 'Starr', 'instrument': 'drums'}
]
import csv

with open('data/beatles.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=beatles[0].keys())
    writer.writeheader()
    for beatle in beatles:
          writer.writerow(beatle)
%%bash
cat data/beatles.csv
first_name,last_name,instrument
John,lennon,guitar
Ringo,Starr,drums
API
An application programming interface (API) is an interface or communication protocol between a client and a server intended to simplify the building of client-side software. It has been described as a “contract” between the client and the server.
Source Wikipedia
HTTP
A client-server protocol based on a request/response cycle.
Modern Web API
RESTful (GET, POST, etc.)
Returns JSON
👉 Examples
Requests: HTTP for Humans™
👉 Documentation
Basic request
import requests

url = 'https://api.github.com/users/ssaunier'
response = requests.get(url).json()

print(response['name'])
Sébastien Saunier
Example
Let's use the Open Library Books API.
This API documentation is not that good - let's decipher it together!
Query Parameters:
Provide an ISBN (bibkeys)
Options:
format=json
jscmd=data
Livecode: Let's find the book title behind ISBN 9780747532699
import requests

isbn = '0-7475-3269-9'
key = f'ISBN:{isbn}'

response = requests.get(
    'https://openlibrary.org/api/books',
    params={'bibkeys': key, 'format':'json', 'jscmd':'data'},
).json()

print(response[key]['title'])
Harry Potter and the Philosopher's Stone
Web Scraping
HTTP (again)
This time, we'll have to deal with HTML (~unstructured data)
HTTP website example

What does that HTML look like?
Right click -> Inspect Element on any website
Typically has a tree-like structure

HTML Vocabulary

BeautifulSoup
The Python package to browse HTML (and XML!)
👉 Documentation
Typical Web Scraper with BeautifulSoup

import requests
from bs4 import BeautifulSoup

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# You now can query the `soup` object!
soup.title.string
soup.find('h1')
soup.find_all('a')
# etc...
Searching by element name

<p>A paragraph</p>

<article>An article...</article>
<article>Another...</article>
paragraph = soup.find("p")
articles = soup.find_all("article")
Searching by id

<a href="https://www.lewagon.com" id="wagon">Le Wagon</a>
item = soup.find(id="wagon")
Searching by CSS Class

<ul>
  <li class="pizza">Margharita</li>
  <li class="pizza">Calzone</li>
  <li class="pizza">Romana</li>
  <li class="dessert">Tiramisu</li>
</ul>
items = soup.find_all("li", class_="pizza")
Live-code
Let's scrape IMDb Top 50 and extract the following information for each movie:
Title
Duration
Let's build a list (movies) of dict ({ 'title': ?, 'duration': ? })
💡 Hint: IMDB requires the headers Accept-Language (to prevent auto-translation based on your IP address) and User-Agent (not to reject your scraping attempts).
Solution
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept-Language":"en-US"
}
response = requests.get("https://www.imdb.com/list/ls055386972/", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

movies = []
for movie in soup.find_all("li", class_="ipc-metadata-list-summary-item"):
    title = movie.find("h3", class_="ipc-title__text").text.split(". ")[1]
    duration = movie.find("div", class_="dli-title-metadata").find_all('span')[1].text
    movies.append({"title": title, "duration": duration})

print(movies[0:2])
[{'title': 'The Godfather', 'duration': '2h 55m'}, {'title': "Schindler's List", 'duration': '3h 15m'}]
Bonus
image.png
Then convert cURL command to Python Requests
Your turn!
There are 3 challenges for this lecture:
Reading and writing CSVs (the hard way!)
Making API calls with Python
Scraping a website
(Optional) Scraping a JavaScript client-side rendered website