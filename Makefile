.PHONY = update-function-code run-lambda

update-function-code:
	zip handler.zip handler.py
	aws lambda update-function-code --function-name myGreatFunction --zip-file fileb://handler.zip

run-lambda:
	aws lambda invoke --function-name myGreatFunction --payload file://myinput.txt outputfile.txt --cli-binary-format raw-in-base64-out
	cat outputfile.txt

run-api:
	curl https://xnuxfk1601.execute-api.eu-north-1.amazonaws.com/test/lingcite
