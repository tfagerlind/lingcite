.PHONY: run-lambda run-api make-check spell-check test

update-function-code:
	zip handler.zip handler.py
	aws lambda update-function-code --function-name myGreatFunction --zip-file fileb://handler.zip

run-lambda:
	aws lambda invoke --function-name myGreatFunction --payload file://myinput.txt outputfile.txt --cli-binary-format raw-in-base64-out
	cat outputfile.txt

run-api:
	curl https://xnuxfk1601.execute-api.eu-north-1.amazonaws.com/test/lingcite

make-check:
	docker run --rm -v $(CURDIR):/data cytopia/checkmake Makefile

spell-check:
	docker run --rm -v $(CURDIR):/workdir -it \
			tmaier/markdown-spellcheck:latest \
				--ignore-numbers -r "**/*.md"

test: make-check spell-check
