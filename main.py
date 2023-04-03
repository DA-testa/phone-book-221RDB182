# python3

import sys

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

def read_queries():
    n = int(input())
    return [input().split() for i in range(n)]

def write_responses(result):
    with sys.stdout as output:
        output.write('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    for query in queries:
        query_type = query[0]
        if query_type == 'add':
            name, number = query[1], query[2]
            if not number.isdigit():
                result.append('Invalid phone number')
            else:
                contacts[number] = Contact(name, number)
        elif query_type == 'del':
            number = query[1]
            if not number.isdigit():
                result.append('Invalid phone number')
            elif number in contacts:
                contacts.pop(number)
            else:
                result.append('Phone number not found')
        elif query_type == 'find':
            number = query[1]
            if not number.isdigit():
                result.append('Invalid phone number')
            elif number in contacts:
                result.append(contacts[number].name)
            else:
                result.append('Phone number not found')
        else:
            result.append('Invalid query')
    return result

if __name__ == '__main__':
    queries = read_queries()
    result = process_queries(queries)
    write_responses(result)
    
