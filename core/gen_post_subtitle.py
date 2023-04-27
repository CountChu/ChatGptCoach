import os
from core import util

def handle(args, prompt_fn):
    util.check_file_exist(args.txt)

    util.check_dir_exist_make(args.output)

    out_fn = os.path.basename(args.txt)
    out_fn, _ = os.path.splitext(out_fn)
    out_fn = os.path.join(args.output, f'{out_fn}.prompt.txt')    

    print(f'Reading {args.txt}')
    print(f'Writing {out_fn}')    

    fw = open(out_fn, 'w', encoding='utf-8')

    util.write_whole_file(fw, prompt_fn)

    fw.write('\n')
    fw.write(util.break_line())
    fw.write('\n')    

    fw.write(f'doc-begin: {args.title}\n')
    fw.write('\n') 

    f = open(args.txt, 'r')

    #
    # count_text_ls.
    #    

    limit = 1000
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

    page_num = 1
    for idx, text_ls in idx_text_ls_d.items():
        fw.write(util.break_line())
        fw.write('\n')
        fw.write('subtitle-post:\n')
        fw.write('\n')

        for text in text_ls:
            fw.write(text)  
        fw.write('\n')

    fw.write(util.break_line())
    fw.write('\n')
    fw.write('subtitle-end:')
    fw.write('\n\n')  

    fw.close()
