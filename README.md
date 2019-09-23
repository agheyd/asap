ASAP
====

Alternative splicing analysis in parallel using [MISO](https://miso.readthedocs.io/en/fastmiso/), [rMATS](http://rnaseq-mats.sourceforge.net/) and [Whippet](https://github.com/timbitz/Whippet.jl)

Install
=======

1. Git clone this repository
```
git clone https://github.com/agheyd/asap.git /path/to/dir
```

2. Run install script
```
bash /path/to/dir/install.sh
```

3. Edit sample_sheet.csv and config.yml to match the current experiment

4. Launch pipeline
```
sbatch /path/to/dir/scripts/cluster_submit.sh /path/to/dir/Snakefile
```
