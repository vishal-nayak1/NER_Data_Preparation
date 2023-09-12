import pandas as pd
import os
import re
# from fuzzywuzzy import process
# import re

import glob, os
# for file in glob.glob("./HDFC/*train-box.txt"):
# 	print(file)
# filenames = glob.glob("./HDFC/*train.txt")
from glob import glob
folders  = glob("./health/*/", recursive = True)
# print(folders)
for folder in folders:
	print(folder)
	with open(f"../buckets/{folder}/completed.txt") as infile:
		contents = infile.readlines()
		filenames = [k.rstrip('\n') for k in contents if k.rstrip('\n') != '']

	# print(filenames)
	# filenames = ['./fggi/train_image.txt', './hdfc/train_image.txt', './reli/train_image.txt', './icici/train_image.txt', './royal/train_image.txt']

	with open("./train.txt", "a+") as final_train, open("./train_box.txt", "a+") as final_box, open("./train_image.txt", "a+") as final_image:
		for filename in filenames:
			try:
				# 'PGTWZ75ETXE_od_1'
				if any(elem in filename for elem in ['PGTUGPQQUPU_tp_2', 'PGTUVVTVRWI_od_4', 'PGTWWXNC16Q_od_1', 'PGTXPAJDVK2_od_1']):
					print(filename)
					continue
				with open(f'./{folder}/{filename}_train-box.txt') as train_box, open(f'./{folder}/{filename}_train-image.txt') as train_img, open(f'./{folder}/{filename}_train.txt') as train:
				    trn_box = train_box.readlines()
				    trn_img = train_img.readlines()
				    trn = train.readlines()
				    trn_box_lines = [k.rstrip('\n') for k in trn_box if k.rstrip('\n') != '']
				    trn_img_lines = [k.rstrip('\n') for k in trn_img if k.rstrip('\n') != '']
				    trn_lines = [k.rstrip('\n') for k in trn if k.rstrip('\n') != '']
				    for boxline, imgline, trnline in zip(trn_box_lines, trn_img_lines, trn_lines):
				    	if boxline == '\n' or trnline == '\n':
				    		continue
				    		print("found new line")
				    	final_train.write(trnline)
				    	final_train.write('\n')

				    	final_box.write(boxline)
				    	final_box.write('\n')

				    	img_list = imgline.split("\t")[:-1]
				    	img_path = imgline.split("\t")[-1].replace(" ", "")
				    	new_imgline = f'{img_list[0]}\t{img_list[1]}\t{img_list[2]}\t{img_path}'
				    	# print(new_imgline)
				    	final_image.write(new_imgline)
				    	final_image.write('\n')

				    final_train.write('\n')
				    final_image.write('\n')
				    final_box.write('\n')
			except Exception as e:
					print(filename, e)
