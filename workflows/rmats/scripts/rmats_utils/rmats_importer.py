import pandas as pd

def import_files(file_path, event_type):

    data_table = pd.read_csv(file_path, sep="\t")
    data_table["event_type"] = event_type

    return data_table
