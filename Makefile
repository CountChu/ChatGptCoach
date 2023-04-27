post-doc:
	python gptcoach.py gen \
		-p post-doc \
		--pdf pdf/hkg18-402-180328091217.pdf \
		-t "HKG18-402: Secure Key Services in OP-TEE" \
		-o out-doc

post-subtitle:
	python gptcoach.py gen \
		-p post-subtitle \
		--txt subtitle/6Nwtlxbtujs.txt \
		-t "HKG18-402: Secure Key Services in OP-TEE" \
		-o out-subtitle
