import yaml, os
from glob import glob
import pandas as pd
from mutils.merge_tools import mcomp

comp_string = snakemake.params.comp
comp_dir = os.path.join(snakemake.params.comp_dir, comp_string)
comp_files = glob(os.path.join(comp_dir, "*", "*", "*"))

mcomp.concat_comp_tables(comp_string, comp_files, snakemake.output[0])
