# ChatGptAnswerPdf
The project lets ChatGPT (for GPT-4) learn the commands you define.

## gptcoach.py

The app generates prompts to teach ChatGPT (for GPT-4) the commands you define.

## Usage

List all supported prompts
```
% python gptcoach.py list
Supported prompts:
    gen
```

Generate the post prompt that teaches ChatGPT to read a PDF document.
```
% python gptcoach.py gen \
    -p post \
    --pdf pdf/hkg18-402-180328091217.pdf \
    -t "HKG18-402: Secure Key Services in OP-TEE" \
    -o out 
```
