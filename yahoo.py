#mannnn fuck EdX for telling me to get "course verified"
#I'll do it  after tomorrow since they wanna be hoes about it.
#This is my solo attempt to figure out pandas

#from pandas.io import data, wb

import pandas.io.data as web

import datetime

start = datetime.datetime(2010,1,1)

end = datetime.datetime(2013,1,27)

f = web.DataReader("F", 'yahoo', start,end)

f.ix['2010-01-04']


