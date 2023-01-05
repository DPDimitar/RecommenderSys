import random
import pandas as pd

class AveragePredictor:
    def __init__(self, b = 0):
        self.b = b



    def predict(self, uid, numberOfMovies):
        self.user_id = uid
        asc = self.model
        asc = asc.head(numberOfMovies)
        list1 = list(asc['movieID'])
        list2 = list(asc['average'])

        return zip(list1, list2)

    def fit(self, UserItemData):
        userData = pd.read_csv(UserItemData.path,sep='\t')
        movies1 = pd.read_csv("/movies.dat", sep='\t')
        userData = userData[['movieID', 'rating']]
        movies = movies1[['id']]
        movies.columns = ['movieID']

        this = pd.merge(movies, userData, on='movieID', how='left')

        vs = this[['movieID', 'rating']].groupby(['movieID']).sum()
        vs.columns = ['sum']

        n = this[['movieID', 'rating']].groupby(['movieID']).count()
        n.columns = ['count']

        g_avg = list(userData['rating'])
        g_avg = sum(g_avg) / len(g_avg)

        vs['count'] = n

        result = vs

        result['average'] = (result['sum'] + self.b * g_avg)/(result['count']+self.b)

        result['average'] = result[['average']].fillna(0)

        result = result[['average']]

        list1 = list(result['average'])

        final = pd.DataFrame(list1)
        final.columns = ['average']
        final['movieID'] = movies['movieID']

        final = final.sort_values(by = 'average',ascending = False)

        self.model = final
