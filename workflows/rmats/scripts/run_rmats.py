from os import path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

annotation = snakemake.params.annotation
comparison = snakemake.params.comparison
read_len = snakemake.params.read_len
star_idx = snakemake.params.star_idx
cstat = snakemake.params.cstat
list_dir = snakemake.params.list_dir
odir = path.dirname(snakemake.output[0])

C1 = comparison.split("_vs_")[0]
C2 = comparison.split("_vs_")[1]
L1 = path.join(list_dir, "{}.list".format(C1))
L2 = path.join(list_dir, "{}.list".format(C2))

shell("rmats.py "
"--b1 {L1} "
"--b2 {L2} "
"-t paired "
"--readLength {read_len} "
"--gtf {annotation} "
"--bi {star_idx} "
"--od {odir} "
"--nthread {snakemake.threads} "
"--cstat {cstat}"
"{log}")
