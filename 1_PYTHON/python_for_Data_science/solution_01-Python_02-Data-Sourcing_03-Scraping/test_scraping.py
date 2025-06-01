# pylint: disable=missing-docstring, invalid-name

# TODO: paste the code from Kitt's instructions
# $DELETE_BEGIN
from bs4 import BeautifulSoup

with open("pages/carrot.html", encoding='utf-8') as recipe_file:
    soup = BeautifulSoup(recipe_file, "html.parser")

for recipe in soup.find_all('p', {'class': 'recipe-name'}):
    print(recipe.text)
# $DELETE_END
