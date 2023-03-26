import sqlite3
import os

class Transaction:
    filename=""
    def __init__(self,filename):
        self.filename