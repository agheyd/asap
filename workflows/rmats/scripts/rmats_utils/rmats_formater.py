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
    return {k:format_cols(v) for (k,v) in data_dict.items()}
