"""This file implements the AWS Lambda entry of LingCite."""
import json
import logging
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
    print(f"print event: {event}")
    print(f"print context: {context}")

    raw_body = event['body']
    body = json.loads(raw_body)
    citation = body['payload']['human-readable']
    output = lingcite.gramcite.bibtex(citation)
    return {
        "statusCode": 200,
        "body": json.dumps({"bibtex": output})
    }
