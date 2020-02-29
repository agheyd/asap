import pandas as pd

def format_cols(rmats_table):

    rmats_include_cols = [
        'ID', 'GeneID', 'geneSymbol',
        'chr', 'strand', 'IncFormLen',
        'SkipFormLen', 'PValue', 'FDR',
        'IncLevel1', 'IncLevel2', 'IncLevelDifference',
        'event_type', 'coord', 'flank'
    ]

    return rmats_table[rmats_include_cols]

def format(data_dict):

    for k,i in data_dict.items():
        if k == "A3SS":
            data_dict[k] = format_cols(data_dict[k])
        elif k == "A5SS":
            data_dict[k] = format_cols(data_dict[k])
        elif k == "MXE":
            data_dict[k] = format_cols(data_dict[k])
        elif k == "SE":
            data_dict[k] = format_cols(data_dict[k])
        elif k == "RI":
            data_dict[k] = format_cols(data_dict[k])

    return data_dict
