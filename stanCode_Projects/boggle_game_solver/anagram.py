"""
File: anagram.py
Name: Jael Lin
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 23

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
d = []
ans = []
new_d1 = []
new_d2 = []
new_d3 = []


def main():
    """
    TODO: This program recursively finds all the anagram(s)
        for the word input by user and terminates when the
        input string matches the EXIT constant defined
        at line 23.
    """
    global new_d1, new_d2, new_d3
    read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\" ""(or " + str(EXIT) + " to quit)")
    while True:
        start = time.time()
        s = input("Find anagrams for: ")
        if s == EXIT:
            break
        else:
            print("Searching... ")
            find_anagrams(s)
            for answer in ans:
                print("Found: " + answer)
                print("Searching... ")
            print(f'{len(ans)} anagrams: {ans}')
            new_d1 = []
            new_d2 = []
            new_d3 = []
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, "r")as f:
        for line in f:
            line = line.strip()
            d.append(line)


def find_anagrams(s):
    """
    :param s: str, the word input by user.
    :return: list ans, within all the anagram.
    """
    if len(ans) != 0:
        for i in range(len(ans)):
            ans.pop()
    word_lst = {}
    for word in s:
        if word not in word_lst:
            word_lst[word] = 1
        else:
            word_lst[word] += 1
    find_anagrams_helper(word_lst, "", len(s))
    return ans


def find_anagrams_helper(word_lst, current_s, ans_s):
    if len(current_s) == ans_s:
        if current_s in d:
            ans.append(current_s)
    else:
        for key in word_lst:
            if word_lst[key] != 0:
                current_s += key
                word_lst[key] -= 1
                if has_prefix(current_s):
                    find_anagrams_helper(word_lst, current_s, ans_s)
                current_s = current_s[0:(len(current_s)-1)]
                word_lst[key] += 1


def has_prefix(sub_s):
    """
    :param sub_s: str, The string (current_s) we check if in the dictionary.
    :return: bool, Return True when sub_s is in the dictionary.
    """
    if len(sub_s) == 1:
        for word in d:
            if word.startswith(sub_s):
                new_d1.append(word)
        return True
    elif len(sub_s) == 2:
        for word in new_d1:
            if word.startswith(sub_s):
                new_d2.append(word)
        return True
    elif len(sub_s) == 3:
        for word in new_d2:
            if word.startswith(sub_s):
                new_d3.append(word)
        return True
    else:
        for word in new_d3:
            if word.startswith(sub_s):
                return True


if __name__ == '__main__':
    main()
