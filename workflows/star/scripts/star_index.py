from os import path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

read_length = snakemake.config["parameters"]["general"]["read_length"]
genome_dir = snakemake.output[0] + "/"
annotation = snakemake.config["locations"]["annotation"]
extra = ""

if snakemake.config["parameters"]["star"]["index"]["sjdb_overhang"]:
    extra += "--sjdbOverhang {} ".format(str(read_length - 1))

shell("STAR "
"--runMode genomeGenerate "
"--runThreadN {snakemake.params.ntasks} "
"--genomeDir {genome_dir} "
"--outFileNamePrefix {genome_dir} "
"--genomeFastaFiles {snakemake.input} "
"--sjdbGTFfile {annotation} "
"{extra}"
"{log}")
