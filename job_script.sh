#!/bin/bash
#SBATCH --account=fc_emac
#SBATCH --partition=savio2
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=01:00:00

module load anaconda3
module load gurobi/10.0.0
source activate my-conda-env

python run_script_overview.py