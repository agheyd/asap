import os
import pandas as pd

def format_names(comp_string, data_frame):
    sample1 = comp_string.split("_vs_")[0]
    sample2 = comp_string.split("_vs_")[1]
    sample1_replaced = [x.replace("sample1", sample1) for x in data_frame.columns]
    sample2_replaced = [x.replace("sample2", sample2) for x in sample1_replaced]
    data_frame.columns = sample2_replaced
    return data_frame

def concat_comp_tables(comp_string, file_list, output_path):
    df_list = []
    for f in file_list:
        name = os.path.basename(f).split("_vs_")[0]
        df = pd.read_csv(f, sep="\t")
        df["type"] = name
        df_list.append(df)
    full_table = pd.concat(df_list).reset_index(drop=True)
    full_table = format_names(comp_string, full_table)
    full_table.to_csv(output_path, sep="\t", index=False)
    return None
