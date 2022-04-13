import pandas as pd 
import requests
import argparse
from alive_progress import alive_bar

def scrap_url(url, filename):
    r = requests.get(url, allow_redirects=True)
    try:
        r.content.decode("utf-8") == '{"error":"file deleted"}'
        print('Error: File deleted')
    except:
        open('raw_data/'+filename, 'wb').write(r.content)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-csv', type=str, help="CSV file containing the URLs of the files")
    parser.add_argument('-column_url', type=str, help='Column of the CSV corresponding to the URL of each PDF / each row has one url')
    parser.add_argument('-column_filename', type=str, help='Column of the CSV corresponding to the filename of each PDF / each row has one filename')

    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    n_row = df.shape[0]
    with alive_bar(n_row) as bar:
        for iter, row in df.iterrows():
            url = row[args.column_url]
            filename = row[args.column_filename]
            scrap_url(url, filename)
            bar()