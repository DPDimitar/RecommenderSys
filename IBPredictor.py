import pandas as pd
from scipy import spatial
import numpy as np


class IBPredictor():

    def __init__(self, min_values=0, threshold=0):
        self.min = min_values
        self.threshold = threshold
        self.movies = pd.read_csv("/movies.dat", sep='\t')


    def similarity(self, mid1, mid2):
        df = self.data
        df1 = df[df['movieID'] == mid1]
        df2 = df[df['movieID'] == mid2]

        a = pd.merge(df1, df2, on=['userID'], how='inner')

        final = 1 - spatial.distance.cosine(list(a['rating_x']), list(a['rating_y']))
        return final

    def getUserRatingForMovie(self, uid, mid):
        df = self.data
        a = (df[(df['userID'] == uid) & (df['movieID'] == mid)]['rating']).tolist()
        return a[0]

    def predictRatingForThisMovie(self, uid, mid):

        df = self.data
        userRatedMovies = df[(df['userID'] == uid) & (df['movieID'] != mid)]
        userRatedMovies = list(userRatedMovies['movieID'])

        up = 0

        for i in range(len(userRatedMovies)):
            up = up + (self.similarity(userRatedMovies[i], mid) * self.getUserRatingForMovie(uid, userRatedMovies[i]))

        down = 0

        for i in range(len(userRatedMovies)):
            down = down + self.similarity(userRatedMovies[i], mid)

        return up/down

    def reccomend(self, uid, n=5, rec_seen=False):
        df = self.data
        movies = pd.DataFrame(df.movieID.unique())
        movies.columns = ['movieID']
        df = df[df['userID'] == uid]
        merge = pd.merge(movies, df, on='movieID', how='left')
        merge['rating'] = merge['rating'].fillna(0)
        merge['userID'] = merge['userID'].fillna(uid)

        this = merge[merge['rating'] == 0]

        a = list(this['movieID'])

        for i in range(len(a)):
            a[i] = self.predictRatingForThisMovie(78, a[i])

        hehe = list(zip(list(this['movieID']), a))

        f = pd.DataFrame(hehe, columns=['movieID', 'rating'])
        f = f.sort_values(by=['rating'], ascending=False)
        f = f.head(n)

        list1 = list(f['movieID'])
        list2 = list(f['rating'])

        return zip(list1, list2)

    def mostSimilarMovies(self, num):
        df = self.data
        movies = pd.DataFrame(df.movieID.unique())
        movies.columns = ['movieID']
        movies['key'] = 1
        merge = pd.merge(movies, movies, on='key')
        a = merge[['movieID_x', 'movieID_y']]
        a = a[a['movieID_x'] != a['movieID_y']]
        list1 = list(a['movieID_x'])
        list2 = list(a['movieID_y'])
        list3 = list()

        for i in range(len(list1)):
            list3.append(self.similarity(list1[i], list2[i]))

        new_df = pd.DataFrame({'movieID_1': list1, 'movieID_2': list2, 'similarity': list3})
        new_df = new_df.sort_values(by=['similarity'], ascending=False)
        new_df = new_df.head(num)

        return zip(list(new_df['movieID_1']), list(new_df['movieID_2']), list(new_df['similarity']))

    def similarItems(self, item, n):
        df = self.data
        movies = pd.DataFrame(df.movieID.unique())
        movies.columns = ['movieID']
        movies = movies[movies['movieID'] != item]
        movies['item'] = item

        list1 = list(movies['movieID'])
        list2 = list(movies['item'])
        list3 = list()

        for i in range(len(list1)):
            list3.append(self.similarity(list1[i], list2[i]))

        new_df = pd.DataFrame({'movieID_1': list1, 'item': list2, 'similarity': list3})
        new_df = new_df.sort_values(by=['similarity'], ascending=False)
        new_df = new_df.head(n)

        return zip(list(new_df['movieID_1']), list(new_df['similarity']))

    def movie_title(self, mid):
        df = self.movies
        df = df[['title', 'id']]
        df = (df[df['id'] == mid]['title']).tolist()
        return df[0]

    def predictForYourself(self, moviesNum=0, predictionNum = 15):
        df = self.data
        movies = pd.DataFrame(df.movieID.unique())
        movies.columns = ['movieID']

        userId = 1321
        movies_list = list()
        ratings_list = list()

        count = 0

        for index, row in movies.iterrows():
            if count < moviesNum:
                print(self.movie_title(row['movieID']))
                name = input("Do you know this movie? If yes type 'yes', else type no or click something else.")
                if (name=="yes" or name=="Yes"):
                    print('Rate This Movie:')
                    rating = input()
                    ratings_list.append(rating)
                    movies_list.append(row['movieID'])
                    count = count + 1
                else:
                    print("You do not know this movie..")



        df1 = pd.DataFrame()
        df1['movieID'] = movies_list
        df1['userID'] = userId
        df1['rating'] = ratings_list

        frames = [df, df1]

        df = pd.concat(frames)

        movies = pd.DataFrame(df.movieID.unique())
        movies.columns = ['movieID']
        df = df[df['userID'] == userId]
        merge = pd.merge(movies, df, on='movieID', how='left')
        merge['rating'] = merge['rating'].fillna(0)
        merge['userID'] = merge['userID'].fillna(userId)

        this = merge[merge['rating'] == 0]

        a = list(this['movieID'])

        for i in range(len(a)):
            a[i] = self.predictRatingForThisMovie(78, a[i])

        hehe = list(zip(list(this['movieID']), a))

        f = pd.DataFrame(hehe, columns=['movieID', 'rating'])
        f = f.sort_values(by=['rating'], ascending=False)
        f = f.head(predictionNum)

        list1 = list(f['movieID'])
        list2 = list(f['rating'])

        return zip(list1, list2)