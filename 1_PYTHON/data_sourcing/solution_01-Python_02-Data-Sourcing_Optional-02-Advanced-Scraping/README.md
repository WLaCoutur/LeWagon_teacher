If you managed to complete all the challenges of the day so far, congratulations!

Let's finish the day with a kind of **advanced scraping**. In this challenge, we'll be using a _real_ browser. You will see that this technique can be used to perform **web automation** (like submitting forms for instance!)

Some websites don't work the way HTTP & HTML were intended to work. They use a technique called **client-side rendering** where the HTML starts almost empty, and all the DOM on the page is generated thanks to JavaScript.

This means that if you use the traditional technique where you look into the HTML (`curl`-style), you won't find anything! You need the JavaScript to be fully rendered, and to do so you need a browser, like Chrome.

To drive Chrome from code, you need a pilot. We will use [**Selenium**](https://www.seleniumhq.org/). With Selenium, you can navigate to a page, scroll down, click on a link, fill in a few inputs, click on a button, etc. Anything a human can do with a browser can also be done with Selenium.

⚠️ There is no `make` on this challenge.

## Example

Imagine you want to get some information about a recipe. The URL structure is easy to understand. `251` is the id of the recipe we are looking for:

```bash
https://recipes.lewagon.com/recipes/251/advanced
```

Go to [that URL](https://recipes.lewagon.com/recipes/advanced?search[query]=carrot&page=1), disable JavaScript in your browser, and reload.

<details>
<summary markdown="span">Disable JavaScript in Chrome 🎈</summary>

1. Open Chrome DevTools by right-clicking on any element of the page and clicking on `Inspect`. Or just hit the `F12` function key.

2. Open the Command Menu by typing `Command-Shift-P` (MacOS) or `Control-Shift-P` (Windows / Linux).

3. Type 'javascript' to find the `Disable JavaScript` option.

</details>

<details>
<summary markdown="span">Disable JavaScript in Firefox 🦊</summary>

1. Open Firefox DevTools by right-clicking on any element of the page and clicking on `Inspect`. Or just hit the `F12` function key.

2. Hit `F1` to open the Settings.

3. Under `Advanced settings`, toggle the `Disable JavaScript` option.

</details>
<br>

See how the page loads indefinitely? We can't scrape with just `requests` + `BeautifulSoup` from the server-side generated HTML. We need Selenium and a browser!

## Setup

For this challenge, we will use Selenium + Chrome. If you want to try another browser (Firefox), you can do that as well but the instructions will need to be adapted.

<details>
<summary markdown='span'>⚠️ If you are working on <strong>Windows with WSL</strong> we need a couple of extra steps first</summary>

We need Google Chrome within WSL so run the commands below to install Chrome inside WSL:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install
```

</details>
<br>

In your terminal, install selenium:

```bash
pip install selenium
pip install chromedriver-binary-auto
```


OK! Now that this is done, open the `test_advanced_scraping.py` file and copy/paste the following code:

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://recipes.lewagon.com/recipes/advanced")

# driver.quit()
```

<details>
<summary markdown='span'>⚠️ Extra steps for <strong>Windows</strong> users </summary>

You unfortunately can't have a visual version of Selenium without installing Python into your Windows system but you can still use it to interact with javascript using websites headless so instead use the code below 👇

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://recipes.lewagon.com/recipes/advanced")

## To verify you are getting the html of the page you can use
## print(driver.page_source) as you go
```

</details>


Open your terminal and run:

```bash
python test_advanced_scraping.py
```

🚀 It should open a Chrome window, navigate to the page and stay like that! If you uncomment the last line `driver.quit()` then you will see that Chrome will close automatically  when the script is done. You need to do that otherwise you'll have plenty of Chrome windows open after a while!

## Searching Chocolate-Based recipes 😋

We will now simulate user interaction with the page. Something a user can do is click on the search bar and type a location. Go ahead and try it: type `chocolate`. Now click on the magnifying glass button to launch the search.

This is what we want to simulate! We will use the [`find_element_by_id`](https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id) method to locate the input which we want to search.

```python
from selenium.webdriver.common.by import By

search_input = driver.find_element(By.ID, 'TODO') # Open the inspector in Chrome and find the input id!
search_input.send_keys('chocolate')
```

With that piece of code, you should see your Chrome browser opening on the specified URL and filling the location input with `chocolate`

## Submitting the Form

The next step will be to submit the form to get the chocolate-based recipes back. To do that, we can add the following line to our code:

```python
search_input.submit()
```

Just like that, you should see the updated list of recipes.

## Retrieving the URLs of Each Recipe

As you can see, the list of updated recipes is also fetched using Javascript and we have to wait a little bit to see the results. This means we need to wait for the recipes to appear before being able to gather the recipes' URLs.

To do that we will use [**explicit wait**](https://selenium-python.readthedocs.io/waits.html):

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# [...]
wait = WebDriverWait(driver, 15)
wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='recipes']")))
```

The weird string in the method uses an [XPath](https://en.wikipedia.org/wiki/XPath) search in the DOM. It locates the `<div/>` with an `id` that has the value `recipes`. After exploration of the website's DOM, we found that this `<div/>` is the element that contains all the recipes fetched by the search.

Now that we waited for the filtered recipes to appear, it's time to collect the URL of each recipe to be able to scrape each one of them.

```python
recipe_urls = []
cards = driver.find_elements(By.XPATH, "//div[@class='recipe my-3']")
print(f"Found {len(cards)} results on the page")
for card in cards:
    url = card.get_attribute('data-href')
    url = url.replace("http://localhost", "https://recipes.lewagon.com")
    recipe_urls.append(url)

print(recipe_urls)
```

Run the code from the terminal. You should get back 12 URLs (i.e. all the recipes on the first page).

## Scraping Each Recipe

Now that we have a list of URLs, we can now navigate to each page, wait for the result to appear, and give it to BeautifulSoup to gather the data we need!

For each recipe, the following code will gather:

- the name of the recipe
- the cooking time of the recipe
- the difficulty of the recipe
- the price range of the recipe
- the description of the recipe

We start with an empty list, `recipes`, that we will populate with a `dict`, storing the desired information about each recipe:


```python
from bs4 import BeautifulSoup

# [...]

recipes = []
for url in recipe_urls:
  print(f"Navigating to {url}")
  driver.get(url)
  wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='p-3 border bg-white rounded-lg recipe-container']")))

  soup = BeautifulSoup(driver.page_source, 'html.parser')
  name = soup.find('h2').string.strip()
  cooktime = soup.find('span', class_='recipe-cooktime').text.strip()
  difficulty = soup.find('span', class_='recipe-difficulty').text.strip()
  price = soup.find('small', class_='recipe-price').attrs.get('data-price').strip()
  description = soup.find('p', class_='recipe-description').text.strip()
  recipes.append({
    'name': name,
    'cooktime': cooktime,
    'difficulty': difficulty,
    'price': price,
    'description': description
  })
```

Finally, we can save the results in a CSV file using the techniques we learned earlier in the day:

```python
import csv

# [...]

with open('data/recipes.csv', 'w') as file:
  writer = csv.DictWriter(file, fieldnames=recipes[0].keys())
  writer.writeheader()
  writer.writerows(recipes)

driver.quit()
```

## Going Headless

Launching a web scraping script with Selenium opens a Google Chrome window which gets in the way and prevents you from doing anything else (you might have seen this, interacting with the page using the mouse or keyboard while the script is running breaks it). There's a solution for that: [Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome). The idea is to use Chrome without its user interface. This is how you can do it:

Replace this line:

```python
options.add_experimental_option("detach", True)
```

With the following lines (you'll already have this one if you're on Windows):

```python
options.add_argument("--headless")
```

Add a few `print()` statements (as you won't see what's going on anymore!) and re-start:

```python
python test_advanced_scraping.py
```
