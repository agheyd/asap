from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("miso --run "
"{snakemake.params.idx_dir} "
"{snakemake.params.bam} "
"--output-dir {snakemake.output} "
"--read-len {snakemake.params.read_len} "
"-p {snakemake.threads} "
"{log}")
