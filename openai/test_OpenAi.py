import os

from openai import OpenAI

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write hello",
  store=True,
)

print(response.output_text)
