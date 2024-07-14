# In this lesson, we're learning about a module called Beautiful Soup
# which is a HTML/XML parser. We can parse a webpage and extract information
# from it without having to rely on any APIs, some websites might offer very
# limited APIs or some may offer no API at all. In suuch cases we apply scraping
# Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# First off, there's a file in this folder called website.html which we will first
# try to scrape. To do that, we'll first import the html file here.

# The BeautifulSoup class is in the bs4 module which is essentially v4 for BS
from bs4 import BeautifulSoup

with open("day-45-web-scraping-with-beautiful-soup/beautiful-soup/website.html", encoding= "utf-8") as site:
    contents = site.read()
    # On just using this I had an UnicodeDecodeError probably due to the heart emoji
    # Let's see if the error repeats after parsing, else I'll have to search for a fix
    # This error doesn't appear in the course using the same code though
    # As I suspected, the heart emoji is the culprit, and removing it from the HTML fixes
    # the issue. I was suggested to add "encoding = "utf-8" " to the open() function and
    # it worked, I guess, for the most part. I'll have to make do with that

# To make a soup out of the text we have extracted from the file, we create a new BeautifulSoup
# object by passing in the "markup" i.e. the file containing the text for the site, and a parser
# For html we can use python's html.parser but for some sites, we might have to use lxml instead
# We'd need to import lxml for that, but for html parser we don't need to do that
soup = BeautifulSoup(contents, "html.parser")

# Now we can print the different componenets of the webpage by using the soup object. If we print
# the object itself, it will give the entire page, and we can use .prettify() to indent the stuff
# We can also use the name of a tag to return the first element with that tag. It will give the
# entire element i.e. starting/ending tags and the content. So we can use .name() or .string() to
# print the name of the tag or the content inside it.
                # print(soup.prettify())
print(soup.title.string)
# Apparently, using "string" and "text" gives the same outcome. Interesting.

# Now this only gives us the first element that matches our query, and we have no way of getting a
# class or id this way, so to get all the elements that match our requirement, we use:
all_anchors = soup.find_all(name="a")
                # print(all_anchors)
# This returns a list of all the items that have the specified name. To select individual ones,
for anchor in all_anchors:
    print(anchor.getText())
    # We can use this to get the text within the tags we have extracted. We can also use vanilla get
                    # print(anchor.get("href"))
    # This can be used to get the specific attributes of the element

# Now we can instead of using name, also use id or class, but since class is a reserved word in
# Python, we use class_ instead
name = soup.find(id= "name")
print(name)
# While specifying id or class, we can also specify name to further confirm our required item
heading = soup.find_all("h3", class_ = "heading")
print(heading)

# Instead of finding them like this, we can drill down even further, since there can be non essential
# data that might get mixed up with what we need, so we can instead use CSS selectors to get items

print(soup.select_one("#name"))
# The attribute passed is the selector in the way we'd use in CSS
print(soup.select("p a"))
# This lets us select an anchor tag that is bundled inside a paragraph tag. The result is a list with 1 item