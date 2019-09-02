import pandas as pd
from os import path
from functools import reduce
from utils import htools

## Load tables
miso_table = pd.read_csv(snakemake.input.miso, sep="\t")
rmats_table = pd.read_csv(snakemake.input.rmats, sep="\t")
whippet_table = (
    pd.read_csv(snakemake.input.whippet, sep="\t", index_col=False)
    .rename(columns={"Coord":"coord", "Strand":"strand"})
)

## Merge all to single table with all entries intact
threefold_overlap = reduce(lambda x,y: pd.merge(left=x, right=y, how="outer", on=["coord", "strand"]), [miso_table, rmats_table, whippet_table])

## Rename columns
comp = snakemake.wildcards.comparison
C1 = comp.split("_vs_")[0]
C2 = comp.split("_vs_")[1]

miso_cols = "coord strand type {}_posterior_mean {}_posterior_mean diff bayes_factor".format(C1,C2).split()
miso_cols_rename = "coord strand type miso_psi_{} miso_psi_{} miso_dpsi miso_bf".format(C1,C2).split()
rmats_cols = "IncLevel1 IncLevel2 IncLevelDifference FDR".split()
rmats_cols_rename = "rmats_psi_{} rmats_psi_{} rmats_dpsi rmats_fdr".format(C1,C2).split()
whippet_cols = "Type Psi_A Psi_B DeltaPsi Probability".split()
whippet_cols_rename = "whippet_type whippet_psi_{} whippet_psi_{} whippet_dpsi whippet_prob".format(C1,C2).split()

cols = miso_cols + rmats_cols + whippet_cols
cols_renamed = miso_cols_rename + rmats_cols_rename + whippet_cols_rename
threefold_overlap = threefold_overlap[cols]
threefold_overlap.columns = cols_renamed

## Define significance
threefold_overlap["miso_significant"] = threefold_overlap.apply(lambda x: htools.significant_miso(x), axis=1)
threefold_overlap["rmats_significant"] = threefold_overlap.apply(lambda x: htools.significant_rmats(x), axis=1)
threefold_overlap["whippet_significant"] = threefold_overlap.apply(lambda x: htools.significant_whippet(x), axis=1)

## Define groups
threefold_overlap["group"] = threefold_overlap.apply(lambda x: htools.define_group(x), axis=1)
threefold_overlap = threefold_overlap.fillna("not_found").drop_duplicates()

## Write table to file
threefold_overlap.to_csv(snakemake.output[0], index=False, sep="\t")
