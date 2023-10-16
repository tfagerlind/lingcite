"""This file implements the AWS Lambda entry of LingCite."""
import json
import logging
import sys

sys.path.insert(0, 'deps')

import lingcite.gramcite


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    """Handle lambda event.

    This is the main Lambda entry of LingCite.

    Under construction. Currently it doesn't do anything interesting.
    """

    logger.info("event: %s", str(event))
    logger.info("context: %s", str(context))
    print("print event: {}".format(str(event)))
    print("print context: {}".format(str(context)))

    input = event['body']['payload']['human-readable']
    output = lingcite.gramcite.bibtex(input)
    return {"bibtex": output}

    print("Should not happen")
