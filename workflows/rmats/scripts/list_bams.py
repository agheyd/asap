from os import path
from glob import glob
import rutils.list_tools.lbam as lb

condition = snakemake.params.condition
output_file = snakemake.output[0]

bams = glob(path.join(snakemake.params.bam_dir, "*", "Aligned.sortedByCoord.out.bam"))
selected_bams = [x for x in bams if condition in x]
bam_list = ",".join(selected_bams)

lb.write_list(bam_list, output_file)
