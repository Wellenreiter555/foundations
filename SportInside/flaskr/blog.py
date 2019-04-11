from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import sqlite3

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT HEADLINE, BODYTEXT FROM SCRAPER'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            
                return resp.content
            

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'https://www.goal.com'
    response = simple_get(url)
    #print(response)
    link_list = []
    count = 0

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for a in html.find_all('a'):
            link = a.get('href')
            #print(type(link))
            if "/meldungen/" in link:
                full_link = ('https://www.goal.com' +link)
                if full_link not in link_list:
                    #print (link_list)
                    link_list.append(full_link)
                    print(count)
                    count +=1
            if count == 10:
                break
    #print (link_list)
    get_article(link_list)

def get_article(link_list):
    for url in link_list:
        response = simple_get(url)
        html = BeautifulSoup(response, 'html.parser')

        #img_link = get_img_link(html)
        content = get_content(html)
        headline = get_headline(html)
        
        #print(img_link)
        #break
        write_to_database(headline, content)


def get_headline(html):
    for h1 in html.find_all('h1'):
        header = h1.text
        return header
              
def get_content(html):
    none_sense = ("Copyright © 2019 Goal.com Alle Rechte vorbehalten. Die auf Goal.com enthalten Informationen dürfen möglicherweise nicht veröffentlicht, übertragen, neu geschrieben oder neu verteilt werden ohne die vorherige schriftliche Genehmigung von Goal.com.") 
    none_sense1 = ("Erlebe die Champions League live auf DAZN.")
    none_sense2 = ("Jetzt Gratismonat sichern!")
    paragraphs = []  
    for p in html.find_all('p'):
        paragraph = p.text
        if none_sense in paragraph:
            continue
        elif none_sense1 in paragraph:
            continue
        elif none_sense2 in paragraph:
            continue
        #print(paragraph)
        paragraphs.append(paragraph)
        joined_list=paragraph.join(paragraphs)
    #print(paragraphs)
    return joined_list

#def get_img_link(html):
#    for img in html.find_all('img'):
#        if "picture__image" in str(img):
#            return str(img)
#
#            picture = img
#            src = img.get("srcset")
#            image = src
#           return image

def write_to_database(HEADLINE, BODYTEXT):

    conn = sqlite3.connect('instance/flaskr.sqlite')
    cursor = conn.cursor()
    print("Link successfully added")

    #cursor.execute('''CREATE TABLE SCRAPER
    #     (HEADLINE           TEXT    NOT NULL,
    #      BODYTEXT           TEXT    NOT NULL)''')
#conn.execute("insert into crawled (title, body) values (?, ?);",(title, body))
    cursor.execute("INSERT INTO SCRAPER (HEADLINE,BODYTEXT) VALUES (?, ?);",(HEADLINE, BODYTEXT))
#cursor.execute("INSERT INTO SCRAPER (ID,HEADLINE,BODYTEXT) \
#      VALUES (2, 'get_headline', 'get_content')");
#cursor.execute("INSERT INTO SCRAPER (ID,HEADLINE,BODYTEXT) \
#      VALUES (3, 'get_headline', 'get_content')");
    cursor.close()
    conn.commit()


get_names()
