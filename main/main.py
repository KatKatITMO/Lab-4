items = [(3, 25, 'r'),
         (2, 15, 'p'),
         (2, 15, 'a'),
         (2, 20, 'm'),        
         (1, 15, 'k'),
         (3, 20, 'a'),
         (1, 25, 't'),
         (1, 15, 'f'),  
         (2, 20, 's'),
         (2, 20, 'c'),
         (1, 10, 'a'),
         (1, 5, 'i')]

items.sort(key = lambda x: x[1]/x[0], reverse = True)

W = 9
a = 0
firstly_you_had = 15 
selected_items = []

for item in items:
    if W >= item[0]:
        selected_items.append(item[2])
        a += item[1]
        W -= item[0]

b = [selected_items [i:i+8] for i in range(0, len(selected_items), 3)]
print('Том, возьми с собой:', b)

print('Максимальная возможная ценность вещей:', a)
for item in items:
    if item[2] not in selected_items:
        a -= item[1] 
a = a + firstly_you_had
print('Итоговые очки выживания:', a)
