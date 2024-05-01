"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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

if __name__ == '__main__':
    phone, time = longest_time_on_phone(calls)
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone, time))
# TASK 2
# The time complexity of this code is O(n) because the code is iterating through all the elements in the calls list.
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

