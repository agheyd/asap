from os import path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

reads = snakemake.input.reads
output_dir = snakemake.params.output_dir
idx = snakemake.input.idx.split(".")[0]

shell("whippet-quant.jl {reads} "
"-o {output_dir} "
"-x {idx} "
"--biascorrect "
"{log}")
