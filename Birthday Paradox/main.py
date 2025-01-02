import random

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']
date = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

number_of_bdays = int(input('How many Birthdays do you want to generate?: '))
print(f'Creating {number_of_bdays} birthdays...')
bday_list = []

for i in range(number_of_bdays):
    random_month = random.randrange(len(month))
    random_date = random.randrange(len(date))
    bday = month[random_month], date[random_date]
    bday_list.append(bday)

print(f'{number_of_bdays} birthdays created...')
# print(bday_list)

duplicate_list = []
for i in bday_list:
    index = bday_list.index(i)
    bday_list.pop(index)
    if bday_list.count(i) > 1:
        duplicate_list.append(i)

print('Simulation 100,000 times...')
sim_bday_num = number_of_bdays * 100_000
sim_num_of_duplicates = len(duplicate_list) * 100_000
percent = str((sim_num_of_duplicates / sim_bday_num))

if percent[2:] == 0:
    percent = percent[3:]
else:
    percent = percent[2:4]

print(f'There is a {percent}% chance of people having the same bday')