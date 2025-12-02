from aocd import get_data,submit
import requests
import certifi
import os
import dotenv

class AOCD:
    def __init__(self,day,year,part=None):
        self.day=day
        self.year=year
        self.part=part

        self.session = os.getenv("AOCD_COOKIE")
        self.data = get_data(session=self.session, day=self.day, year=self.year)

    def sample_data(self,sample_length=100):
        try:
            print(self.data[:sample_length])
        except Exception as e:
            print(e)

    def submit_answer(self,value):
        submission = submit(value)
        return submission

    def set_part(self,part):
        self.part=part