from os import path
from glob import glob
import rutils.list_tools.lbam as lb

output_file = snakemake.output[0]
bam_files = snakemake.params.bam_files

lb.write_list(bam_files, output_file)
