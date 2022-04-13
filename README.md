# Create a virtual environment
’python3 -m venv env’

# Install the Python packages
’pip install -r requirements.txt’

# Prepare your training data

1. Create a folder *raw_data*

If you have a CSV file containing at least two columns: one listing the filename for each row, and one containing the URL of the file for each row:
> Scrap your CSV file and download the files in *raw_data* while naming them according to the filename column
> ’python3 utils/scraping_files.py [-h] [-csv CSV] [-column_url COLUMN_URL] [-column_filename COLUMN_FILENAME]

’’’
optional arguments:
  -h, --help            show this help message and exit
  -csv CSV              CSV file containing the URLs of the files
  -column_url COLUMN_URL
                        Column of the CSV corresponding to the URL of each PDF / each row has one url
  -column_filename COLUMN_FILENAME
                        Column of the CSV corresponding to the filename of each PDF / each row has one filename
’’’

2. Create JSON files for the files in *raw_data* containing the features that you want to train the model on as well as their values, and put the JSON files in *train_data* folder.

If you have a CSV containing the features, you are free to use ’utils/retrieve_data.py’!

3. Now, you have your documents / files in *raw_data* and your JSON files in *train_data*. What you want to do is to merge the two folders into *train_data*, meaning that you want in the end to have in the folder two files for each filename: a PDF (the original document), and its JSON (dictionary of features). 

You can use ’utils/delete_json_add_pdf.py’ to copy the PDF files from *raw_data* to *train_data* if there is a JSON associated in *train_data*, and to delete the JSON files if the PDF file associated doesn't exist in *raw_data*.