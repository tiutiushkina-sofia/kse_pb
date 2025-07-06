import pandas as pd
import matplotlib.pyplot as plt
import requests
api_key = "35eb1b300ae38cb138384c99b763dd9a"
symbol = "AAPL"

url = f"http://api.marketstack.com/v2/eod?access_key={api_key}&symbols={symbol}"
r = requests.get(url)
data = r.json()
print(data)

df = pd.DataFrame(data['data'],columns=["open","close","high","low","volume","date"])
df['date'] = pd.to_datetime(df['date'])

df['short_ma'] = df['open'].rolling(window=7).mean().shift(-7)
df['long_ma'] = df['open'].rolling(window=14).mean().shift(-14)

# Модель:
# Якщо short term ma перетинає long term ma йдучи знизу, це говорить про ймовірне зниження ціни надалі, тому ми продаємо
# Якщо short term ma перетинає long term ma йдучи згори, це говорить про ймовірне підвиження ціни надалі, тому ми купляємо
# Така здогадка виникла після візуалізації на графіку наших кривих

prev_delta = df['long_ma'].shift(1) - df['short_ma'].shift(1)
curr_delta = df['long_ma'] - df['short_ma']

df_sell = df[(prev_delta <= 0) & (curr_delta > 0)].reset_index(drop=True)
df_buy = df[(prev_delta > 0) & (curr_delta <= 0)].reset_index(drop=True)

# Знайшли різницю long term ma та short term ma чи вони додатні чи від'ємні за поточний день та за попередній
# Поставили сигнали купівлі та продажу

ax = df.plot(x='date',y=['open','short_ma','long_ma'],kind='line')
ax.plot(df_sell['date'], df_sell['open'], 'ro', label='sell')
ax.plot(df_buy['date'], df_buy['open'], 'bo', label='buy')

if len(df_buy) > len(df_sell):
    df_buy.head(len(df_sell))

if len(df_buy) < len(df_sell):
    df_sell.head(len(df_buy))

# Внормовуємо кількість сигналів купівлі та продажу щоб нормально порахувати прибуток

is_long = df_buy['date'] < df_sell['date']

df_trades = pd.DataFrame(columns=['type', 'entry_price', 'exit_price'])
n = len(is_long)
for i in range(n):
    if is_long[i]:
        df_trades.loc[i] = ['long', df_buy['open'][i], df_sell['open'][i]]
    else:
        df_trades.loc[i] = ['short', df_sell['open'][i], df_buy['open'][i]]


long_profits = (df_trades['exit_price']-df_trades['entry_price'])/df_trades['entry_price']
short_profits = (df_trades['entry_price']-df_trades['exit_price'])/df_trades['entry_price']
df_trades['profit'] = 0.0

for i in range(n):
    if is_long[i]:
        df_trades.loc[i, 'profit'] = (long_profits[i])
    else:
        df_trades.loc[i, 'profit'] = (short_profits[i])

total_profit = df_trades['profit'].sum()
print('total profit', total_profit*100, '%')
print('buy signals\n', df_buy)
print('sell signals\n', df_sell)

plt.legend()
plt.show()