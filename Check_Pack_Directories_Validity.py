import os
from glob import glob 

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


main_folder = 'Canada'

sub_dir_list = get_immediate_subdirectories(main_folder)
print(sub_dir_list)

for sub_dir in sub_dir_list:
	pack_list = get_immediate_subdirectories(main_folder+'/'+sub_dir)
	for pack in pack_list:
		pack_folder = main_folder+'/'+sub_dir+'/'+pack
		img_list = glob(pack_folder+'/*.png')
		if (len(img_list)!=12000):
			print(pack_folder)
			print(len(img_list))
			print('----------------------')