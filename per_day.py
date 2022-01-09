'''This is a function I created to add all of the hours and minutes that remained in a Udemy class and calculate how many minutes I needed to watch per day in order to be
    adequately prepared for an exam.'''

def per_day(hours, minutes, days_until_test):
    total_hours = 0
    total_minutes = 0
    for i in hours:
        i = int(i)
        total_hours += i
    for i in minutes:
        i = int(i)
        total_minutes += i
    total = (total_hours * 60) + total_minutes
    return total // days_until_test


hours_left = input('Enter hours: ').split()
minutes_left = input('Enter minutes: ').split()
days_left = int(input('Enter days until exam: '))
how_much = per_day(hours_left, minutes_left, days_left)
print('You will need to watch', how_much, 'per day.')
