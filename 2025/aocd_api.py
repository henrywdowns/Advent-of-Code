from aocd import get_data,submit
import requests
import certifi
import os
import dotenv
from datetime import date

# to solve my UNC issues:

# net use Y: "\\corp.bloomberg.com\ny-dfs\users\hdowns5\VSCode\Python\Advent-of-Code"
# cd Y:

class AOCD:
    def __init__(self,day,year=None,part=None):
        self.day=day
        if year:
            self.year=year
        else:
            if date.today().month < 12: 
                self.year = date.today().year - 1
            else:
                self.year = date.today().year
        self.part=part

        self.session = os.getenv("AOCD_COOKIE")
        self.data = get_data(session=self.session, day=self.day, year=self.year)

    def sample_data(self,sample_length=100):
        try:
            print(self.data[:sample_length])
        except Exception as e:
            print(e)

    def submit_answer(self,value):
        submission = submit(value,session=self.session)
        return submission

    def set_part(self,part):
        self.part=part

    def get_list(self,delimiter):
        return [line for line in self.data.split(delimiter) if line]