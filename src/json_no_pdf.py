import pandas as pd
import os
from alive_progress import alive_bar

def no_pdf(filename, filename_json, entries):
    return (filename not in entries and filename_json in entries)

if __name__=="__main__":
    entries = os.listdir('train_data_v0/')
    filenames = list(pd.read_csv("train_data_v0.csv").file_name)
    n = len(filenames)
    with alive_bar(n) as bar:
        for filename in filenames:
            filename_json = filename.split('.')[0]+'.json'
            if no_pdf(filename, filename_json, entries):
                os.remove(f"train_data_v0/{filename_json}")
            bar()