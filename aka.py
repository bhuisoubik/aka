from platform import system as osname
from sys import argv
from pathlib import Path
from os.path import join as Pjoin
from os.path import exists
from os.path import abspath
from os.path import splitext
from os.path import basename
from os import mkdir
from os import remove
from os import walk

script_type = ''
bin_path = Pjoin(str(Path.home()), ".aka.bin")

VERSION = '0.0.1'

if not exists(bin_path):
	mkdir(bin_path)

'''
check shell type from OS name
	batch for Windows
	bash for MacOS, Linux
'''
if osname() == "Windows":
	script_type = ".bat"
elif osname() == "Linux" or osname() == "Darwin":
	script_type = ".bash"

def help():
	print('''NAME
	aka - create alias for long-named executables or commnads

USAGE
	aka [OPTIONS] [ALIAS-NAME]...

OPTIONS
	-n, --new [ALIAS-NAME] [EXECUTABLE]
		Create a new alias
	-l, --list
		List all created aliases
	-s, --search [ALIAS-NAME]
		Check whether an alias already exists or not
	-r, --remove [ALIAS-NAME]
		Remove an existing alias
	-v, --version
		Print Version
	-h, --help
		Show this''')

def write_file(file, data):
	f = open(file, 'w')
	f.write(data)
	f.close()

def boilerplate(exec_name):
	if script_type == ".bat":
		return '@echo off\n' + exec_name + " %*"
	elif script_type == ".bash":
		return '#!/bin/bash\n' + exec_name + " $@"

def get_files(rootdir):
	file_paths = []

	for folder, subs, files in walk(rootdir):
		for filename in files:
			file_paths.append(abspath(Pjoin(folder, filename)))
	return file_paths


def main():
	try:
		if argv[1] == "-n" or argv[1] == "--new":
			if len(argv) > 3:
				file_name = Pjoin(bin_path, (argv[2] + script_type) if script_type == ".bat" else argv[2])
				data = boilerplate(argv[3])
				if exists(file_name):
					print("Alias already exists")
				else:
					write_file(file_name, data)
					print(f"Try running '{argv[2]}'")
			else:
				print('Argument expected\naka -n <alias-name> <exe-name>')
		elif argv[1] == "-l" or argv[1] == "--list":
			alias_filenames = get_files(bin_path)
			for i in range(0, len(alias_filenames)):
				x = alias_filenames[i]
				f = open(str(x), 'r+')
				alias_name = str(splitext(basename(x))[0])
				exec_name = str(f.read()).split('\n')[-1].split(' ')[0]
				print(f"{alias_name}\t\t-\t\t{exec_name}")
				f.close()
		elif argv[1] == "-s" or argv[1] == "--search":
			if len(argv) > 2:
				file_name = Pjoin(bin_path, (argv[2] + script_type) if script_type == ".bat" else argv[2])
				if exists(file_name):
					f = open(str(file_name), 'r+')
					alias_name = str(splitext(basename(file_name))[0])
					exec_name = str(f.read()).split('\n')[-1].split(' ')[0]
					print(f"{alias_name}\t\t-\t\t{exec_name}")
					f.close()
				else:
					print("alias not found")
			else:
				print('Argument expected\naka -s <alias-name>')
		elif argv[1] == "-r" or argv[1] == "--remove":
			if len(argv) > 2:
				file_name = Pjoin(bin_path, (argv[2] + script_type) if script_type == ".bat" else argv[2])
				if exists(file_name):
					remove(file_name)
					print("Alias removed successfully")
				else:
					print('alias not found')
			else:
				print('Argument expected\naka -r <alias-name>')
		elif argv[1] == "-h" or argv[1] == "--help":
			help()
		elif argv[1] == "-v" or argv[1] == "--version":
			print(f"aka - {VERSION}")
		else:
			print(f"Option '{argv[1]}' not found!\nTry running 'aka -h'")
	except IndexError:
		help()

main()
