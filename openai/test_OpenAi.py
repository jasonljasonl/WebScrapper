from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write hello",
  store=True,
)

print(response.output_text)
