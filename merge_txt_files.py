# print(result)
# filenames = ["./new_data/train_image.txt", "./old_dataset/train_image.txt", "./united/train_image.txt"]
# filenames = ["./train_image.txt", "./data/engine/sample_train_image.txt", "./data/date/sample_train_image.txt"]
# filenames = ['./FW/train.txt', './TW/train.txt']
filenames = ['./train_image.txt', './sample_train_image.txt']

with open("./train_image_final.txt", "w") as outfile:
    for filename in filenames:
        with open(filename) as infile:
            contents = infile.read()
            outfile.write(contents)
            # outfile.write('\n----------------')

# labels = []
# with open('./train.txt') as t, open("labels_final.txt", "w") as outfile:
# 	for idx, line in enumerate(t):
# 		line = line.strip()
# 		if line == "":
# 			continue
# 		else:
# 			# row = re.split('\s+',line)
# 			row = line.split("\t")
# 			# print(row[1])
# 			labels.append(row[1])
# 	# print(labels)
# 	for lab in set(labels):
# 		outfile.write(f"{lab}\n")