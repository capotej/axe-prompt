# Axe System Prompt

# Overview
This repository contains a prompting strategy to enable tool/function calling for LLM workflows that do not support it explicitly. 

Currently, it is strictly focused on creating/updating files, but plan to support generic function calling in the future.

# How it works
This system prompt instructs the model to render all code snippets strictly as INSERT or UPDATE statements to a fictional "files" database. These SQL statements can then be parsed out of the model's output and turned into actual filesystem operations.

# Tests

You can evaluate different models using `llm` and editing the model name in the Makefile. 

I'm using [Mistral-Small-24B-Instruct-2501-4bit](https://huggingface.co/mlx-community/Mistral-Small-24B-Instruct-2501-4bit) via [llm-mlx](https://pypi.org/project/llm-mlx/)

## Dependencies
* [llm](http://llm.datasette.io)


