# /usr/bin/env/python3.9

import os
from sys import argv


def get_unit(bytesize):
	size =	bytesize \
			if bytesize < 1000 else bytesize / 1000 \
			if bytesize < 1000000 else bytesize / 1000000 \
			if bytesize < 1000000000 else bytesize / 1000000000

	unit =	"Bytes" \
			if bytesize < 1000 else "KB" \
			if bytesize < 1000000 else "MB" \
			if bytesize < 1000000000 else "GB"

	return size, unit


if __name__ == "__main__":
	
	errmsg = f"Usage: python {argv[0]} <target-name> <directory>" 
	
	if len(argv) < len(errmsg.split(" ")[2:]):
		exit( errmsg )

	target = argv[1]
	targetdir = argv[2]

	orgdir = os.getcwd()

	try:
		os.chdir( targetdir )
	except Exception as e:
		exit(e)

	filetree = os.walk( os.getcwd() )

	targets = size = 0

	for dirpath, _, filenames in filetree:
		if target not in filenames:
			continue

		targets += 1

		size += os.stat( os.path.join(dirpath, target) ).st_size

	relsize, unit = get_unit(size)

	print( f"\n{relsize} {unit} in {targets} files of target name \'{target}\'. \n" )
	
	relsize, unit = get_unit(size / targets)
	
	print( f"Average size per person; {round(relsize, 2)} {unit}. \n" )

	os.chdir( orgdir )
