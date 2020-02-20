#!/bin/bash
#SBATCH --cpus-per-task=1   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=12800M        # memory per node
#SBATCH --time=5:30:00
#SBATCH --job-name=PSPNet
############# ttSBATCH --exclusive
#SBATCH --output=outputs_folder_by_folder/%x-%j.out
#SBATCH --gres=gpu:4
module load nixpkgs/16.09 gcc/5.4.0 cuda/8.0.44 cudnn/6.0 opencv/3.3.0 python/3.5.4 bazel/0.5.2
virtualenv --no-download $SLURM_TMPDIR/env3
source $SLURM_TMPDIR/env3/bin/activate
# virtualenv env3
# source env3/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

pip install Pillow

echo "Hello world"
python PSPNet_Folder_Submission_folder_by_folder_faster.py -i 'GSV_Images_AB_16666/Pack_8/' -o 'Canada/GSV_Images_AB_16666/Pack_8/'
