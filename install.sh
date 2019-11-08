#!/bin/bash
set -a

## Install miniconda3 if not already installed
if conda -V ; then
	echo "Conda is installed"
else
	echo "Installing Conda"
	wget -P ~/ https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
	mkdir -p ~/modules/
	bash ~/Miniconda3-latest-Linux-x86_64.sh -b -p ~/modules/miniconda3
	rm ~/Miniconda3-latest-Linux-x86_64.sh
	PATH=$PATH:~/modules/miniconda3/bin/
fi

## Install Whippet if not already installed
if $HOME/julia/bin/julia -E 'Pkg.installed("Whippet")' ; then
	echo "Whippet is installed"
else
	echo "Installing Whippet"
	mkdir ~/julia
	wget -P ~/ https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.4-linux-x86_64.tar.gz
	tar -C ~/julia -xvzf ~/julia-0.6.4-linux-x86_64.tar.gz --strip-components=1
	rm ~/julia-0.6.4-linux-x86_64.tar.gz
	$HOME/julia/bin/julia -e 'Pkg.add("Whippet");using Whippet'
	PATH="$PATH:$HOME/julia/bin"
	PATH="$PATH:$HOME/.julia/v0.6/Whippet/bin/"
fi
