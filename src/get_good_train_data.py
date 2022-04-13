import pandas as pd
import os

if __name__=="__main__":
    df = pd.read_csv("train_data.csv").fillna('')
    df['PDL_v1'] = df['PDL_v1'].map(lambda x: x.split('\n')[0])
    entries = os.listdir('train_data/')
    df.drop(df[~df['file_name'].isin(entries)].index, inplace=True)
    df.to_csv('train_data_standard.csv', index=False)