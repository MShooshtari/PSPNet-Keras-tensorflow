import subprocess
from glob import glob

job_list = glob('BC_*.sh')

for job in job_list:
	job_command = ['sbatch', job]
	subprocess.call(job_command)
