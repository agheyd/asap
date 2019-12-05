from os import path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

reads = snakemake.input.reads
genome_dir = snakemake.input.star_idx
outprefix = path.dirname(snakemake.output[0]) + "/"
extra = ""

if snakemake.config["parameters"]["star"]["align"]["2-pass-mode"]:
    extra += "--twopassMode Basic "

shell("STAR "
"--runThreadN {snakemake.params.ntasks} "
"--genomeDir {genome_dir} "
"--readFilesIn {reads} "
"--readFilesCommand zcat "
"--outSAMtype BAM SortedByCoordinate "
"--outFileNamePrefix {outprefix} "
"{extra}"
"{log}")
