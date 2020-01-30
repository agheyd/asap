from os import path
from snakemake.shell import shell

#log = snakemake.log_fmt_shell(stdout=True, stderr=True)
log = snakemake.log
reads = snakemake.input.reads
output_dir = snakemake.output.quant.split(".")[0]
sam_out = snakemake.output.sam
idx = snakemake.input.idx.split(".")[0]

shell("whippet-quant.jl {reads} "
"-o {output_dir} "
"-x {idx} "
"--biascorrect "
"--sam "
"2> {log} 1> {sam_out}")
