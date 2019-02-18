data = []
count =0
line_average = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('Finished loading.', len(data), 'line(s) in total.')

sum_len = 0
for d in data:
	sum_len += len(d)
print('The average lengh of each review is', sum_len / len(data))