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
bash /path/to/dir/install.sh
```

Run
====

1. Edit sample_sheet.csv and config.yml to match your current experiment

2. Launch pipeline on HPC
```
nohup ./path/to/dir/scripts/submit.py /path/to/dir/Snakefile &
```

3. You can run individual tools by specifying this as a separate command line argument
```
nohup ./path/to/dir/scripts/submit.py /path/to/dir/Snakefile --tool miso|rmats|whippet
```
