sql2fs:
	cat prompts/sql2fs.txt | llm -m mlx-community/Mistral-Small-24B-Instruct-2501-4bit -o temperature 0.0 -o seed 1 -x > sql2fs.py

test: hello_response
	cat build/hello_response.txt | python3 sql2fs.py

hello_response: 
	/bin/sh generate_hello_response.sh