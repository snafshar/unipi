#!/bin/bash
#SBATCH --job-name=portfolio-benchmark
#SBATCH --partition=normal
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=4
#SBATCH --output=results-%j.out
set -euo pipefail
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK}"
echo "job=${SLURM_JOB_ID} host=$(hostname) threads=${OMP_NUM_THREADS}"
./benchmark --threads "${OMP_NUM_THREADS}"
