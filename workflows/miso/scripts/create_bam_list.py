import os
from glob import glob
from mutils.create_tools import cbam

s = snakemake.params.condition
output_file = snakemake.output[0]

files = glob(os.path.join(snakemake.params.bam_dir, "*", "Aligned.sortedByCoord.out.bam"))
sample_files = [x for x in files if s in x]

cbam.write_list(sample_files, output_file)
