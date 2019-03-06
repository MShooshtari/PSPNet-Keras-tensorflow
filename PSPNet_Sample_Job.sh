#!/bin/bash
#SBATCH --cpus-per-task=1   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=12800M        # memory per node
#SBATCH --time=00:30:00
#SBATCH --job-name=PSPNet
#SBATCH --output=outputs/%x-%j.out
echo "Hello world"
python pspnet.py -m pspnet101_cityscapes -i example_images/cityscapes.png -o example_results/cityscapes.jpg