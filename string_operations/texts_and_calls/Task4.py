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

def telemarketers(texts, calls):
    telemarketers = set()
    for call in calls:
        telemarketers.add(call[0])
    for call in calls:
        telemarketers.discard(call[1])
    for text in texts:
        telemarketers.discard(text[0])
        telemarketers.discard(text[1])
    return sorted(telemarketers)

if __name__ == '__main__':
    telemarketers = telemarketers(texts, calls)
    print("These numbers could be telemarketers: ")
    for telemarketer in telemarketers:
        print(telemarketer)
# TASK 4
# The time complexity of this code is O(nlog(n)) because the code iterates through all elements in calls twice and all elements in texts once.

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

