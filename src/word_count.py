
import os
from sys import argv


def walkerror(oserr, *_):
	exit( oserr )

def targetpaths(target):
	""" Return list of full paths to any filename matching targetname. """

	paths = []

	for dirpath, _, filenames in os.walk( os.getcwd() ):
		if target not in filenames:
			continue
	
		paths.append( os.path.join(dirpath, target) )

	return paths

def wordcount(path):
	""" Return dictionary with keys and values as words in target-path and their occurrences. """

	wc = {}

	with open(path, "r") as f:
		lines = f.readlines()

	for line in lines:
		# From text to list of words separated by whitespace, without newline. 
		line = line.strip("\n").split(" ")

		for word in line:
			word = word.lower()

			if word not in wc.keys():
				wc[word] = 0

			else:
				wc[word] += 1

	return wc


if __name__ == "__main__":
	
	errmsg =f"Usage: python {argv[0]} <target-name> <directory>"
	
	if len(argv) < len(errmsg.split(" ")[2:]):
		exit(errmsg)

	target = argv[1]
	targetdir = argv[2]

	orgdir = os.getcwd()
	os.chdir( targetdir )

	paths = targetpaths( target )
	targets = len(paths)
	count = 0
	

	for path in paths:
		# Sum up values in return dict and add to cumulative word-count. 
		count += sum( wordcount( path ).values() )
	
	msg = f"Word-Count: {count} in {targets} files. \n"
	msg += f"Average words/person: {count / targets} "

	print(msg)

	os.chdir( orgdir )
