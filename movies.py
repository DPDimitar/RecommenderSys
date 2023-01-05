import pickle
import time
import datetime
import pytz
import pandas as pd


class MovieData:
    def __init__(self, thepath):
        self.path = thepath
        self.data = pd.read_csv(self.path, sep='\t')


    def get_title(self,mid):
        df = self.data
        df = df[['title', 'id']]
        df = (df[df['id'] == mid]['title']).tolist()
        return df[0]




