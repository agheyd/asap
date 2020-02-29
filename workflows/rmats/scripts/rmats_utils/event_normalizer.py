import pandas as pd

def format_cols(rmats_table):

    rmats_include_cols = [
        'ID', 'GeneID', 'geneSymbol',
        'chr', 'strand', 'IncFormLen',
        'SkipFormLen', 'PValue', 'FDR',
        'IncLevel1', 'IncLevel2', 'IncLevelDifference',
        'event_type', 'coord'
    ]

    return rmats_table[rmats_include_cols]

def melt_mxe(mxe_table):
    mxe_table_new = pd.DataFrame()

    for index, row in mxe_table.iterrows():
        entry = row

        ae1 = entry.coord_ae1
        ae1_entry = entry.copy()
        ae1_entry["coord"] = ae1

        ae2 = entry.coord_ae2
        ae2_entry = entry.copy()
        ae2_entry["coord"] = ae2
        ae2_entry["IncLevelDifference"] = -ae2_entry["IncLevelDifference"]

        entry = pd.concat([ae1_entry, ae2_entry], axis=1).T
        mxe_table_new = mxe_table_new.append(entry)
        mxe_table_new_harmonized = harmonize_columns(mxe_table_new)

    return mxe_table_new_harmonized

def format(data_dict):

    for k,i in data_dict.items():
        if k == "A3SS":
            data_dict[k] = format_cols(data_dict[k])
        elif k == "A5SS":
            data_dict[k] = format_cols(data_dict[k])
        elif k == "MXE":
            data_dict[k] = melt_mxe(data_dict[k])
        elif k == "SE":
            data_dict[k] = format_cols(data_dict[k])
        elif k == "RI":
            data_dict[k] = format_cols(data_dict[k])

    return data_dict
