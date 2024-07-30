# ask LLMs in the Terminal

`ask_openai.py` – call the [OpenAI API](https://openai.com/api), fill in your `API_KEY`

`ask_ollama.py` – call the [local Ollama API](https://ollama.com/) (localhost:11434)

required:
* [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)
* [openai](https://github.com/openai/openai-python) (ask_openai.py)
* [requests](https://requests.readthedocs.io/) (ask_ollama.py)
* [rich](https://github.com/Textualize/rich)

## OpenAI API

`ask_openai.py` uses the [openai](https://github.com/openai/openai-python) Python library to call the [OpenAI API](https://openai.com/api). An internet connection is required. You have to insert your `API_KEY` by editing the `my_api_key = '***'` line before running the script. Choose a specific OpenAI model by editing the `gpt_model = 'gpt-4o'` line.

## Ollama API

`ask_ollama.py` uses the [requests](https://requests.readthedocs.io/) Python library to call the [local Ollama API](https://ollama.com/). An internet connection is not required. Install Ollama first and start the local server (localhost:11434). To download LLMs use the `ollama run <model>` command. The best general LLMs for computers with 8…16 GB of RAM are `gemma2` by Google (9B, 5.4GB), `llama3.1` by Meta (8B, 4.7GB), `phi3` by Microsoft (4B, 2.2GB), and `mistral` by MistralAI (7B, 4.1GB).
