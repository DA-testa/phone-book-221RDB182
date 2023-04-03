# python3

import sys
from collections import defaultdict

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

def read_queries():
    n = int(input())
    return [input().split() for i in range(n)]

def write_responses(result):
    print('\n'.join(result))
    # Keep list of all existing (i.e. not deleted yet) contacts.
def process_queries(queries):
    result = []
    contacts = defaultdict(list)
    for query in queries:
        query_type = query[0]
            # we should rewrite contact's name
        if query_type == 'add':
            name, number = query[1], query[2]
            if not number.isdigit():
                result.append('Invalid phone number')
            else:
                contacts[number].append(Contact(name, number))
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
                result.append(contacts[number][-1].name)
            else:
                result.append('Phone number not found')
        else:
            result.append('Invalid query')
    return result

if __name__ == '__main__':
    queries = read_queries()
    result = process_queries(queries)
    write_responses(result)
    
