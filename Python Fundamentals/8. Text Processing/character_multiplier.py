word_one, word_two = input().split()
total_sum = 0
find_longest_word = word_one if len(word_one) >= len(word_two) else word_two
find_shortes_word = word_two if find_longest_word == word_one else word_one

for i in range(len(find_shortes_word)):
    total_sum += ord(word_one[i]) * ord(word_two[i])

for i in range(len(find_shortes_word), len(find_longest_word)):
    total_sum += ord(find_longest_word[i])

print(total_sum)