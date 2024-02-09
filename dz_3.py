def display_square(side_length, filling_char, filled):
    if filled:
        for _ in range(side_length):
            print(filling_char * side_length)
    else:
        print(filling_char * side_length)
        for _ in range(side_length-2):
            print(filling_char + " "*(side_length-2) + filling_char)
        print(filling_char * side_length)

print(display_square(5, "$", True))
print(display_square(5, "$", False))