# 최종본
word = list(map(str, input().upper()))
word.sort()

word_set = []
count = []

for i in range(len(word)):
    if word[i] in word_set:
        count[len(count)-1] += 1

    else :
        word_set.append(word[i])
        count.append(1)

max_index = count.index(max(count))
is_two = 0
for i in range(len(count)):
    if count[i]==count[max_index]:
        is_two += 1

if is_two != 1:
    print('?')
else:
    print(word_set[max_index])
