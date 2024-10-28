import random
count = 1
while True:
    print('Help!')
    if random.choice(range(10000)) == 111:
        break
        print('Let me out!')
    count += 1


print ('At last! It took', count, 'tries to escape!')
    