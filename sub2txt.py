#
# FILENAME.
#       sub2txt.py - Subtitle To TXT Python App.
#
# FUNCTIONAL DESCRIPTION.
#       A python application convert subtitles into TXT format.
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2023/5/2
#

import argparse
import os
import re
import pdb  
from core import util

br = pdb.set_trace

def build_args():
    desc = '''
    Usage 1: 
        python sub2txt.py -i subtitle/9OEt4aG6V5w.refine.txt -o txt
'''
    #
    # Build an ArgumentParser object to parse arguments.
    #

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Standard arguments.
    #    

    parser.add_argument(
            '-i',
            dest='input',
            help='A file name of the subtitle.. E.g., 9OEt4aG6V5w.refine.txt') 

    parser.add_argument(
            '-o',
            dest='output',
            help='An output directory') 
    
    #
    # Check arguments.
    #

    args = parser.parse_args()

    return args

def main():

    #
    # Read arguments.
    #

    args = build_args()

    #
    # Check file and directory.
    # 

    util.check_file_exist(args.input)
    util.check_dir_exist_make(args.output) 

    #
    # Assign out_fn
    # 

    out_fn = os.path.join(args.output, os.path.basename(args.input))

    #
    # Convert subtitles to TXT.
    #

    print(f'Reading {args.input}')
    print(f'Writing {out_fn}')

    f = open(args.input, encoding='utf-8')
    f_w = open(out_fn, 'w', encoding='utf-8')

    pattern = r'\[\d\d\:\d\d]\s+(.*)' 
    for line in f:
        group = re.match(pattern, line)
        if group == None:
            f_w.write('\n')
            continue 

        f_w.write(group[1]+'\n')

    f_w.close()
    f.close()


if __name__ == '__main__':
    main()