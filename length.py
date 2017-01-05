def last_word(s):
    words=s.split()
    if len(words)> 0:
        return len(words[-1])
    return 0

print(last_word("welcome python"))
print(last_word("python"))