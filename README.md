ASAP
====

Alternative splicing analysis in parallel using [MISO](https://miso.readthedocs.io/en/fastmiso/), [rMATS](http://rnaseq-mats.sourceforge.net/) and [Whippet](https://github.com/timbitz/Whippet.jl)

Install
=======

1. Install [Miniconda](https://conda.io/en/latest/miniconda.html)
2. Create pipeline directory:
```
mkdir -p path/to/asap
```
3. Clone git repository
```
git clone https://github.com/DidrikOlofsson/asap.git path/to/asap
```
4. Create Snakemake environment from provided environment file
```
conda env create -n snk -f path/to/asap/envs/snakemake.yml
```
5. Activate environment
```
conda activate snk
```
6. Run pipeline locally:
```
snakemake --use-conda -s path/to/asap/Snakefile
```
7. Run pipeline on cluster:
```
nohup python path/to/asap/scripts/run_cluster.py path/to/asap/Snakefile &
```
