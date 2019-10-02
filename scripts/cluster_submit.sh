#!/bin/bash

#SBATCH --mail-type=none
#SBATCH --job-name=ASAP
#SBATCH --time=24:00:00
#SBATCH --nodes=1-1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4G
#SBATCH --qos=medium

if [[ $1 ]]; then
	SNAKEFILE=$1
else
	echo "Please provide a valid Snakefile"
	exit 1
fi

EXTRA=""

if [[ "$2" == "whippet" ]]; then
	EXTRA="--until WhippetDelta"
elif [[ "$2" == "rmats" ]]; then
	EXTRA="--until AddrMATSCoord"
elif [[ "$2" == "miso" ]]; then
	EXTRA="--until AddMisoCoord"
fi

## Arrange PATH
export PATH="$PATH:$HOME/bin"
export PATH="$PATH:$HOME/modules/miniconda3/bin"
export PATH="$PATH:$HOME/julia/bin"
export PATH="$PATH:$HOME/.julia/v0.6/Whippet/bin/"

## Launch pipeline
module add Singularity snakemake
submit_asap $SNAKEFILE $EXTRA
module remove Singularity snakemake
