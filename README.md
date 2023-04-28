# ChatGptAnswerPdf
The project lets ChatGPT (for GPT-4) learn the commands you define.

# Applications

## gptcoach.py

The app generates prompts to teach ChatGPT (for GPT-4) the commands you define.

## dl_sub.py

The app downloads subtitles of a video from YouTube. The video is specified by video ID (E.g., 6Nwtlxbtujs).

# Usage

List all supported prompts
```
% python gptcoach.py list
Supported prompts:
    post-doc
    post-subtitle
```

Generate the post-doc prompt that teaches ChatGPT to read a PDF document.
```
% python gptcoach.py gen \
    -p post-doc \
    --pdf pdf/hkg18-402-180328091217.pdf \
    -t "HKG18-402: Secure Key Services in OP-TEE" \
    -o out-doc 
```

Download subtitles of the video (video ID: 6Nwtlxbtujs) from YouTube in the subtitle directory.
```
% python dl_sub.py -v 6Nwtlxbtujs -o subtitle
```

Generate the post-subtitle prompt that teaches ChatGPT to read subtitles of a video.
```
% python gptcoach.py gen \
    -p post-subtitle \
    --txt txt/6Nwtlxbtujs.txt \
    -t "HKG18-402: Secure Key Services in OP-TEE" \
    -o out-subtitle 
```
