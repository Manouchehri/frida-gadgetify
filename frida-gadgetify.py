#!/usr/bin/env python2
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

	# Assuming a valid section exists... I really should be using segments
	injected_tag = binary.dynamic_entry_from_tag(lief.ELF.DYNAMIC_TAGS.NULL)
	# @TODO: Create a section if none exists

	# Change the tag type
	injected_tag.tag = lief.ELF.DYNAMIC_TAGS.NEEDED
	injected_tag.value = 0 # Should already be zero

	# Write to a temp file and reload the binary with the modified tag.
	temp_filename = next(tempfile._get_candidate_names())
	temp_directory = tempfile._get_default_tempdir()
	temp_full_path = "" + temp_directory + "/" + temp_filename
	binary.write(temp_full_path)
	new_binary = lief.parse(temp_full_path)
	os.remove(temp_full_path)

	# Fetch the first NEEDED tag (which has a duplicate at the end)
	injected_tag = new_binary.dynamic_entry_from_tag(lief.ELF.DYNAMIC_TAGS.NEEDED)

	# @TODO: Grow the .dynstr size properly.
	injected_tag.name = frida_filename

	# (•_•) ( •_•)>⌐■-■ (⌐■_■)
	new_binary.write(output_filename)
	print("Injected binary successfully written to " + output_filename + "!")
	print("")
	print(frida_filename + " must be in your LD_LIBRARY_PATH.")
	print("Example:")
	print("LD_LIBRARY_PATH=/home/dave/libs/ " + output_filename)

if __name__ == '__main__':
	main()
