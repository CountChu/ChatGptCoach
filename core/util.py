import os
import sys

def check_file_exist(fn):
    if not os.path.exists(fn):
        print('Error. The file does not exist.')
        print(fn)
        sys.exit(1)

def check_dir_exist(dn):
    if not os.path.exists(dn):
        print('Error. The directory does not exist.')
        print(dn)
        sys.exit(1)

def get_prompt(prompt):
    if prompt not in ['post-doc', 'post-subtitle']:
        return None

    check_dir_exist('prompts')

    out = os.path.join('prompts', f'{prompt}.txt')
    check_file_exist(out)

    return out

def check_dir_exist_make(dn):
    if not os.path.exists(dn):
        print(f'Make {dn}')
        os.mkdir(dn)

def write_whole_file(fw, fn):
    f = open(fn, 'r', encoding='utf-8')
    for line in f:
        fw.write(line)
    f.close()

BREAK_LINE_NUM = 1
def break_line():
    global BREAK_LINE_NUM

    line = '-' * 70
    line = f'-------- {BREAK_LINE_NUM} {line}'
    BREAK_LINE_NUM += 1

    return line

