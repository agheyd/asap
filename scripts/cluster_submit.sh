#!/bin/bash

#SBATCH --mail-user=didrio87@zedat.fu-berlin.de
#SBATCH --mail-type=end
#SBATCH --job-name=ASAP
#SBATCH --time=24:00:00
#SBATCH --nodes=1-1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4G
#SBATCH --qos=medium

SNAKEFILE=$1

## Arrange PATH
export PATH="$PATH:$HOME/bin"
export PATH="$PATH:$HOME/modules/miniconda3/bin"
export PATH="$PATH:$HOME/julia/bin"
export PATH="$PATH:$HOME/.julia/v0.6/Whippet/bin/"

## Launch pipeline
module add Singularity snakemake
submit_asap $SNAKEFILE
module remove Singularity snakemake
