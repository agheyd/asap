from os import path
from glob import glob
import rmats_utils.lister as lister

output_file = snakemake.output[0]
bam_files = snakemake.params.bam_files

lb.write_list(bam_files, output_file)
