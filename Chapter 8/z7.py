def rem(lis, word):
    n = []
    for elem in lis:
        n.append(elem.strip(word)) # strip removes all the a and n appreas in the text expect middle one
    return n


lis = ["wowan", "hen", "yan", "bestofluck","kianhoaan", "an"]
print(rem(lis, "an"))