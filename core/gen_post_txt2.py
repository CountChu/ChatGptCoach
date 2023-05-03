import os
import pdb
import yaml
from core import util

br = pdb.set_trace

def handle(args, prompt_fn):

    f = open(prompt_fn)
    y = yaml.load(f, Loader=yaml.loader.SafeLoader)
    f.close()

    util.check_file_exist(args.txt)

    util.check_dir_exist_make(args.output)

    out_fn = os.path.basename(args.txt)
    out_fn, _ = os.path.splitext(out_fn)
    out_fn = os.path.join(args.output, f'{out_fn}.prompt.txt')    

    print(f'Reading {args.txt}')
    print(f'Writing {out_fn}')    

    fw = open(out_fn, 'w', encoding='utf-8')

    fw.write(y['post_begin'].format(title=args.title))
    fw.write('\n')    

    f = open(args.txt, 'r', errors='ignore')

    #
    # count_text_ls.
    #    

    limit = 1500
    count_text_ls = []
    acc = 0
    for text in f:
        count = len(text.split())
        acc += count
        idx = acc//limit
        count_text_ls.append((count, acc, idx, text))    
        
    #
    # Build idx_text_ls_d.
    #
    
    idx_text_ls_d = {}
    for count, acc, idx, text in count_text_ls:    
        print('%4d, %4d, %4d, %s' % (count, acc, idx, text.strip()))
        if idx not in idx_text_ls_d:
            idx_text_ls_d[idx] = [] 

        idx_text_ls_d[idx].append(text)

    part_max = len(idx_text_ls_d)
    for idx, text_ls in idx_text_ls_d.items():
        fw.write(util.break_line())
        fw.write('\n')
        fw.write(y['text_begin'].format(num=idx+1, max=part_max))
        fw.write('\n')        
        for text in text_ls:
            fw.write(text)  
        fw.write(y['text_end'].format(num=idx+1, max=part_max))
        fw.write('\n')
        fw.write('\n')
        fw.write(y['hint'].format(num=idx+1, max=part_max))
        fw.write('\n')
        fw.write('\n')

    fw.write(util.break_line())
    fw.write('\n')
    fw.write(y['post_end'])
    fw.write('\n\n')  

    fw.close()
