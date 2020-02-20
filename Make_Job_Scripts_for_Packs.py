import os

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def makeJobScript(main_folder, pack):
	job_text = ''
	job_text += '#!/bin/bash' + '\n'
	job_text += '#SBATCH --cpus-per-task=1   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.' + '\n'
	job_text += '#SBATCH --mem=12800M        # memory per node' + '\n'
	job_text += '#SBATCH --time=5:30:00' + '\n'
	job_text += '#SBATCH --job-name=PSPNet' + '\n'
	job_text += '#SBATCH --output=outputs_folder_by_folder/%x-%j.out' + '\n'
	job_text += '#SBATCH --gres=gpu:4' + '\n'

	job_text += 'module load nixpkgs/16.09 gcc/5.4.0 cuda/8.0.44 cudnn/6.0 opencv/3.3.0 python/3.5.4 bazel/0.5.2' + '\n'
	job_text += 'virtualenv --no-download $SLURM_TMPDIR/env3' + '\n'
	job_text += 'source $SLURM_TMPDIR/env3/bin/activate' + '\n'

	job_text += 'pip install --upgrade pip' + '\n'

	job_text += 'pip install -r requirements.txt' + '\n'

	job_text += 'pip install Pillow' + '\n'

	job_text += 'echo "Hello world"' + '\n'
	# job_text += 'python PSPNet_Folder_Submission_folder_by_folder_faster.py -i \'GSV_Images_AB_58331/Pack_0/\' -o \'Canada/GSV_Images_AB_58331/Pack_0/\'' + '\n'
	job_text += 'python PSPNet_Folder_Submission_folder_by_folder_faster.py -i \''+main_folder+'/'+pack+'/\''+' -o \'Canada/'+main_folder+'/'+pack+'/\'' + '\n'

	return job_text


main_folder = 'GSV_Images_YT_Packs'
# jobs_folder = main_folder + '_Jobs'
# if (not os.path.exists(jobs_folder)):
# 	os.makedirs(jobs_folder)

pack_list = get_immediate_subdirectories(main_folder)

for pack in pack_list:
	job_script_text = makeJobScript(main_folder, pack)
	file_name = 'YT_'+ pack + '.sh'
	tempFile = open(file_name, 'w')
	tempFile.write(job_script_text)
	tempFile.close()
