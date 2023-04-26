import argparse
import sys
import os
import PyPDF2

import pdb
br = pdb.set_trace

def build_args():
    desc = '''
    Usage 1: python gptcoach.py list    
    Usage 2: python gptcoach.py gen -p post --pdf pdf/hkg18-402-180328091217.pdf -t "HKG18-402: Secure Key Services in OP-TEE" -o out 
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
            help='A name of prompt. E.g., post') 

    parser.add_argument(
            '--pdf',
            dest='pdf',
            help='A PDF file')       

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

BREAK_LINE_NUM = 1
def break_line():
    global BREAK_LINE_NUM

    line = '-' * 70
    line = f'-------- {BREAK_LINE_NUM} {line}'
    BREAK_LINE_NUM += 1

    return line

def handle_gen_post(args):

    if not os.path.exists('prompts'):
        print('Error. The directory does not exist.')
        print('prompts')
        sys.exit(1)

    prompt_fn = os.path.join('prompts', f'{args.prompt}.txt')
    if not os.path.exists(args.pdf):
        print('Error. The file does not exist.')
        print(prompt_fn)
        sys.exit(1)

    if not os.path.exists(args.pdf):
        print('Error. The file does not exist.')
        print(args.pdf)
        sys.exit(1)

    if not os.path.exists(args.output):
        print(f'Make {args.output}')
        os.mkdir(args.output)

    out_fn = os.path.basename(args.pdf)
    out_fn, _ = os.path.splitext(out_fn)
    out_fn = os.path.join(args.output, f'{out_fn}.txt')


    print(f'Reading {args.pdf}')
    print(f'Writing {out_fn}')


    fw = open(out_fn, 'w', encoding='utf-8')

    f = open(prompt_fn, 'r', encoding='utf-8')
    for line in f:
        fw.write(line)
    f.close()

    fw.write('\n')
    fw.write(break_line())
    fw.write('\n')

    fw.write(f'post-begin: {args.title}\n')
    fw.write('\n')    

    f = open(args.pdf, 'rb')
    pdf_reader = PyPDF2.PdfReader(f)

    count_text_ls = []
    acc = 0
    limit = 1000
    #limit = 100

    train_seq = [0, 0, 1, 1, 1, 2, 2, 2, 2]
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        count = len(text.split())
        acc += count
        idx = acc//limit
        idx2 = idx 
        if page_num < len(train_seq):
            idx2 = train_seq[page_num] + idx
            max_idx2 = idx2  
        else:
            idx2 = max_idx2 + idx + 1

        count_text_ls.append((count, acc, idx, idx2, text))
    
    idx_text_ls_d = {}
    for count, acc, idx, idx2, text in count_text_ls:
        print('%4d, %4d, %4d, %4d' % (count, acc, idx, idx2))
        if idx2 not in idx_text_ls_d:
            idx_text_ls_d[idx2] = [] 

        idx_text_ls_d[idx2].append(text)

    page_num = 1
    for idx, text_ls in idx_text_ls_d.items():
        fw.write(break_line())
        fw.write('\n')
        fw.write('post-pages:\n')
        fw.write('\n')

        for text in text_ls:
            fw.write(f'Page {page_num}:')
            fw.write('\n\n')
            fw.write(text)
            fw.write('\n\n')
            page_num += 1

    fw.write(break_line())
    fw.write('\n')
    fw.write('post-end:')
    fw.write('\n\n')   

    f.close() 
    fw.close()


def handle_gen(args):
    if args.prompt == 'post':
        handle_gen_post(args)
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



