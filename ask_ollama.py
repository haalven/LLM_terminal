#! /usr/bin/env python3

# ask the Ollama API

models = {
    'llama':      'llama3.2',
    'gemma':      'gemma3:4b',
    'uncensored': 'CognitiveComputations/dolphin-llama3.1:latest',
}

from os.path import basename
from prompt_toolkit import prompt
from sys import argv, exit
from requests import post
from rich.console import Console
from rich.markdown import Markdown
from json import dumps

# parameter
myname = basename(argv.pop(0))
if not argv:
    exit('usage: ' + myname + ' <model> [question?]\n'
         'models: ' + str(dumps(models, indent=2, ensure_ascii=False)))
model = argv.pop(0)
if model in models:
    model = models[model]
else:
    exit('model error: ' + model + ' not in '
         + str(dumps(models, indent=2, ensure_ascii=False)))
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
    print('>>>', data)
    response_obj = post(url, json=data)

    response_json = response_obj.json()
    real_model = response_json['model']
    answer = response_json['response']

    # formatting
    console = Console()
    markdown = Markdown(answer)
    print(); console.print(markdown); print()
    exit(0)

except Exception as e:
    exit(str(e))
