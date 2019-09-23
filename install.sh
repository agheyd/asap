#!/bin/bash

## Set up symbolic links to submission scripts
mkdir ~/bin
S_SCRIPT=$(readlink -f scripts/submit.py)
ln -s $S_SCRIPT ~/bin/submit_asap

## Install miniconda3
wget -P ~/ https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ~/Miniconda3-latest-Linux-x86_64.sh -b -p ~/modules/miniconda3
rm ~/Miniconda3-latest-Linux-x86_64.sh

## Install Whippet
mkdir ~/julia
wget -P ~/ https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.4-linux-x86_64.tar.gz
tar -C ~/julia -xvzf ~/julia-0.6.4-linux-x86_64.tar.gz --strip-components=1
rm ~/julia-0.6.4-linux-x86_64.tar.gz
$HOME/julia/bin/julia -e 'Pkg.add("Whippet");using Whippet'
