def has_no_repeats(s):
    prev_char = s[0]
    for i in range(1,len(s)):
        if prev_char == s[i]: return False
        else: prev_char = s[i]

    return True

if __name__ == '__main__':
    print(has_no_repeats("hi world"))
    print('------')
    print(has_no_repeats("hello world"))
    print('------')
    print(has_no_repeats("abcdefghijklmnopqrstuvwxyz"))
    print('------')
    print(has_no_repeats("freeCodeCamp"))
    print('------')
    print(has_no_repeats("The quick brown fox jumped over the lazy dog."))
    print('------')
    print(has_no_repeats("Mississippi"))