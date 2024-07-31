#!/usr/bin/env python3

# ask ChatGPT in the Terminal

my_api_key = 'sk-***'

from os.path import basename
from prompt_toolkit import prompt
from sys import argv, exit
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

# question
myname = basename(argv.pop(0))
question = '\x20'.join(argv)
while not question:
    try: question = prompt('Q: ')
    except KeyboardInterrupt:
        print()
        exit('interrupted')

# api args
client = OpenAI(api_key=my_api_key)
gpt_model = 'gpt-4o'
customized = 'You are a scientist, give formal answers. \
    Tell me, if you are not sure. It is very important that your \
    answer is correct!' # begging helps
temp = 0.2 # will make it more focused and deterministic

# call api
try:
    completion = client.chat.completions.create(
      model=gpt_model,
      temperature=temp,
      messages=[
        {'role': 'system', 'content': customized},
        {'role': 'user', 'content': question}
      ]
    )

    real_model = str(completion.model)
    answer = str(completion.choices[0].message.content)

    # formatting
    console = Console()
    markdown = Markdown(answer)
    print(); print('Model: ', real_model); print(); console.print(markdown); print()
    exit(0)

except Exception as e:
    exit(str(e))
