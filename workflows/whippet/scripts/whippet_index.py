from os import path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

fasta = snakemake.input.genome
annotation = snakemake.input.annotation
output_dir = snakemake.output[0].split(".")[0]

shell("whippet-index.jl "
"--fasta {fasta} "
"--gtf {annotation} "
"--suppress-low-tsl "
"-x {output_dir} "
"{log}")

