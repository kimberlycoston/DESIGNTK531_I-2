import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("Set OPENAI_API_KEY first.")

client = OpenAI()

resp = client.responses.create(
    model="gpt-5.2",
    input="Explain MQTT."
)

print(resp.output_text)
