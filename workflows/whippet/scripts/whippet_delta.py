from snakemake.shell import shell
from os import path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

def inputCmd(subsets):
    cond_a_files = subsets[0]
    cond_b_files = subsets[1]
    input_cmd = "-a {} -b {}".format(cond_a_files, cond_b_files)
    print(input_cmd)
    return input_cmd

quant_subsets = snakemake.params.quant_subsets
input_cmd = inputCmd(quant_subsets)
output_path = snakemake.params.output_path
min_cov = snakemake.params.min_cov
min_sam = snakemake.params.min_sam

shell("whippet-delta.jl "
"{input_cmd} "
"-o {output_path} "
"-r {min_cov} "
"-s {min_sam} "
"{log}")
