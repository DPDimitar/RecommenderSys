import random
import pandas as pd

class RandomPredictor:
    def __init__(self, minimum_rating, maximum_rating):
        self.min_rate = minimum_rating
        self.max_rate = maximum_rating
        self.movies = pd.read_csv("/movies.dat", sep='\t')


    def predict(self, uid):
        self.user_id = uid
        db = self.data
        myUserData = db[db['userID'] == uid]
        myUserData = myUserData[['userID', 'movieID', 'rating']]
        myUserData.dropna(inplace=True)
        myMoviesData = self.movies
        myMoviesData = myMoviesData[['id']]
        myMoviesData.columns = ['movieID']
        this = pd.merge(myMoviesData, myUserData, on='movieID', how='left')
        this = pd.DataFrame(this)

        this['rating'] = this['rating'].fillna(0)
        this = this[['rating']]

        l1 = this['rating'].tolist()

        for i, item in enumerate(l1):
            l1[i] = int(item)
            if l1[i]==0:
                l1[i] = random.randint(self.min_rate, self.max_rate)

        keys = list(range(1,len(l1)))
        dictionary = dict(zip(keys, l1))

        return dictionary


    def fit(self, UserItemData):
        UserItemData.readData()
        self.data = UserItemData.data




