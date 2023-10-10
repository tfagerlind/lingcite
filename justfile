# Deploy application to AWS cloud
deploy:
	zip handler.zip handler.py
	aws lambda update-function-code --function-name myGreatFunction --zip-file fileb://handler.zip

# Manually test API from the inside
run-lambda:
	aws lambda invoke --function-name myGreatFunction --payload file://myinput.txt outputfile.txt --cli-binary-format raw-in-base64-out
	cat outputfile.txt

# Manually test API from the outside
run-api:
	curl https://xnuxfk1601.execute-api.eu-north-1.amazonaws.com/test/lingcite

# Check spelling of markdown files
check-spelling:
    docker run --rm -v ${PWD}:/workdir -it \
        tmaier/markdown-spellcheck:latest \
            --ignore-numbers -r "**/*.md"

# Lint markdown files
check-markdown:
    docker run --rm -v $(pwd):/work tmknom/markdownlint -- .

check-python:
    docker run -ti --rm -v ${PWD}:/apps alpine/flake8:6.0.0 handler.py

# Check everything
check: check-markdown check-spelling check-python
