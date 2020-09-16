#!/usr/bin/env python
#author: David Louis

#from sys import argv
import argparse	#contains argv, but command changes to sys.argv
#import getopt


#arguements
'''
program --file = fastq file that will be converted to fasta

- open file
- 

'''

################ functions ##############
#opens a fastq file and converts it into a fasta file
def fastq2fasta():
	fastq = open(args.file)
	with fastq as fastq_file:         #opens the file and stores it
		for header in fastq_file:               #creates a loop storing every variable as header
                        if header.startswith('@M'):      #if the lines starts with @ do....
                                print(header.replace('@', '>').rstrip())        #.replace is a regex
                                print(next(fastq_file).rstrip())        #next prints next line, .rstrip() removes trailing characters
	fastq.close()           #closes file

#def usage()
#	print("\nUsage: Convert fastq file into a fasta file\n")
#	print("Example:")
#	print(" --file file.fastq")
#	print("or")
#	print(" -f file.fastq\n")#  fastq file that will be converted into fasta\n")

############## parsing ##############
parser = argparse.ArgumentParser(description='converts Fastq file to Fasta file')

parser.add_argument('-f', '--file', required=True, metavar='', help='input FASTQ file to be converted to FASTA')
args=parser.parse_args()

############## main code ############

fastq2fasta()











