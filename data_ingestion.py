'''
    Data ingestion python
'''

import pandas as pd
import fileinput
import re
import glob

def train_data():

    # train_dataset = pd.DataFrame(columns=['phrase','sentiment'])
    filenames = glob.glob(f"train/**/*.txt",recursive=True)
    
    with fileinput.input(files=filenames) as f:
        
        input_data = [
            (line,re.search(r'\\(.*)\\',fileinput.filename()).group(0).strip('\\'))
            for line in f
        ]

    train_dataset = pd.DataFrame(input_data,columns=['phrase','sentiment'])

    train_dataset.to_csv("train_dataset.csv",index=False,header=True)    

def test_data():

    # train_dataset = pd.DataFrame(columns=['phrase','sentiment'])
    filenames = glob.glob(f"test/**/*.txt",recursive=True)
    
    with fileinput.input(files=filenames) as f:
        
        input_data = [
            (line,re.search(r'\\(.*)\\',fileinput.filename()).group(0).strip('\\'))
            for line in f
        ]

    test_dataset = pd.DataFrame(input_data,columns=['phrase','sentiment'])

    test_dataset.to_csv("test_dataset.csv",index=False,header=True)    

train_data()
test_data()