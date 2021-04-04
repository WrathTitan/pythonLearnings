def check_balance(brackets):
    check = 0
    for bracket in brackets:
        if bracket == '[':
            check += 1

        elif bracket == ']':
            check -= 1

        if check < 0:
            return False

    return check == 0


bracket_string = '[[[[[[]]]]'

print(check_balance(bracket_string))
