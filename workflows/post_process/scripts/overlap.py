import pandas as pd
import yaml
from glob import glob
from os import path
from functools import reduce

def get_tables_array(tool_selection, output_dir, comparison):
    tables = []
    for t in tool_selection:
        if t == "miso":
            pass
        if t == "rmats":
            diff_tables = glob(
                path.join(
                    output_dir, "rmats", "results", comparison, "*.merged.w_coord.tsv"
                )
            )
            tables += diff_tables
        elif t == "whippet":
            diff_tables = glob(
                path.join(output_dir, "whippet", "delta", comparison, "*.diff.gz")
            )
            tables += diff_tables
    return tables

def format_cols(df_array, comparison):
    new_df_array = []
    condition_A, condition_B = comparison.split("_vs_")
    for df in df_array:
        if "bayes_factor" in df.columns:
            pass
        elif "FDR" in df.columns:
            rmats_cols = "coord event_type strand IncLevel1 IncLevel2 IncLevelDifference FDR".split()
            rmats_cols_rename = (
                "coord event_type strand rmats_psi_{} rmats_psi_{} rmats_dpsi rmats_fdr"
                .format(condition_A,condition_B).split()
            )
            df_subset = df[rmats_cols]
            df_subset.columns = rmats_cols_rename
            new_df_array.append(df_subset)
        elif "Probability" in df.columns:
            whippet_cols = "Coord Type Strand Psi_A Psi_B DeltaPsi Probability".split()
            whippet_cols_rename = (
                "coord whippet_type strand whippet_psi_{} whippet_psi_{} whippet_dpsi whippet_prob"
                .format(condition_A,condition_B).split()
            )
            df_subset = df[whippet_cols]
            df_subset.columns = whippet_cols_rename
            new_df_array.append(df_subset)
    return new_df_array

def significant_miso(x):
    if ((x.miso_dpsi >= 0.1) or (x.miso_dpsi <= -0.1)) and (x.miso_bf > 5):
        return True
    else:
        return False
    return None

def significant_rmats(x):
    if ((x.rmats_dpsi >= 0.1) or (x.rmats_dpsi <= -0.1)) and (x.rmats_fdr <= 0.1):
        return True
    else:
        return False
    return None

def significant_whippet(x):
    if ((x.whippet_dpsi >= 0.1) or (x.whippet_dpsi <= -0.1)) and (x.whippet_prob >= 0.9):
        return True
    else:
        return False
    return None

def assign_significance(tool_selection, dataframe):
    if "miso" in tool_selection:
        pass
    if "rmats" in tool_selection:
        dataframe["rmats_significant"] = dataframe.apply(lambda x: significant_rmats(x), axis=1)
    if "whippet" in tool_selection:
        dataframe["whippet_significant"] = dataframe.apply(lambda x: significant_whippet(x), axis=1)
    return dataframe

def assign_group(tool_selection, entry):
    group = ""
    for t in tool_selection:
        if t == "miso":
            if entry.miso_significant:
                group += "m"
        if t == "rmats":
            if entry.rmats_significant:
                group += "r"
        if t == "whippet":
            if entry.whippet_significant:
                group += "w"
    if group != "":
        entry["group"] = group
    elif group == "":
        entry["group"] = "none"
    return entry

tool_selection = config["parameters"]["general"]["tools"]
output_dir = config["locations"]["output_dir"]
comparison = snakemake.wildcards.comparison
tables = get_tables_array(tool_selection, output_dir, comparison)

df_array = [pd.read_csv(x, sep="\t", index_col=False) for x in tables]
df_array_formated = format_cols(df_array, comparison)
df_merged = reduce(lambda x,y: pd.merge(
    left=x, right=y, how="outer", on=["coord", "strand"]), df_array_formated
)
df_w_significance = assign_significance(tool_selection, df_merged)
df_w_group = (
    df_w_significance.apply(lambda x: assign_group(tool_selection, x), axis=1)
    .drop_duplicates()
)
df_w_group.to_csv(snakemake.output, sep="\t", index=False)
