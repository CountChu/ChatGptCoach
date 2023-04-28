import os
import PyPDF2
from core import util

def handle(args, prompt_fn):
    util.check_file_exist(args.pdf)

    util.check_dir_exist_make(args.output)

    out_fn = os.path.basename(args.pdf)
    out_fn, _ = os.path.splitext(out_fn)
    out_fn = os.path.join(args.output, f'{out_fn}.prompt.txt')

    print(f'Reading {args.pdf}')
    print(f'Writing {out_fn}')

    fw = open(out_fn, 'w', encoding='utf-8')

    util.write_whole_file(fw, prompt_fn)

    fw.write('\n')
    fw.write(util.break_line())
    fw.write('\n')

    fw.write(f'doc-begin: {args.title}\n')
    fw.write('\n')    

    f = open(args.pdf, 'rb')
    pdf_reader = PyPDF2.PdfReader(f)

    #
    # count_text_ls.
    #

    count_text_ls = []
    acc = 0
    limit = 1000
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

    #
    # Build idx_text_ls_d.
    #
    
    idx_text_ls_d = {}
    for count, acc, idx, idx2, text in count_text_ls:
        print('%4d, %4d, %4d, %4d' % (count, acc, idx, idx2))
        if idx2 not in idx_text_ls_d:
            idx_text_ls_d[idx2] = [] 

        idx_text_ls_d[idx2].append(text)

    page_num = 1
    for idx, text_ls in idx_text_ls_d.items():
        fw.write(util.break_line())
        fw.write('\n')
        fw.write('doc-post:\n')
        fw.write('\n')

        for text in text_ls:
            fw.write(f'Page {page_num}:')
            fw.write('\n\n')
            fw.write(text)
            fw.write('\n\n')
            page_num += 1

        fw.write('\n')
        fw.write('// Please just accept my posted pages, don\'t response them, and don\'t repeat them.\n')
        fw.write('\n')            

    fw.write(util.break_line())
    fw.write('\n')
    fw.write('doc-end:')
    fw.write('\n\n')   

    f.close() 
    fw.close()
