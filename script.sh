#!/bin/bash -l

#SBATCH -J TCLB_test
#SBATCH -N 1
#SBATCH -n 4
#SBATCH --ntasks-per-node=4
#SBATCH --time=2:00:00 
#SBATCH -p gpu
#SBATCH --gres=gpu:1

# SBATCH -A director2047

nvidia-smi
 
hostname

which esysparticle
echo $ESPATH
echo $LD_LIBRARY_PATH

cd \$SLURM_SUBMIT_DIR 

module load mpi/openmpi-x86_64
mpirun -np 1 -x LD_LIBRARY_PATH -x PATH -x PYTHONPATH ~/TCLB_part/CLB/d3q27_cumulant_part/main shear.xml


