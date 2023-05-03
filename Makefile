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

post-doc-3:
	python gptcoach.py gen \
		-p post-doc \
		--pdf pdf/lvc21-215.pdf \
		-t "LVC21-215 PKCS#11 in OP-TEE" \
		-o out-doc

post-doc-4:
	python gptcoach.py gen \
		-p post-doc \
		--pdf pdf/sfo15-503-securestorageinop-tee.pdf \
		-t "SFO15-503 Secure storagein OP-TEE" \
		-o out-doc		

post-doc-5:
	python gptcoach.py gen \
		-p post-doc \
		--pdf "pdf/LAS16-504 - Secure Storage updates in OP-TEE.pdf" \
		-t "LAS16-504 - Secure Storage updates in OP-TEE" \
		-o out-doc	

download-subtitle-1:
	python dl_sub.py -v 6Nwtlxbtujs -o subtitle

download-subtitle-2:
	python dl_sub.py -v VxBEQdu1T7A -o subtitle	

download-subtitle-3:
	python dl_sub.py -v pChEdObYLRM -o subtitle	

download-subtitle-4:
	python dl_sub.py -v 9OEt4aG6V5w -o subtitle	

download-subtitle-5:
	python dl_sub.py -v k61PiuFrc_U -o subtitle
			
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

post-subtitle-3:
	python gptcoach.py gen \
		-p post-subtitle \
		--txt subtitle/VxBEQdu1T7A.refine.txt \
		-t "LVC21-215 PKCS#11 in OP-TEE" \
		-o out-subtitle		

post-subtitle-4:
	python gptcoach.py gen \
		-p post-subtitle \
		--txt subtitle/9OEt4aG6V5w.refine.txt \
		-t "LAS16-504 Secure Storage updates in OP-TEE" \
		-o out-subtitle

sub2txt-4:
	python sub2txt.py \
		-i subtitle/9OEt4aG6V5w.refine.txt \
		-o txt  

sub2txt-5:
	python sub2txt.py \
		-i subtitle/k61PiuFrc_U.refine.txt \
		-o txt 

		

post-txt-4:
	python gptcoach.py gen \
		-p post-txt \
		--txt txt/9OEt4aG6V5w.refine.txt \
		-t "LAS16-504 Secure Storage updates in OP-TEE" \
		-o out-txt

post-txt2-4:
	python gptcoach.py gen \
		-p post-txt2 \
		--txt txt/9OEt4aG6V5w.refine.txt \
		-t "LAS16-504 Secure Storage updates in OP-TEE" \
		-o out-txt2

post-txt2-5:
	python gptcoach.py gen \
		-p post-txt2 \
		--txt txt/k61PiuFrc_U.refine.txt \
		-t "SFO17-309 Secure Storage Updates" \
		-o out-txt2
