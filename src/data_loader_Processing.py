import pandas as pd

class DataLoaderProcessing:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_data(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip')
        df = df.dropna()
        df = df.drop_duplicates()
        df['description'] = df['title'] + ' ' + df['genres']
        df_new = df[['description']]
        df_new['description'] = df_new['description'].str.replace('|', ',', regex=False)
        df_new = df_new.reset_index(drop=True)
        df_new.to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv