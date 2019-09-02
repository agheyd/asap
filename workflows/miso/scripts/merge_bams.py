import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("samtools merge "
"-b {snakemake.input} "
"-O BAM "
"-@ {snakemake.threads} "
"{snakemake.output} "
"{log}")
