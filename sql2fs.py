import os
import sys
import re

def read_input():
    return sys.stdin.read()

def extract_sql_statements(input_text):
    # Regular expression to match SQL statements
    sql_statement_pattern = re.compile(r'INSERT\(\'([^\']+)\', \'([^\']+)\'\)|UPDATE\(\'([^\']+)\', \'([^\']+)\'\)', re.IGNORECASE)
    matches = sql_statement_pattern.findall(input_text)
    return matches

def create_directory(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def perform_filesystem_operations(sql_statements):
    for statement in sql_statements:
        if statement[0]:  # INSERT statement
            file_path, content = statement[0], statement[1]
            create_directory(file_path)
            with open(file_path, 'w') as file:
                file.write(content)
        elif statement[2]:  # UPDATE statement
            file_path, content = statement[2], statement[3]
            if os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write(content)
            else:
                print(f"Error: File '{file_path}' does not exist for UPDATE operation.")

def main():
    input_text = read_input()
    sql_statements = extract_sql_statements(input_text)
    perform_filesystem_operations(sql_statements)

if __name__ == "__main__":
    main()

