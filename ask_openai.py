#! /usr/bin/env python3

# ask ChatGPT in the Terminal

'''
put your API KEY in the .toml file
with the same filename as this command
'''

# models: https://openai.com/api
models = {
    '4o':  'gpt-4o',
    'o4':  'o4-mini',
    '4.1': 'gpt-4.1'
}


import sys, os, tomllib
from json import dumps
from prompt_toolkit import prompt
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown


# read a toml file
def read_configuration(my_dir, my_name):
    c_file = os.path.splitext(my_name)[0] +'.toml'
    c_path = os.path.join(my_dir, c_file)
    if not os.path.exists(c_path):
        print('config not found at: ' + c_path)
        return None
    try:
        with open(c_path, 'rb') as f:
            return tomllib.load(f)
    except:
        print('error reading toml: ' + c_path)
        return None

def main() -> int:
    # path, dir
    sys.argv.pop(0)
    my_path = os.path.abspath(__file__)
    my_dir  = os.path.dirname(my_path)
    my_name = os.path.basename(my_path)

    # load api key from toml
    config = read_configuration(my_dir, my_name)
    if not config:
        print('reading the config file failed')
        return 1
    try:
        my_api_key = str(config['my_api_key'].strip())
    except Exception as e:
        print('reading my_api_key failed')
        return 1
    if not my_api_key:
        print('my_api_key string is empty')
        return 1

    # question
    if not sys.argv:
        print('usage: ' + my_name + ' <model> [question?]\n'
            'models: ' + str(dumps(models, indent=2, ensure_ascii=False)))
        return 1
    model = sys.argv.pop(0)
    if model in models:
        model = models[model]
    else:
        print('model error: ' + model + ' not in '
            + str(dumps(models, indent=2, ensure_ascii=False)))
        return 1
    question = '\x20'.join(sys.argv)
    while not question:
        try: question = prompt('Q: ')
        except KeyboardInterrupt:
            print('\ninterrupted')
            return 1

    # api args
    client = OpenAI(api_key=my_api_key)
    customized = 'You are a scientist, give formal answers. \
        Tell me, if you are not sure. It is very important that your \
        answer is correct!' # begging helps
    temp = 0.2 # will make it more focused and deterministic

    # call api
    try:
        if model.startswith('o'):
            completion = client.chat.completions.create(
            model=model,
            messages=[
                {'role': 'user', 'content': question}
            ]
            )
        else:
            completion = client.chat.completions.create(
            model=model,
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
        return 0

    except Exception as e:
        print(e)
        return 1


if __name__ == '__main__':
    sys.exit(main())
