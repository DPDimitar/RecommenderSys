import datetime
import pandas as pd


class UserItemData:
    def __init__(self, thepath, fromm=None, to=None, minr=0):
        self.path = thepath
        self.from_date = fromm
        self.to_date = to
        self.min_ratings = minr

    def readData(self):
        if self.from_date == None and self.min_ratings == 0:
            n = pd.read_csv(self.path,sep='\t')
            self.data = n


        elif self.from_date == None and self.min_ratings > 0:

            df = pd.read_csv(self.path, sep='\t')
            tes = df[['userID', 'movieID', 'rating']]
            n = tes[['userID', 'movieID']].groupby(['movieID'], as_index=False).count()
            n.columns = ['movieID', 'count']
            n = n[n['count'] >= self.min_ratings]
            n = n[['movieID']]

            n = pd.merge(n, tes, on='movieID', how='inner')
            self.data = n


        else:

            df = pd.read_csv(self.path,sep='\t')
            df['date_day'] = df['date_day'].astype(str)
            df['date_month'] = df['date_month'].astype(str)
            df['date_year'] = df['date_year'].astype(str)
            df['whole_date'] = df['date_day'] + "." + df['date_month'] + "." + df['date_year']
            df['whole_date'] = pd.to_datetime(df['whole_date'], format="%d.%m.%Y")
            fromd = datetime.datetime.strptime(self.from_date, "%d.%m.%Y")
            tod = datetime.datetime.strptime(self.to_date, "%d.%m.%Y")
            df_new = df[(df['whole_date'] >= fromd) & (df['whole_date'] <= tod)]

            tes = df[['userID', 'movieID', 'rating']]
            n = tes[['userID', 'movieID']].groupby(['movieID'], as_index=False).count()
            n.columns = ['movieID', 'count']
            n = n[n['count'] > self.min_ratings]
            n = n[['movieID']]

            df45 = df_new[['userID', 'movieID']]

            n = pd.merge(n, df45, on='movieID', how='inner')

            self.data = n


    def nRatings(self):
        return len(self.data)
