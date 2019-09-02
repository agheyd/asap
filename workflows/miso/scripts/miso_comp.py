import os
from glob import glob
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
comparison = snakemake.params.comparison.split("_vs_")
run_dir = snakemake.params.run_dir
idx = snakemake.params.idx
dirs = glob(os.path.join(run_dir, "*", idx))
run_1 = [x for x in dirs if comparison[0] in x]
run_2 = [x for x in dirs if comparison[1] in x]

shell("compare_miso "
"--compare-samples {run_1} {run_2} "
"{snakemake.params.output_dir} "
"{log}")
