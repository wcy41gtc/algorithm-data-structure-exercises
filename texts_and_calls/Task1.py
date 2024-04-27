"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def count_unique_numbers(texts, calls):
    unique_numbers = set()
    for text in texts:
        unique_numbers.add(text[0])
        unique_numbers.add(text[1])
    for call in calls:
        unique_numbers.add(call[0])
        unique_numbers.add(call[1])
    return len(unique_numbers)

if __name__ == '__main__':
    print("There are {} different telephone numbers in the records.".format(count_unique_numbers(texts, calls)))
# TASK 1
# The time complexity of this code is O(n) because the code is iterating through all the elements in the texts and calls lists.
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
