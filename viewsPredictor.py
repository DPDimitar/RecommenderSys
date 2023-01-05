import random
import pandas as pd

class ViewsPredictor:
    def __init__(self):
        self.data = pd.read_csv("/user_ratedmovies.dat", sep='\t')


    def predict(self, uid, numberOfMovies):
        asc = self.model
        asc = asc.head(numberOfMovies)
        list1 = list(asc['movieID'])
        list2 = list(asc['userID'])

        return zip(list1, list2)

    def fit(self):
        df = self.data
        df = df[['userID', 'movieID']]
        n = df[['userID', 'movieID']].groupby(['movieID'], as_index=False).count()
        n = n.sort_values(by='userID', ascending=False)
        self.model = n


