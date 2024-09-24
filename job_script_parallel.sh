#!/bin/bash
#SBATCH --account=fc_emac
#SBATCH --partition=savio2
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00

module load anaconda3
module load gurobi/10.0.0
module load parallel/20220522
source activate my-conda-env

export WDIR=/global/home/users/jesscarney/yes_hydrogen
cd $WDIR 

export JOBS_PER_NODE=$(($SLURM_CPUS_ON_NODE/$SLURM_CPUS_PER_TASK))

echo $SLURM_JOB_NODELIST |sed s/\,/\\n/g > hostfile

parallel --jobs $JOBS_PER_NODE --slf hostfile --wd $WDIR --joblog task.log --a task.ls sh wrap.sh {} $SLURM_CPUS_PER_TASK
