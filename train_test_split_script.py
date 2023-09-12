import pandas as pd
import os
import re


from random import sample
import random
with open("./train_image.txt") as final_image:
	image_list = [trn_img_path.strip().split('\t')[-1] for trn_img_path in final_image]
	random.shuffle(image_list)
	filter_img = sample(image_list, 100)

with open("./train.txt") as final_train, open("./train_box.txt") as final_box, open("./train_image.txt") as final_image, open("./test_image.txt", 'w') as sample_image, open("./test.txt", 'w') as sample_lab, open("./test_box.txt", 'w') as sample_box, \
	open("./train_.txt", 'w') as train_lab, open("./train_box_.txt", 'w') as train_box, open("./train_image_.txt", 'w') as train_image:
	# image_list =  [trn_img_path.strip().split('\t')[-1] for trn_img_path in final_image]
	# filter_img = sample(image_list, 80)
	# print(filter_img[:5])
	flag = False
	count = 1
	for trn, trn_img, trn_box in zip(final_train, final_image, final_box):
		# print(trn, trn_img, trn_box)
		trn = trn.strip()
		trn_box = trn_box.strip()
		trn_img = trn_img.strip()
		if trn_img.split("\t")[-1] in filter_img:
			flag = True
			trnline = trn.split("\t")
			boxline = trn_box.split("\t")
			imgline = trn_img.split("\t")

			sample_lab.write(f'{trnline[0]}\t{trnline[1]}\n')
			sample_box.write(f'{boxline[0]}\t{boxline[1]}\n')
			sample_image.write(f'{imgline[0]}\t{imgline[1]}\t{imgline[2]}\t{imgline[3]}\n')
		else:
			# print(trn_img.split("\t")[-1])
			if trn == "" and trn_img == "" and trn_box == "" and flag:
				sample_box.write("\n")
				sample_lab.write("\n")
				sample_image.write("\n")
				flag= False
				print(count)
				count+= 1
			elif trn == "" and trn_img == "" and trn_box == "" and not flag:
				train_box.write("\n")
				train_lab.write("\n")
				train_image.write("\n")
				# count = 0
			else:
				trnline = trn.split("\t")
				boxline = trn_box.split("\t")
				imgline = trn_img.split("\t")

				train_lab.write(f'{trnline[0]}\t{trnline[1]}\n')
				train_box.write(f'{boxline[0]}\t{boxline[1]}\n')
				train_image.write(f'{imgline[0]}\t{imgline[1]}\t{imgline[2]}\t{imgline[3]}\n')

			


			





