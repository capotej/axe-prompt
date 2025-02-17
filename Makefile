response2fs:
	cat prompts/response2fs.txt | llm -m mlx-community/Mistral-Small-24B-Instruct-2501-4bit -o temperature 0.0 -o seed 1 -x > response2fs.py

test: build/hello_response.txt
	cat build/hello_response.txt | python3 response2fs.py
	python3 build/hello.py "alice"

hello_response: 
	/bin/sh generate_hello_response.sh