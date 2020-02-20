import glob
import os
from zipfile import ZipFile
import sys

if __name__ == '__main__':
	inputFolder = sys.argv[2]
	outputFolder = sys.argv[4]
	if (not os.path.exists(outputFolder)):
		os.makedirs(outputFolder)

	##### Added by Mahdi #####
	commandText = 'python pspnet_folder_faster.py -m pspnet101_cityscapes -g ' + inputFolder + ' -o ' + outputFolder
	os.system(commandText)
