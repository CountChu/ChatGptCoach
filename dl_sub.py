#
# FILENAME.
#       dl_sub.py - Download Subtitle Python App.
#
# FUNCTIONAL DESCRIPTION.
#       A python application downloads subtitles of a video from YouTube.
#       The video is specified by video ID (E.g., 6Nwtlxbtujs).
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2023/4/28
#

import argparse
import os
import json
from youtube_transcript_api import YouTubeTranscriptApi
import pdb  
from core import util

br = pdb.set_trace

def build_args():
    desc = '''
    Usage 1: 
        python dl_sub.py -v 6Nwtlxbtujs -o subtitle
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
            '-v',
            dest='video_id',
            help='A video id in YouTube. E.g., 6Nwtlxbtujs') 

    parser.add_argument(
            '-o',
            dest='output',
            help='An output directory') 
    
    #
    # Check arguments.
    #

    args = parser.parse_args()

    return args

def seconds_to_hh_mm_ss(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


def main():

    #
    # Read arguments.
    #

    args = build_args()

    #
    # Check output directory. If not exist, make it.
    #

    util.check_dir_exist_make(args.output) 

    #
    # Download subtitle.
    #

    st_ls = YouTubeTranscriptApi.get_transcript(args.video_id)


    fn = os.path.join(args.output, f'{args.video_id}.txt')
    print(f'Writing {fn}')
    f = open(fn, 'w')

    for st in st_ls:
        start = st['start']
        text = st['text']
        hh, mm, ss = seconds_to_hh_mm_ss(start)
        if hh == 0:
            f.write('[%02d:%02d] %s\n' % (mm, ss, text))
        else:
            f.write('[%d:%02d:%02d] %s\n' % (hh, mm, ss, text))

    f.close()

if __name__ == '__main__':
    main()