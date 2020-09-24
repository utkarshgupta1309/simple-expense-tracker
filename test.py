import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_excel('expense.xlsx')
df.set_index('Txn Date',inplace = True)
# print(df.tail())
# var = input("Select biller")
# df1 = df[df['Description'].str.contains(var)]
df2 = df[df['Description'].str.contains("ZOMATO")]
#frames = [df1, df2]
#df3 = pd.concat(df1)
df3 = df1
df3.to_excel('debit1.xlsx')
df3 = pd.read_excel('debit1.xlsx',parse_dates = True)
end = df3.sum()
print(end)
df3.plot(x='Txn Date',y='        Debit',kind = 'bar')
plt.show()
