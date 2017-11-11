#!/usr/bin/env python3
from sys import argv
import bs4 as bs
import requests


def get_images():
  category_choice = ""
  argv.reverse()
  arg_qty = len(argv) - 2
  
  if arg_qty < 1:
    category_choice = "computer" # default category
  else:
    while arg_qty >= 0:
      category_choice += argv[arg_qty] + "+"
      arg_qty = arg_qty - 1
  
  session = requests.session()
  search = session.get('http://www.tumblr.com/search/' + category_choice[:-1])
  soup = bs.BeautifulSoup(search.content, "lxml")
  images = []

  for image in soup.find_all('img'):
    src_url = image['src']

    rules = [ 'media.tumblr.com' in src_url,
              'avatar' not in src_url,
              'inline' not in src_url,]

    if all(rules):
      images.append(src_url)
      print(src_url)
  
  return images


scraped_images = get_images()

