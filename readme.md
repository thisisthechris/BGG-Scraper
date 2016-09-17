# Board Game Geek Scraper for Visual Dictonary

This script takes a category from Board Game Geek and posts the contents to Pinterest.

## You will need

* Python 2.7x 
* [Requests](http://docs.python-requests.org/en/master/) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) installed (if you don't have this installed we will later)
* [A Pinterest account registered as a developer](https://developers.pinterest.com)
* [A Pinterest access token with read public and write public permissions](https://developers.pinterest.com/tools/access_token/)
* A public pinterest board to upload content too - make a note of the URL

## Instructions

1. Download and unzip this repository
2. Open a terminal window and change to the directory with this repository. Example:
```bash
cd ~/Downloads/BGG-Scraper/
```
3. If you don't have Requests and Beautiful Soup already installed, we can do that now:
```bash
sudo pip install -r requirements.txt
```
4. Update the scraper.py script with your Pinterest access token. Look for the line:
```python
    "access_token": "Put your token in these quote marks",
```
5. Still in the script, update the category ID with the one you want to scrape. Its the number in the URL. Look for the line:
```python
category_id = 1055
```
6. Nearly there. Now you need the last part of the URL of your Pinterest board. So one of mine is: https://www.pinterest.com/thisisthechris/test/ - I just need the last bit - "thisisthechris/test". Now look for the line to update:
 ```python
board_name = "the name goes in these quote marks"
```
7. Save the file! 
8. Run it! In your terminal:
```bash
python scraper.py
```
9. Keep an eye on it initally. There will be a pause while the list of games is downloaded, then you should start seeing the names of the board games appearing. 
10. Go to your Pinterest board - the games are showing up! It's exciting!
11. Keep your computer on and go and have a cup of tea. It'll take a little while to go through all the games. 
12. Come back, check that the script reached the end of the list. You might need to tweak some of the paramters if there are more than 1k games in the category.
13. You're done. :)