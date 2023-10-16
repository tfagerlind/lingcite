# Build test container
build:
    docker build . -t lingcite

# Deploy application to AWS cloud
deploy:
    rm -f handler.zip
    cd src && pip install -t deps -r ../requirements.prod.txt --upgrade && zip -r ../handler.zip lingcite handler.py deps
    aws lambda update-function-code --function-name myGreatFunction \
        --zip-file fileb://handler.zip

# Manually test API from the inside
run-lambda:
    aws lambda invoke --function-name myGreatFunction \
        --payload file://myinput-with-body.txt outputfile.txt \
        --cli-binary-format raw-in-base64-out
    cat outputfile.txt

# Manually test API from the outside
run-api:
    curl -X POST  \
        -H 'Content-Type: application/json' \
        -d @myinput.txt \
        https://xnuxfk1601.execute-api.eu-north-1.amazonaws.com/test/lingcite

# Check spelling of markdown files
check-spelling:
    docker run --rm -v ${PWD}:/workdir -t \
        tmaier/markdown-spellcheck:latest \
            --ignore-numbers -r "**/*.md"

# Check markdown files
check-markdown:
    docker run --rm -v $(pwd):/work tmknom/markdownlint -- .

# Check python files
check-python: build
    docker run -t --rm -v ${PWD}:/apps alpine/flake8:6.0.0 src/handler.py src/lingcite tests
    docker run --rm lingcite python -m pylint src/handler.py

# Check docker file
check-dockerfile:
    docker run --rm -i hadolint/hadolint < Dockerfile

# Check yaml files
check-yaml:
    docker run --rm -v ${PWD}:/data cytopia/yamllint .

# Run functional tests
run-functional-tests: build
    docker run --rm lingcite pytest -vv -p no:warnings

# Test and check everything
test: check-markdown check-spelling check-python check-yaml check-dockerfile run-functional-tests
