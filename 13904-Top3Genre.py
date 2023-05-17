#!/usr/bin/python3

ratings = {} # "genre" : [#, total rating]

while True:
    try: 
        inputList = input().split(',')
        rating = float(inputList[2])
        genres = inputList[1].split('|')
        for genre in genres:
            if genre in ratings:
                ratings[genre][0] += 1
                ratings[genre][1] += rating
            else:
                ratings[genre] = [1, rating]
    except EOFError as e:
        break

avgRating = []
for key, value in ratings.items():
    avg = value[1]/value[0]
    avg = int(avg*100) / 100
    avgRating.append([key, avg])

for genre in sorted(avgRating, key = lambda x: (x[1], x[0]), reverse = True)[0:3]:
    print(f'{genre[0]},{genre[1]:.2f}')