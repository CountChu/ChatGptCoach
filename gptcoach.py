#
# FILENAME.
#       gptcoach.py - GPT Coach Python App.
#
# FUNCTIONAL DESCRIPTION.
#       The app generates prompts to teach ChatGPT (for GPT-4) the commands you define.
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2023/4/26
#

import argparse
import sys
import os

from core import util
from core import gen_post_doc
from core import gen_post_subtitle
from core import gen_post_txt
from core import gen_post_txt2

import pdb
br = pdb.set_trace

def build_args():
    desc = '''
    Usage 1: 
        python gptcoach.py list    
    Usage 2: 
        python gptcoach.py gen 
            -p post-doc \\
            --pdf pdf/hkg18-402-180328091217.pdf \\
            -t "HKG18-402: Secure Key Services in OP-TEE" \\
            -o out-doc
    Usage 3: 
        python gptcoach.py gen \\ 
            -p post-subtitle 
            --txt txt/6Nwtlxbtujs.txt \\
            -t "HKG18-402: Secure Key Services in OP-TEE" \\
            -o out-subtitle  
    Ussage 4:
        python gptcoach.py gen \\
            -p post-txt \\
            --txt txt/9OEt4aG6V5w.refine.txt \\
            -t "LAS16-504 Secure Storage updates in OP-TEE" \\
        -   o out-txt
'''
    #
    # Build an ArgumentParser object to parse arguments.
    #

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Anonymous arguments.
    #

    parser.add_argument(
            'command',
            help='list, gen')

    #
    # Standard arguments.
    #    

    parser.add_argument(
            '-p',
            dest='prompt',
            help='A name of prompt. E.g., post-doc, post-subtitle') 

    parser.add_argument(
            '--pdf',
            dest='pdf',
            help='A PDF file')       

    parser.add_argument(
            '--txt',
            dest='txt',
            help='A TXT file')         

    parser.add_argument(
            '-t',
            dest='title',
            help='A title of a PDF file')

    parser.add_argument(
            '-o',
            dest='output',
            help='An output directory') 
    
    #
    # Check arguments.
    #

    args = parser.parse_args()

    return args

def handle_list(args):
    print('Supported prompts:')
    print('    post-doc')
    print('    post-subtitle')    
    print('    post-txt')    
    print('    post-txt2')

def handle_gen(args):

    util.check_dir_exist('prompts')

    prompt_fn_d = {
        'post-doc': 'post-doc.txt', 
        'post-subtitle': 'post-doc.txt', 
        'post-txt': 'post-txt.txt',
        'post-txt2': 'post-txt2-3.yaml',
        }

    prompt_fn = prompt_fn_d[args.prompt]
    prompt_fn = os.path.join('prompts', prompt_fn)
    util.check_file_exist(prompt_fn)

    if args.prompt == 'post-doc':
        gen_post_doc.handle(args, prompt_fn)

    elif args.prompt == 'post-subtitle':
        gen_post_subtitle.handle(args, prompt_fn)

    elif args.prompt == 'post-txt':
        gen_post_txt.handle(args, prompt_fn)

    elif args.prompt == 'post-txt2':
        gen_post_txt2.handle(args, prompt_fn)
    else:
        assert False, args.prompt    

def main():

    #
    # Read arguments.
    #

    args = build_args()

    #
    # Dispatch command
    #

    if args.command == 'list':
        handle_list(args)

    elif args.command == 'gen':
        handle_gen(args)
    
    else:
        assert False, args.command

if __name__ == '__main__':
    main()



