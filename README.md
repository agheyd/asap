ASAP
====

Alternative splicing analysis in parallel using [MISO](https://miso.readthedocs.io/en/fastmiso/), [rMATS](http://rnaseq-mats.sourceforge.net/) and [Whippet](https://github.com/timbitz/Whippet.jl)

Install
====

1. Git clone this repository
```
git clone https://github.com/agheyd/asap.git /path/to/dir
```

2. Run install script
```
/path/to/dir/install.sh
```

3. Install HPC submission script
```
pip install git+https://github.com/agheyd/submit2hpc.git
```

Run
====

1. Edit sample_sheet.csv and config.yml to match your experimental parameters

2. Launch pipeline on HPC
```
nohup submit2hpc --configfile /path/to/config.yml /path/to/dir/Snakefile &
```
