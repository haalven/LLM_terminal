#!/usr/bin/env python3

# ask gpt in the terminal

my_api_key = '<YOUR_API_KEY_HERE>'

from prompt_toolkit import prompt
from sys import exit
from openai import OpenAI

question = ''
while not question:
    try: question = prompt('Q: ')
    except KeyboardInterrupt:
        print()
        exit('interrupted')

client = OpenAI(api_key=my_api_key)
gpt_model = 'gpt-4o'
customized = 'You are a scientist, give short and formal answers. \
Tell me, if you are not sure. It is very important that your \
answer is correct!' # begging helps
temp = 0.2 # will make it more focused and deterministic
print()

try:
    completion = client.chat.completions.create(
      model=gpt_model,
      temperature=temp,
      messages=[
        {'role': 'system', 'content': customized},
        {'role': 'user', 'content': question}
      ]
    )

    real_model = completion.model
    answer = completion.choices[0].message.content
    print(real_model + ':\n' + answer)
    exit(0)

except Exception as e:
    exit(str(e))
