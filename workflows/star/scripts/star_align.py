from os import path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

reads = snakemake.input.reads
genome_dir = path.dirname(snakemake.input.star_idx[0])
outprefix = path.dirname(snakemake.output[0]) + "/"
extra = ""

if snakemake.config["parameters"]["star"]["align"]["2-pass-mode"]:
    extra += "--twopassMode Basic "

shell("STAR "
"--runThreadN {snakemake.threads} "
"--genomeDir {genome_dir} "
"--readFilesIn {reads} "
"--readFilesCommand zcat "
"--outSAMtype BAM SortedByCoordinate "
"--outFileNamePrefix {outprefix} "
"{extra}"
"{log}")