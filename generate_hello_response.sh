#!/usr/bin/env bash

set -euo pipefail

system_prompt=$(cat src/system.txt)

mkdir -p build

# shellcheck disable=SC2002
cat "testdata/hello.txt" | llm -s "$system_prompt" \
    -m mlx-community/Mistral-Small-24B-Instruct-2501-4bit \
    -o temperature 0.0 \
    -o seed 1 > build/hello_response.txt