# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from read import UserItemData
from movies import MovieData
from predictor import RandomPredictor
from recommendation import Recommender
from IBPredictor import IBPredictor
from average import AveragePredictor
from viewsPredictor import ViewsPredictor

if __name__ == '__main__':


##  TASK 1

    the_data = UserItemData("/user_ratedmovies.dat")

    the_data.readData()
    print(the_data.nRatings())


    the_data2 = UserItemData("/user_ratedmovies.dat",fromm = '12.1.2007', to='16.2.2008', minr=100)

    the_data2.readData()
    print(the_data2.nRatings())


##  TASK 2

    md = MovieData("/movies.dat")
    print(md.get_title(1))


##  TASK 3

    md = MovieData("/movies.dat")
    uim = UserItemData("/user_ratedmovies.dat")

    rp = RandomPredictor(1, 5)
    rp.fit(uim)
    pred = rp.predict(78)
    print(type(pred))
    items = [1, 3, 20, 50, 100]
    for item in items:
       print("Movie: {}, score: {}".format(md.get_title(item), pred[item]))


##  TASK 4

    md = MovieData('/movies.dat')
    uim = UserItemData('/user_ratedmovies.dat')
    rp = RandomPredictor(1, 5)
    rec = Recommender(rp)
    rec.fit(uim)
    rec_items = rec.recommend(78, n=5, rec_seen=False)
    for id_movie, val in rec_items:
       print("Movie: {}, score: {}".format(md.get_title(id_movie), val))


##  TASK 5

## WHAT IS THE MEANING OF 'g_avg is the average of all movies'  ??? !

    md = MovieData('/movies.dat')
    uim = UserItemData('/user_ratedmovies.dat')
    rp = AveragePredictor(100)
    rp.fit(uim)
    pred = rp.predict(78, 5)
    for idmovie, val in pred:
       print("Movie: {}, score: {}".format(md.get_title(idmovie), val))

## TASK ^6

    md = MovieData('/movies.dat')
    uim = UserItemData('/user_ratedmovies.dat')
    rp = ViewsPredictor()
    rp.fit()
    pred = rp.predict(78, 5)
    for idmovie, val in pred:
       print("Movie: {}, score: {}".format(md.get_title(idmovie), val))

## For all tasks below

    md = MovieData('/movies.dat')
    uim = UserItemData('/user_ratedmovies.dat', minr=1000)
    rp = IBPredictor()
    rec = Recommender(rp)
    rec.fit(uim)

##  TASK &&7

    print("Similarity between the movies 'Men in black'(1580) and 'Ghostbusters'(2716): ", rp.similarity(1580, 2716))
    print("Similarity between the movies 'Men in black'(1580) and 'Schindler's List'(527): ", rp.similarity(1580, 527))
    print("Similarity between the movies 'Men in black'(1580) and 'Independence day'(780): ", rp.similarity(1580, 780))

    print("Predictions for 78: ")
    rec_items = rp.reccomend(78, n=15, rec_seen=False)
    for idmovie, val in rec_items:
       print("Movie: {}, score: {}".format(md.get_title(idmovie), val))



## TASK 8 Most similar movies (+)

    print("Most similar movies: ")
    similarMovie = rp.mostSimilarMovies(20)
    for idmovie, idmovie2, val in similarMovie:
       print("Movie1: {}, Movie2: {}, similarity: {}".format(md.get_title(idmovie), md.get_title(idmovie2), val))

## TASK 9 Recommendation based on the currently viewed content

    rec_items = rp.similarItems(4993, 10)
    print('Movies similar to "The Lord of the Rings: The Fellowship of the Ring": ')
    for idmovie, val in rec_items:
       print("Movie: {}, score: {}".format(md.get_title(idmovie), val))



## TASK 10 Recommendation for yourself

    results = rp.predictForYourself(20, 15)
    print("Prediction for you:")
    for idmovie, val in results:
        print("Movie: {}, score: {}".format(md.get_title(idmovie), val));