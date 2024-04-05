import openai
from prompt import setup_prompt
from api_keys import gpt_api_key

openai.api_key = gpt_api_key 
messages = []

temp = 0.5
messages.append({"role": "system", "content": setup_prompt})
messages.append({"role": "user", "content": "hi, I'm working on some Multi-Armed Bandit Algorithms"})

response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages, temperature = temp)
reply = response["choices"][0]["message"]["content"]
messages.append({"role": "assistant", "content": reply})


while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages, temperature = temp)
    reply = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")

