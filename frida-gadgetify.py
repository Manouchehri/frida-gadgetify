#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: David Manouchehri

import lief
import argparse
import tempfile
import os

def main():
	parser = argparse.ArgumentParser(description="gadgetify")
	parser.add_argument('-V', '--version', action="version", version="%(prog)s 0.1")
	parser.add_argument("-i", action="store", dest="input_filename", required=True, help="input filename")
	parser.add_argument("-o", action="store", dest="output_filename", help="output filename")
	parser.add_argument("-l", action="store", dest="frida_filename", default="frida-gadget.so", help="frida-gadget filename")

	args = parser.parse_args()

	output_filename = args.output_filename
	if output_filename is None:
		output_filename = args.input_filename + ".out"

	input_filename = args.input_filename
	frida_filename = args.frida_filename

	binary = lief.parse(input_filename)

	binary.add_library(frida_filename)

	# (•_•) ( •_•)>⌐■-■ (⌐■_■)
	binary.write(output_filename)
	print("Injected binary successfully written to " + output_filename + "!")
	print("")
	print(frida_filename + " must be in your LD_LIBRARY_PATH.")
	print("Example:")
	print("LD_LIBRARY_PATH=/home/dave/libs/ " + output_filename)

if __name__ == '__main__':
	main()
