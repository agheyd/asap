from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("summarize_miso "
"--summarize-samples {snakemake.params.sample_dir} "
"{snakemake.params.output_dir} "
"{log}")
