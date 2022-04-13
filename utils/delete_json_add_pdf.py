from alive_progress import alive_bar
import shutil
import os

def no_file(filename_1, filename_2, entries_1, entries_2):
    return (filename_1 not in entries_1 and filename_2 in entries_2)

if __name__=="__main__":
    entries_raw = [file for file in os.listdir('raw_data/') if '.pdf' in file]
    entries_train = [file for file in os.listdir('train_data/') if '.json' in file]

    with alive_bar(len(entries_raw)) as bar:
        for filename in entries_train:
            filename_pdf = filename.split('.')[0]+'.pdf'
            if no_file(filename_pdf, filename, entries_raw, entries_train) == False:
                shutil.copy(f"raw_data/{filename_pdf}", f"train_data/{filename_pdf}")
            bar()

    with alive_bar(len(entries_train)) as bar:
        for filename in entries_raw:
            filename_json = filename.split('.')[0]+'.json'
            if no_file(filename, filename_json, entries_raw, entries_train):
                os.remove(f"train_data/{filename_json}")
            bar()