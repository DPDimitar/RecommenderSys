import random
import pandas as pd


class Recommender:
    def __init__(self, X):
        self.predictor = X
        self.movies = pd.read_csv("/movies.dat", sep='\t')

    def fit(self, UserItemData):
        UserItemData.readData()
        self.data = UserItemData.data
        self.predictor.data = UserItemData.data


    def recommend(self, uid, n = 5, rec_seen = True):

        our_predictor = self.predictor

        if rec_seen == True:

            df = self.data
            df = df[['userID', 'movieID']]
            df = df[df['userID'] == uid]
            df_len = len(df)
            l1 = list(range(0, df_len))

            for i in l1:
                l1[i] = (random.randint(our_predictor.min_rate, our_predictor.max_rate))

            df['rating'] = l1

            df = df[df['rating'] == 5]

            df = df.head(n)

            list1 = list(df['movieID'])
            list2 = list(df['rating'])

            return zip(list1, list2)

        else:

            movies = self.movies
            movies = movies[['id']]
            movies.columns = ['movieID']
            df = self.data
            df = df[df['userID'] == uid]
            df = df[["movieID"]]
            list_one = list(df['movieID'])
            list_two = list(movies['movieID'])
            final_list = list(set(list_one) - set(list_two)) + list(set(list_two) - set(list_one))
            df_len = len(final_list)
            final_list2 = list(range(0, df_len))

            for i in final_list2:
                final_list2[i] = (random.randint(our_predictor.min_rate, our_predictor.max_rate))


            data_tuples = list(zip(final_list, final_list2))
            df_new = pd.DataFrame(data_tuples, columns=['movieID', 'rating'])

            df_new = df_new[df_new['rating'] == 5].head(n)

            list1 = list(df_new['movieID'])
            list2 = list(df_new['rating'])

            return zip(list1, list2)






