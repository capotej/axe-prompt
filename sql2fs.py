import os
import sys
import re
from typing import List

def read_sql_from_stdin() -> str:
    return sys.stdin.read()

def extract_sql_statements(sql_input: str) -> List[str]:
    # Simple regex to extract SQL statements
    sql_statements = re.findall(r'CREATE TABLE.*?;|INSERT INTO.*?;|UPDATE.*?;', sql_input, re.DOTALL)
    return sql_statements

def create_directory(path: str):
    os.makedirs(path, exist_ok=True)

def create_file(path: str, content: str):
    with open(path, 'w') as file:
        file.write(content)

def update_file(path: str, content: str):
    with open(path, 'w') as file:
        file.write(content)

def process_sql_statements(sql_statements: List[str]):
    for statement in sql_statements:
        statement = statement.strip()
        if statement.startswith('CREATE TABLE'):
            # We assume the table creation is already done as per the schema
            continue
        elif statement.startswith('INSERT INTO'):
            match = re.match(r'INSERT INTO files \(name, content\) VALUES \((\'[^\']*\'), (b\'[^\']*\'|NULL)\);', statement)
            if match:
                name = match.group(1).strip("'")
                content = match.group(2).strip("b'")
                if content == 'NULL':
                    content = ''
                directory = os.path.dirname(name)
                create_directory(directory)
                create_file(name, content)
        elif statement.startswith('UPDATE'):
            match = re.match(r'UPDATE files SET content = \'([^\']*)\' WHERE name = \'([^\']*)\';', statement)
            if match:
                content = match.group(1)
                name = match.group(2)
                update_file(name, content)

def main():
    sql_input = read_sql_from_stdin()
    sql_statements = extract_sql_statements(sql_input)
    process_sql_statements(sql_statements)

if __name__ == "__main__":
    main()

