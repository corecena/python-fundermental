from collections import deque
from array import array
numbers = array("i",[1,4,8,9])
print(type(numbers))
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
sentence = input(" enter the string to test")

char_frequency ={}
for letter in sentence:
    if letter in char_frequency:
        char_frequency[letter] +=1
    else:
        char_frequency[letter] =1
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv:kv[1],
    reverse =True
)
print(char_frequency_sorted[0])
print(char_frequency_sorted[1])