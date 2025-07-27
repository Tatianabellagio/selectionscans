#!/bin/bash
#SBATCH --job-name="sf2_chr4"
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32G
#SBATCH --output=/carnegie/nobackup/scratch/tbellagio/selection_scan/sweepfinder//sweepfinder2_chr4_20250722_030505_output.txt
#SBATCH --mail-user=tbellagio@carnegiescience.edu
#SBATCH --mail-type=FAIL

cd /carnegie/nobackup/scratch/tbellagio/selection_scan/sweepfinder/
pwd

echo "Running SweepFinder2 on chromosome 4..."

/home/tbellagio/SweepFinder2/SweepFinder2 -sg 100 sweepfinder2_chr4.sf sweepfinder_chr4_100w_nback.out
