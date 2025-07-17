# Project Genisys

Genisys is a CLI-tool created in python that will generate projects for you using the power of LLMs. It takes the input of type of projects that you need and will output the sample project of such type. Uses the power of local llms powered by ollama and also has the capacity to be connected to the openAI's GPT.

## Features

- Generate projects using the power of LLMs.
- Generate projects using the power of local llms powered by ollama.
- Generate projects using the power of openAI's GPT.
- Showcase projects using the power of github.

## Getting Started

To get started with using project genisys we need to setup the project locally. To get a local copy of the project clone the repository and follow the steps as follows.

## Prerequisites

- Git, Python3, OpenAI API key, and Ollama for local models.

1. Clone the repository

```bash
git clone https://github.com/Sumeet-Aulakh/Genisys
```

2. Install the dependecies

```
pip3 install -r requirements.txt
```

3. Set up the environment variables

```.env
GITHUB_TOKEN="github_..."
OPENAI_API_KEY="sk-proj-..."
GITHUB_USERNAME="your-github-name"
GITHUB_SIGNIN_TOKEN="ghp_..."
```

**Note:** You can get the github token from [here](https://github.com/settings/tokens) and the openai api key from [here](https://platform.openai.com/account/api-keys). Github token is used to authenticate the github api and the openai api key is used to authenticate the openai api. Github signin token is used to authenticate the github signin api. If you are not using github signin then you can leave the github signin token empty.

4. Run ollama for local models **Highly Recommended**

   You can run it from ollama app on macOS or you can run it from the terminal.

```bash
ollama serve
```

**Note:** You need to download first from ollama. (https://ollama.com/)

## Usage

To use the project genisys we need to run the following command.

```bash
python3 genisys.py
```

## For Local Models

Local models are supported by ollama. To use the local models we need to have the ollama installed in our system. You can install ollama by following the instructions [here](https://github.com/ollama/ollama).

For the project we have used the following models:

- [qwen2.5-coder](https://ollama.com/library/qwen2.5-coder)
- [codellama](https://ollama.com/library/codellama)
- [starcoder](https://ollama.com/library/starcoder)
- [deepseek-coder-v2](https://ollama.com/library/deepseek-coder-v2)

To use the local models we need to have the ollama installed in our system. You can install ollama by following the instructions [here](https://github.com/ollama/ollama).

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
