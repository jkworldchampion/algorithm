word = list(map(str, input()))

word_vector = [-1] * 26

for i in range(len(word)):
    index = ord(word[i])
    if word_vector[index-97] != -1:
        continue
    word_vector[index-97] = i

for i in word_vector:
    print(i, end=' ')
