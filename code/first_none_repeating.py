def first_not_repeating_characters(s):
    chars = {}

    for c in s:             # loop through the string
        if chars.get(c):    
            chars[c] +=1    # adds the c count to the hashtable

        else:
            chars[c] = 1    

    for c in s:             # loops through to the refers to see the first none repeating character
        if chars[c] == 1:   
            return c

    return "_"                    

    # Time complexity Log(n)