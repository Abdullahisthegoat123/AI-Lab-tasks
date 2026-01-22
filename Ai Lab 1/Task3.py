def anagram(string1,string2):
    if len(string1) == len(string2):
        for char in string1:
            if char in string2:
                continue
            else:
                return False
        print(f"Is '{string1}' an anagram of '{string2}'?")
        return True
    else:
        print(f"Is '{string1}' an anagram of '{string2}'?")
        return False

print(anagram("listen","silent"))