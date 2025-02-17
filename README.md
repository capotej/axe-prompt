# Axe System Prompt

# Overview

This repository contains a prompting strategy to enable tool/function calling for LLM workflows that do not support it explicitly. 

Currently, it is focused on creating/updating files, but plan to support generic function calling in the future.

# How it works

This system prompt instructs the model to render all code using the [txtar](https://pkg.go.dev/golang.org/x/tools/txtar) format. You can then pipe the model's output to something like `response2fs.py` to turn the `txtar` output into filesystem operations. 

# Tests

You can evaluate different models using `llm` and changing the model used in `build_hello_response.sh`. 

## Running tests (M1 Mac)

1. Install [llm](http://llm.datasette.io) using uv

        $ uv tool install llm

2.  Install the [MLX llm plugin](https://pypi.org/project/llm-mlx/)

        $ llm install llm-mlx

3. Download [Mistral-Small-24B-Instruct-2501-4bit](https://huggingface.co/mlx-community/Mistral-Small-24B-Instruct-2501-4bit)

        $ llm mlx download-model mlx-community/Mistral-Small-24B-Instruct-2501-4bit

4. Run `make test`

5. You should see `Hello, alice!` if all went well.