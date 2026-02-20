import pandas as pd
url = 'https://raw.githubusercontent.com/stoltzmaniac/wine-reviews-kaggle/master/winemag-data_first150k.csv'
df = pd.read_csv(url)
df.to_csv('Markus.csv', index=False)