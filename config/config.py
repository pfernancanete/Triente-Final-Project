import sqlalchemy as alch
from getpass import getpass
import pandas as pd
import os
import requests
import sqlalchemy as alch
import sys



connectionData=f"mysql+pymysql://root:admin@localhost/triente"
engine = alch.create_engine(connectionData)

engine.execute("""
    USE triente ;

""")



