#!/usr/bin/python3.12

import glob
from srt_to_vtt import srt_to_vtt

def main():
    input_file_directory = input("Input directory path (all files inside directory will be converted): ")
    #finds all srt files in directory and makes a list
    input_files = glob.glob(f"{input_file_directory}/*.srt")
    #counts the number of files
    num_files = len(input_files)
    #converts each file in list
    for input_file in input_files:
        output_file = input_file.replace(".srt", ".vtt")
        srt_to_vtt(input_file, output_file)
    print(f"Successfully converted {num_files} files")
    return (output_file)

#run main function
main()
