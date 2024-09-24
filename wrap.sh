#!/usr/bin/env bash

module load anaconda3
module load gurobi/10.0.0
source activate my-conda-env

python run_script_pareto_parallel.py $1
