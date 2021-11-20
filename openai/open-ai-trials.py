import openai
import os

openai.api_key = "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"
response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)
