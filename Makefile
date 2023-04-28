post-doc-1:
	python gptcoach.py gen \
		-p post-doc \
		--pdf pdf/hkg18-402-180328091217.pdf \
		-t "HKG18-402: Secure Key Services in OP-TEE" \
		-o out-doc

post-doc-2:
	python gptcoach.py gen \
		-p post-doc \
		--pdf pdf/optee-sks-secure-ota-foundries-linuxdevbr-rsalveti.pdf \
		-t "Leveraging OP-TEE as a generic HSM via PKCS#11 for secure OTA" \
		-o out-doc

download-subtitle-1:
	python dl_sub.py -v 6Nwtlxbtujs -o subtitle

post-subtitle-1:
	python gptcoach.py gen \
		-p post-subtitle \
		--txt subtitle/6Nwtlxbtujs.txt \
		-t "HKG18-402: Secure Key Services in OP-TEE" \
		-o out-subtitle

post-subtitle-2:
	python gptcoach.py gen \
		-p post-subtitle \
		--txt subtitle/9s-HpoCUmdI.txt \
		-t "Leveraging OP-TEE as a generic HSM via PKCS#11 for secure OTA" \
		-o out-subtitle
