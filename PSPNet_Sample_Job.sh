#!/bin/bash
#SBATCH --cpus-per-task=1   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=12800M        # memory per node
#SBATCH --time=00:05:00
#SBATCH --job-name=PSPNet
#SBATCH --exclusive
#SBATCH --output=outputs/%x-%j.out
#SBATCH --gres=gpu:4
module load nixpkgs/16.09 gcc/5.4.0 cuda/8.0.44 cudnn/6.0 opencv/3.3.0 python/3.6.3 bazel/0.5.2
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --upgrade pip

pip install -r requirements.txt

echo "Hello world"
### python pspnet.py -m pspnet101_cityscapes -i example_images/cityscapes.png -o example_results/cityscapes.jpg