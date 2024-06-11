# List even numbers

MAX_NUMBER = 12

def even_numbers():
    for i in range(MAX_NUMBER):
        if i % 2 == 0:
            print(i, end=' ')

even_numbers()
