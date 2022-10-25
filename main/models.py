from django.db import models
from pymongo import MongoClient
import secrets

# Create your models here.

coll = MongoClient()
db = coll["links"]
f_dbase = db["links_full"]
c_dbase = db["pre_links"]

def check_l(obj):
    if c_dbase.find_one({"link": str(obj)}):
        return False
    else:
        return True

def generate_links():
    sec = secrets.token_urlsafe(6)
    if check_l(sec):
        c_dbase.insert_one({"link": sec})
        return sec
    else:
        generate_links()

def m_link(i_link):
    l = f_dbase.find_one({"initial_link": i_link})
    if l != None:
        return l["short_link"]
    s_link = generate_links()
    f_dbase.insert_one({"initial_link": i_link, "short_link": s_link})
    return s_link

def r_link(link):
    r = f_dbase.find_one({"short_link": link})
    if r != None:
        return r["initial_link"]
    else:
        return False