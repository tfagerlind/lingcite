# LingCite

LingCite is a program that converts human readable citations to BibTeX
citations. It is deployed to AWS as a web service.

# Implementation

The web service consists of a front-end implemented by a static web page located
in an bucket. The back-end consists of a REST API hosted as a lambda service.

# Prerequisites

* curl
* docker
* make
* AWS command line interface

# How to test

There are currently no automatic tests...

# How to deploy

Ensure that you have the AWS rights to update function code to `myGreatFunction`
(the name of the AWS lambda function). Run

    make update-function-code

# How to manually test

Either call the API by using the AWS command line interface:

    make run-lambda

or call the API from the outside:

    make run-api
