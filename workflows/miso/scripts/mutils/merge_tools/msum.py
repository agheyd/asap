def concat_sum_tables(file_list, output_path):
    df_list = []
    for f in file_list:
        name = os.path.basename(f).split(".")[0]
        df = pd.read_csv(f, sep="\t")
        df["type"] = name
        df_list.append(df)
    full_table = pd.concat(df_list).reset_index(drop=True)
    full_table.to_csv(output_path, sep="\t", index=False)
    return None
