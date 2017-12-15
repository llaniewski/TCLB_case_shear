# Shear case for TCLB+ESYS

`shear.xml` - main configuration file for TCLB
`script.sh` - SLURM batch script for Goliath cluster (run with `sbatch script.sh`)
`make_vtk` - script which runs dump2vtk to generate files for ParaView
`WallLoader.py` - Python functions for loading walls in ESYS

## Notice:
in `script.sh` you have to change the path to your TCLB installation