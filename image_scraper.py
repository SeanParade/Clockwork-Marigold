#!/usr/bin/env python3
import bs4 as bs
import requests
from sys import argv

__args = '+'.join(argv[1:])  # Skip script name at argv[0]. Returns "" if no args

def get_images(category):
  images = []
  
  if __args is not "":
    category_choice = __args
  else:
    category_choice = category.replace(" ", "+")  # Use function passed args

  session = requests.session()
  search = session.get('http://www.tumblr.com/search/' + category_choice)
  soup = bs.BeautifulSoup(search.content, "lxml")

  for image in soup.find_all('img'):
    src_url = image['src']
    rules = [ 'media.tumblr.com' in src_url,
              'avatar' not in src_url,
              'inline' not in src_url,]
    if all(rules):
      images.append(src_url)
      print(src_url)
  
  return images

get_images("computer")
