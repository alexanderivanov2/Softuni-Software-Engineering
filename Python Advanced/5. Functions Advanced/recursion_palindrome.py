def palindrome(word, index=0, left_index=-1):
    if len(word) // 2 == index:
        return f"{word} is a palindrome"
    if word[index] == word[left_index]:
        return palindrome(word, index + 1, left_index - 1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peterp", 0))

