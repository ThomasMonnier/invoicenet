import pandas as pd 
import requests
from alive_progress import alive_bar

def scrap_url(url, filename):
    r = requests.get(url, allow_redirects=True)
    try:
        r.content.decode("utf-8") == '{"error":"file deleted"}'
    except:
        open('train_data_v0/'+filename, 'wb').write(r.content)

if __name__=='__main__':
    df = pd.read_csv('train_data_v0.csv')
    n_row = df.shape[0]
    with alive_bar(n_row) as bar:
        for iter, row in df.iterrows():
            url = row['file_link']
            filename = row['file_name']
            scrap_url(url, filename)
            bar()