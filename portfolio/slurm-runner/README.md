# SLURM Experiment Runner

I created this SLURM batch template to run reproducible performance
experiments. I record the job identifier, host, and allocated thread count so
that each result has enough execution context to be interpreted later.

I edit the executable and resource values for a specific benchmark, then
submit it with `sbatch run.slurm`.
