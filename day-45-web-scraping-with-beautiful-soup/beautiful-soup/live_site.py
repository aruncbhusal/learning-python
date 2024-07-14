# Next up, we'll be creating a soup from a live site
# The site is Y-combinator's hacker news page: https://news.ycombinator.com/
# For it we need to make a get request to the page and it will be extracted

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

# Our first task is to get the first headline and its points. By using Chrome inspector
# we found that the headline is an anchor element inside a class called "titleline"
# In the course, the class for the anchor is "storylink" but when I inspected, where was
# no such class, so I'll have to use my own method
# Then the score is a span with class "score"

articles= soup.select(selector= ".titleline > a")
# Here I had to use the selector with ">" to select the immediate child to the span class that
# has the title since there is also another anchor inside it, but it is inside another span
article_titles = []
article_links = []
for article in articles:
    title = article.getText()
    article_titles.append(title)
    link = article.get("href")
    article_links.append(link)

print(article_titles)
print(article_links)

article_upvotes= [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]
print(article_upvotes)

# Now the final task was to find the article with the highest number of upvotes in the page
# So we need to replace the find to find_all and select_one to select.
# In the course, both had find but since there was no class for the headline, I had no choice
# but to use the select instead
# Before that, we had to change the score values which were originally strings to numbers by first
# separating the number from the word "points" using split() then taking the number item only with [0]

                    # max_upvotes_index = 0
                    # for count in article_upvotes:
                    #     if count > article_upvotes[max_upvotes_index]:
                    #         max_upvotes_index = article_upvotes.index(count)
# We could use the above, or we can just use the max function from Python. I forgot it was a function
# and not a method of the list class, and since I didn't see it when using . I resorted to this method
max_upvotes_index = article_upvotes.index(max(article_upvotes))

print(article_titles[max_upvotes_index])
print(article_links[max_upvotes_index])
print(article_upvotes[max_upvotes_index])