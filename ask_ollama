#!/usr/bin/venv python3

# ask the Ollama API

model = 'gemma2'
#model = 'llama3.1'

from os.path import basename
from prompt_toolkit import prompt
from sys import argv, exit
from requests import post
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
url = 'http://localhost:11434/api/generate'
data = {
    'model':    model,
    'prompt':   question,
    'options':  {'temperature': 0.2},
    'stream':   False
}

# call api
try:
    response_obj = post(url, json=data)

    response_json = response_obj.json()
    real_model = response_json['model']
    answer = response_json['response']

    # formatting
    console = Console()
    markdown = Markdown(answer)
    print(); print('Model: ', real_model); print(); console.print(markdown); print()
    exit(0)

except Exception as e:
    exit(str(e))
