# Deploy application to AWS cloud
deploy:
    zip handler.zip handler.py
    aws lambda update-function-code --function-name myGreatFunction \
        --zip-file fileb://handler.zip

# Manually test API from the inside
run-lambda:
    aws lambda invoke --function-name myGreatFunction \
        --payload file://myinput.txt outputfile.txt \
        --cli-binary-format raw-in-base64-out
    cat outputfile.txt

# Manually test API from the outside
run-api:
    curl https://xnuxfk1601.execute-api.eu-north-1.amazonaws.com/test/lingcite

# Check spelling of markdown files
check-spelling:
    docker run --rm -v ${PWD}:/workdir -it \
        tmaier/markdown-spellcheck:latest \
            --ignore-numbers -r "**/*.md"

# Check markdown files
check-markdown:
    docker run --rm -v $(pwd):/work tmknom/markdownlint -- .

# Check python files
check-python:
    docker run -ti --rm -v ${PWD}:/apps alpine/flake8:6.0.0 handler.py src tests

# Check docker file
check-dockerfile:
    docker run --rm -i hadolint/hadolint < Dockerfile

# Check yaml files
check-yaml:
    docker run --rm -v ${PWD}:/data cytopia/yamllint .

# Run functional tests
run-functional-tests:
    docker build . -t lingcite
    docker run --rm lingcite pytest -vv -p no:warnings

# Test and check everything
test: check-markdown check-spelling check-python check-yaml check-dockerfile run-functional-tests
