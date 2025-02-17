import sys
import re

def read_input():
    """Read input from STDIN."""
    return sys.stdin.read()

def extract_sql_statements(input_text):
    """Extract SQL statements from the input text."""
    # Use a regular expression to find SQL statements
    sql_statements = re.findall(r'INSERT\(\'([^\']+)\', \'([^\']+)\'\)|UPDATE\(\'([^\']+)\', \'([^\']+)\'\)', input_text)
    return sql_statements

def perform_filesystem_operations(sql_statements):
    """Perform filesystem operations based on the extracted SQL statements."""
    for statement in sql_statements:
        if statement[0]:  # INSERT statement
            filename = statement[0]
            content = statement[1]
            with open(filename, 'w') as file:
                file.write(content)
        elif statement[2]:  # UPDATE statement
            filename = statement[2]
            content = statement[3]
            with open(filename, 'w') as file:
                file.write(content)

def main():
    input_text = read_input()
    sql_statements = extract_sql_statements(input_text)
    perform_filesystem_operations(sql_statements)

if __name__ == "__main__":
    main()

