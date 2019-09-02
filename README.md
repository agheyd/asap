ASAP
====

Alternative splicing analysis in parallel using [MISO](https://miso.readthedocs.io/en/fastmiso/), [rMATS](http://rnaseq-mats.sourceforge.net/) and [Whippet](https://github.com/timbitz/Whippet.jl)

Install
=======

1. Install [Miniconda](https://conda.io/en/latest/miniconda.html)
2. Create pipeline directory:
```
mkdir -p ~/asap
```
3. Clone git repository
```
git clone https://github.com/DidrikOlofsson/asap.git ~/asap
```
4. Create Snakemake environment from provided environment file
```
conda env create -n snk -f ~/asap/envs/snakemake.yml
```
5. Activate environment
```
conda activate snk
```
6. Run pipeline locally:
```
snakemake --use-conda -s ~/asap/Snakefile
```
7. Run pipeline on cluster:
```
nohup python ~/asap/scripts/run_cluster.py ~/asap/Snakefile &
```
