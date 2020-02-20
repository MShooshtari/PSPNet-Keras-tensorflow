import glob
import os

inputFolder = 'St_Johns_GSV_Metadata_and_Images/St_Johns_GSV_Images/'
outputFolder = 'Results_folder_by_folder' + '/' + inputFolder
##### Added by Mahdi #####
commandText = 'python pspnet_folder_faster.py -m pspnet101_cityscapes -g ' + inputFolder + ' -o ' + outputFolder
os.system(commandText)
##########################	

# imageFolderList = get_immediate_subdirectories(inputFolder)



# for imageFolder in imageFolderList:
# 	folderAddress = inputFolder + '/' + imageFolder
# 	tempOutputFolder = outputFolder + '/' + imageFolder
# 	if (not os.path.exists(tempOutputFolder)):
# 		os.makedirs(tempOutputFolder)

# 	commandText = 'python pspnet_folder.py -m pspnet101_cityscapes -g ' + folderAddress + ' -o ' + tempOutputFolder
# 	os.system(commandText)






# # for imageAddress in imagesList:
# 	print(imageAddress)
# 	imageName = os.path.basename(imageAddress)
# 	print(imageName)

# 	imageOutputAddress = imageAddress.replace(inputFolder, outputFolder).replace('.png', '.jpg')
# 	print(imageOutputAddress)
# 	imageName = os.path.basename(imageOutputAddress)
# 	tempOutputFolder = imageOutputAddress.replace(imageName, '')
# 	if (not os.path.exists(tempOutputFolder)):
# 		os.makedirs(tempOutputFolder)
# 	commandText = 'python pspnet.py -m pspnet101_cityscapes -i ' + imageAddress + ' -o ' + imageOutputAddress
# 	os.system(commandText)

