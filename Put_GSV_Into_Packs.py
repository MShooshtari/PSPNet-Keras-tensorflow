import os
import sys
import shutil

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

main_folder = 'GSV_Images_YT'
output_folder = main_folder + '_Packs'


pc_folder_list = get_immediate_subdirectories(main_folder)
pc_folder_len = len(pc_folder_list)

pack_size = 1000
number_of_packs = pc_folder_len//pack_size + 1
print(number_of_packs)

for i in range(number_of_packs):
	start_idx = i*pack_size
	end_idx = min(pc_folder_len, (i+1)*pack_size)
	pack_list = pc_folder_list[start_idx:end_idx]
	for pc_folder in pack_list:
		src = main_folder + '/' + pc_folder
		dst = output_folder + '/' + 'Pack_'+str(i)
		if (not os.path.exists(dst)):
			os.makedirs(dst)
		# print(src)
		# print(dst)
		# exit()
		shutil.move(src, dst)
		# exit()


	print(pack_list)
	print(start_idx)
	print(end_idx)