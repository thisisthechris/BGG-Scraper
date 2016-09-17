import requests
import time
from bs4 import BeautifulSoup

category_id = 1055 # American West, Swap for what category you want
board_name = "the name goes in these quote marks"
auth_payload = {
    "access_token": "Put your token in these quote marks",
}

page_id = 1 
show_count = 1000 # You might need to increase this if there are more than 1k games in a category

# Download the list of games from BGG, and load it into memory
list_page = BeautifulSoup(
        requests.get("https://boardgamegeek.com/geekitem.php?instanceid=5&objecttype=property&objectid="+str(category_id)+"&subtype=boardgamecategory&pageid="+str(page_id)+"&sort=name&view=boardgames&modulename=linkeditems&callback=&showcount="+str(show_count)+"&filters[categoryfilter]=&filters[mechanicfilter]=&action=linkeditems&ajax=1").text,
        "html.parser"
    )

# Loop through the list of games, finding each of the URLs in the table
for game in list_page.find_all("span", {"class": "go_thumbnail"}):

    game_url = "https://boardgamegeek.com" + game.find("a").get("href")

    # Download the game page and load it into memory
    game_page = BeautifulSoup(
        requests.get(game_url).text,
        "html.parser"
    )

    # Display the game's name in the terminal so we can see what's going on
    print game_page.find("meta", {"name":"og:title"})['content']

    # Send the games's data to Pinterest
    requests.post("https://api.pinterest.com/v1/pins/", params=auth_payload, data={
        "board": board_name,
        "note": game_page.find("meta", {"name":"og:title"})['content'], # The game's name
        "link": game_page.find("meta", {"name":"og:url"})['content'], # The game's BGG Page
        "image_url": game_page.find("meta", {"name":"og:image"})['content'] # The game's boxart
    })

    time.sleep(1) # Wait for a second so we don't break any of the sites
