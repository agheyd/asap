import yaml, os
from glob import glob
import pandas as pd
from mutils.merge_tools import msum

sum_path = snakemake.params.sum_dir
condition = snakemake.params.condition
sum_files = glob(os.path.join(sum_path, "*", "*", "*", "*"))
merge_files = [x for x in sum_files if condition in x]
output_path = snakemake.output[0]

msum.concat_sum_tables(merge_files, output_path)
