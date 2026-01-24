# MQTT + LLM integration

## Project description

This hw assignment demonstrates a basic MQTT publish/subscribe workflow extended with an LLM.  
A publisher sends sample sensor data to an MQTT topic, and a subscriber listens for incoming messages.  
When a message is received, the subscriber sends the payload to an OpenAI LLM, which generates a brief analysis of the sensor data and prints the result to the console.

## Setup and Installation

### Requirements
- Python 3.x
- An OpenAI API key

## Install dependencies

```
pip install paho-mqtt openai python-dotenv
```
## Configure openAI API key
- Create a .env file in the project directory with the following content:   
OPEN_API_KEY=sk-xxxxxxxxxxxxxx
- Place .env in .gitignore file prior to pushing


## Run Publisher (in primary terminal)

```
python pub.py
```

## Run Subscriber (in secondary terminal)

```
python sub.py
```

# Example Usage

1) Start the subscriber in one terminal:
```
python sub.py
```

2) Start the publisher in a second terminal:
```
python pub.py
```

3) When a message is published:
- The sub prints the raw MQTT payload
- The payload is sent to the LLM
- The LLM generates an analysis of the sensor data
- The analysis is printed to the console

## Example output:
Received message on topic pythontest/sensors/mysensor: {"temperature": 22.5, "humidity": 55}  

--- LLM response ---  
The temperature and humidity values appear to be within a normal indoor range...  
--- end ---
