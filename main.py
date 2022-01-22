import logging
import os
from dotenv import load_dotenv
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)

# Store conversation history
conversation_history = []
# ID of the channel you want to send the message to
channel_id = "C030FPGAX8Q"

try:
    # Call the conversations.history method using the WebClient
    # conversations.history returns the first 100 messages by default
    # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
    result = client.conversations_history(channel=channel_id)

    conversation_history = result["messages"]

    # Print results
    logger.info("{} messages found in {}".format(len(conversation_history), id))

    for con in conversation_history:
        print(con['text'])

except SlackApiError as e:
    logger.error("Error creating conversation: {}".format(e))
