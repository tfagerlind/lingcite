# Build test container
build:
    docker build -f Dockerfile.dev -t lingcite.dev --progress plain .
    docker build -f Dockerfile.prod -t lingcite.prod --progress plain .

# Deploy application to AWS cloud
tmpdir  := `mktemp -d`
deploy: build
    docker run --rm -v "{{tmpdir}}:/build" -e HANDLER=/build/handler.zip lingcite.prod ./create-package.sh
    aws lambda update-function-code --function-name myGreatFunction \
        --zip-file fileb://{{tmpdir}}/handler.zip

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
    docker run --rm -v "${PWD}:/workdir" -t \
        tmaier/markdown-spellcheck:latest \
            --ignore-numbers -r "**/*.md"

# Check markdown files
check-markdown:
    docker run --rm -v $(pwd):/work tmknom/markdownlint -- .

# Check python files
check-python: build
    docker run -t --rm -v "${PWD}:/apps" alpine/flake8:6.0.0 src/handler.py src/lingcite tests
    docker run --rm lingcite.dev python -m pylint src/handler.py

# Check docker file
check-dockerfile:
    docker run --rm -i hadolint/hadolint < Dockerfile.prod
    docker run --rm -i hadolint/hadolint < Dockerfile.dev

# Check json files
check-json:
    docker run --rm -v "${PWD}:/data" cytopia/jsonlint -t '  ' *.json

check-shell:
    docker run --rm -v "${PWD}:/mnt" koalaman/shellcheck:stable create-package.sh

# Check yaml files
check-yaml:
    docker run --rm -v "${PWD}:/data" cytopia/yamllint .

# Run functional tests
run-functional-tests: build
    docker run --rm lingcite.dev pytest -vv -p no:warnings

# Test and check everything
test: check-spelling check-markdown check-python check-dockerfile check-json check-shell check-yaml run-functional-tests
