import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("samtools index "
"{snakemake.input} "
"{log}")
