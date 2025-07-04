# ask LLMs in the Terminal

`ask_openai.py` – call the [OpenAI API](https://openai.com/api), `API_KEY` required 

`ask_ollama.py` – call the [local Ollama API](https://ollama.com/) (localhost:11434)

required:
* [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) (input)
* [openai](https://github.com/openai/openai-python) (ask_openai.py)
* [requests](https://requests.readthedocs.io/) (ask_ollama.py)
* [rich](https://github.com/Textualize/rich) (output)

## OpenAI API

[ask_openai.py](https://github.com/haalven/LLM_terminal/blob/main/ask_openai.py) uses the [openai Python library](https://github.com/openai/openai-python) to call the [OpenAI API](https://openai.com/api). An internet connection is required.

[ask_openai.toml](https://github.com/haalven/LLM_terminal/blob/main/ask_openai.toml) ➔ you have to insert your `API_KEY` by editing the `my_api_key = "sk-***"` line before running the script.

usage: `./ask_openai.py <model> [question?]`

Choose a specific OpenAI model ➔ see: [platform.openai.com/docs/models](https://platform.openai.com/docs/models).

## Ollama API

[ask_ollama.py](https://github.com/haalven/LLM_terminal/blob/main/ask_ollama.py) uses the [requests Python library](https://requests.readthedocs.io/) to call the [local Ollama API](https://ollama.com/) (based on [llama.cpp](https://en.wikipedia.org/wiki/Llama.cpp)). An internet connection is not required. Install Ollama first and start the local server (localhost:11434). To download LLMs use the `ollama run <model>` command.

usage: `./ask_ollama.py <model> [question?]`

The best general LLMs for computers with 8…16 GB of RAM in March 2025 are `gemma3n:e4b` by Google (4B, 7.5GB) and `llama3.2` by Meta (3B, 2.0GB). See also: [ollama.com/models](https://ollama.com/models).

## Example

![example screenshot](example1.jpg)
