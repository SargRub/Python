# Print function
def our_print(*obj, sep=" ", end="\n"):
    for i in range(len(obj)):
        if i < len(obj) - 1:
            print(obj[i], end=sep)
        else:
            print(obj[i], end=end)






