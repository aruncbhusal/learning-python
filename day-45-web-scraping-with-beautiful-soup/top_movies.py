# The final project for today is to scrape a webpage for the top 100 movies of all time:
# https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/
# The first task here is to create a text file with the top 100 movies in order from 1
# Notice that the website lists in the order from 100 to 1.

import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# Since the actual website was archived by web.archive.org, I used the actual website instead
# Well, the main website had removed the ) that separated the movie number from the title, so since that is
# something I'll probably have to use, I'll stick with the archived site maybe

soup = BeautifulSoup(response.text, "html.parser")
# Apparently I was specifying the parser in the get() function instead of this one. My bad
# The name of the movies seem to be in a h3 element with a class "title" so let me try that first
all_movies = soup.find_all("h3", class_ = "title")

            # for movie in all_movies:
            #     print(movie.getText().split(")"))
# As shown in the course, there was nothing changed while placing the movies in the file so I'll
# just write all the text into a new text file rather than separating the movie index and name
with open("day-45-web-scraping-with-beautiful-soup/movies.txt", "w", encoding="utf-8") as file:
    for movie in all_movies[::-1]:
        # We need to reverse the order so I'll just loop through the reversed list. That should work
        file.write(f"{movie.getText()}\n")
# And yet again, I had to set the encoding to utf-8 else it would give me the same decode error