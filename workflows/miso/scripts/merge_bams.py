import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("samtools merge "
"{snakemake.output} "
"{snakemake.params.bam_input} "
"-O BAM "
"-@ {snakemake.params.ntasks} "
"{log}")
