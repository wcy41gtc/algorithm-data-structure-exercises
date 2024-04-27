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

def longest_time_on_phone(calls):
    phone_time = {}
    for call in calls:
        if call[0] in phone_time:
            phone_time[call[0]] += int(call[3])
        else:
            phone_time[call[0]] = int(call[3])
        if call[1] in phone_time:
            phone_time[call[1]] += int(call[3])
        else:
            phone_time[call[1]] = int(call[3])
    max_time = max(phone_time.values())
    for phone, time in phone_time.items():
        if time == max_time:
            return phone, time
def get_codes(calls):
    codes = set()
    for call in calls:
        if call[0].startswith('(080)'):
            if call[1].startswith('(080)'):
                codes.add('080')
            elif call[1].startswith('('):
                codes.add(call[1].split(')')[0][1:])
            elif call[1].startswith('140'):
                codes.add('140')
            else:
                codes.add(call[1].split()[0])
    return codes

def percentage_of_calls(calls):
    count = 0
    total = 0
    for call in calls:
        if call[0].startswith('(080)'):
            total += 1
            if call[1].startswith('(080)'):
                count += 1
    return count / total * 100

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
    print("First record of texts, {} texts {} at time {}".format(texts[0][0], texts[0][1], texts[0][2]))
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))
    print("There are {} different telephone numbers in the records.".format(count_unique_numbers(texts, calls)))
    phone, time = longest_time_on_phone(calls)
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone, time))
    codes = get_codes(calls)
    print("The numbers called by people in Bangalore have codes:")
    for code in sorted(codes):
        print(code)
    print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage_of_calls(calls)))
    print("These numbers could be telemarketers: ")
    for telemarketer in telemarketers(texts, calls):
        print(telemarketer)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

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