import matplotlib as mpl
import mplcyberpunk
from bcb import currency
from bcb import sgs
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
from matplotlib.dates import date2num
from datetime import datetime
from datetime import timedelta

plt.style.use("cyberpunk")

selic = sgs.get({'selic': 432}, start = '2010-01-01')

today = datetime.now()
last_year = today - timedelta(days = 366)

inflacao = sgs.get({ 'ipca': 433, 'igp-m': 189 }, start = last_year + timedelta(180))

df = currency.get(['USD', 'EUR'], start='2000-01-01', end='2023-10-10', side='both')

print(df)