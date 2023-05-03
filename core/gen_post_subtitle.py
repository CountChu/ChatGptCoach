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

    fw.write(f'subtitle-begin: {args.title}\n')
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

    for idx, text_ls in idx_text_ls_d.items():
        fw.write(util.break_line())

        line_num = 0
        for text in text_ls:
            if line_num % 5 == 0:
                fw.write('\n')
                fw.write('subtitle-post: // The command posts subtitles of the video.\n')
                #fw.write('subtitle-post:\n')
                fw.write('\n')
            fw.write(text)  
            line_num += 1
        fw.write('\n')
        fw.write('// Please just accept my posted subtitles, don\'t response them, and don\'t repeat them.\n')
        fw.write('\n')

    fw.write(util.break_line())
    fw.write('\n')
    fw.write('subtitle-end: // The post is done. You just response the long of the video.')
    fw.write('\n\n')  

    fw.close()
