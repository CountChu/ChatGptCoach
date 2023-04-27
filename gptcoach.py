import argparse
import sys

from core import util
from core import gen_post_doc
from core import gen_post_subtitle

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
    print('    gen')

def handle_gen(args):

    prompt_fn = util.get_prompt(args.prompt)

    if args.prompt == 'post-doc':
        gen_post_doc.handle(args, prompt_fn)

    elif args.prompt == 'post-subtitle':
        gen_post_subtitle.handle(args, prompt_fn)

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



