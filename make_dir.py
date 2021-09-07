import os
child_dir = "dev"
parent_dir = "/home/alethea/Downloads"
final_dir = parent_dir + child_dir
print(final_dir)
os.mkdir(final_dir)
path_1 = os.path.join(parent_dir, child_dir)
print("path_1",path_1)
try:
	os.mkdir(path_1)
	print("Directory '%s' created successfully" %child_dir)
except OSError as er:
	print("error",er)
