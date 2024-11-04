import pandas as pd

def clean_data(csv_file, output_file):
    df = pd.read_csv(csv_file)
    df.dropna(inplace=True)
    df.to_csv(output_file, index=False)

input_csv = '/path/to/input.csv'
cleaned_csv = '/path/to/output.csv'
clean_data(input_csv, cleaned_csv)
