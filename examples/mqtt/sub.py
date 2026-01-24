# subscriber.py
import paho.mqtt.client as mqtt
import time
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# create client
openai_client = None
if os.getenv("OPENAI_API_KEY"):
    openai_client = OpenAI()

def run_llm(prompt: str) -> str:
    """Call OpenAI and return text response."""
    if openai_client is None:
        return "OpenAI not configured. Set OPENAI_API_KEY to enable LLM output."

    resp = openai_client.responses.create(
        model="gpt-5.2",
        input=prompt
    )
    return resp.output_text
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        # Subscribe to topic
        client.subscribe("pythontest/sensors/mysensor")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

    prompt = f"Generate an analysis of this sensor data:\n\n{payload}"


   # print LLM response
    try:
        llm_response = run_llm(prompt)
        print("\n--- LLM response ---")
        print(llm_response)
        print("--- end ---\n")
    except Exception as e:
        print(f"LLM call failed: {type(e).__name__}: {e}")

# Create subscriber client
subscriber = mqtt.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Connect to public broker
print("Connecting to broker...")
subscriber.connect("test.mosquitto.org", 1883, 60)

# Start the subscriber loop
subscriber.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping subscriber...")
    subscriber.loop_stop()
    subscriber.disconnect()
