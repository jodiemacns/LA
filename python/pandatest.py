#wget http://labfiles.linuxacademy.com/python/pandas/temps.csv
import datetime as dt
import pandas as pd
import numpy as np

df = pd.read_csv("temps.csv")
head = df.head()

print head

df['CDT'] = df['CDT'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d'))
print df.head

ptable = pd.pivot_table(df, index=[df['CDT'].apply(lambda x: dt.datetime.strftime(x,'%B'))], values = ["Mean TemperatureF"], aggfunc=np.average)

print ptable

df['Month'] = df['CDT'].apply(lambda x: dt.datetime.strftime(x, '%B'))
ptable = pd.pivot_table(df, index=df['CDT'].dt.day, columns=df['Month'], values='Mean TemperatureF')
print ptable

df['Above 70'] = df['Mean TemperatureF'].apply(lambda x: 1 if x > 70 else 0)

ptable = pd.pivot_table(df, index=df["Month"], values=["Above 70"], aggfunc = np.sum)
print ptable

ptable = pd.pivot_table(df, index=df["Month"], values=["Max TemperatureF"], aggfunc = np.max)
print ptable

print ptable

