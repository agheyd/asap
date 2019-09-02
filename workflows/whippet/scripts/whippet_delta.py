from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

quant_path = snakemake.params.quant_path
comparison = snakemake.params.comparison
output_path = snakemake.params.output_path
min_cov = snakemake.params.min_cov
min_sam = snakemake.params.min_sam

cond_A, cond_B = comparison.split("_vs_")

shell("whippet-delta.jl "
"-d {quant_path} "
"-a {cond_A} "
"-b {cond_B} "
"-o {output_path} "
"-r {min_cov} "
"-s {min_sam} "
"{log}")

