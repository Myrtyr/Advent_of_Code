from day8 import *

with open('2021/data/input_day8.txt', 'r') as f:
    displays = f.readlines()

result = 0
for display in displays:
    numbers_1478 = {}
    all_numbers = {}
    output = display.split("|")[0].split()
    fives = []
    sixes = []
    # Figure out 1, 4, 7 and 8
    for digit in output:
        if len(digit) == 2:
            numbers_1478[1] = [character for character in digit]
            all_numbers[digit] = '1'
        elif len(digit) == 3:
            numbers_1478[7] = [character for character in digit]
            all_numbers[digit] = '7'
        elif len(digit) == 4:
            numbers_1478[4] = [character for character in digit]
            all_numbers[digit] = '4'
        elif len(digit) == 7:
            numbers_1478[8] = [character for character in digit]
            all_numbers[digit] = '8'
        elif len(digit) == 6:
            sixes.append(digit)
        else:
            fives.append(digit)

    # Figure out remaining digits
    first_one, second_one = numbers_1478[1]
    letters_four = numbers_1478[4]
    fours = []
    for letter in letters_four:
        if letter != first_one and letter != second_one:
            fours.append(letter)
    first_four, second_four = fours
    for digit in fives:
        if first_one in digit and second_one in digit:
            all_numbers[digit] = '3'
        elif first_four in digit and second_four in digit:
            all_numbers[digit] = '5'
        else:
            all_numbers[digit] = '2'
    for digit in sixes:
        if first_one in digit and second_one in digit:
            if first_four in digit and second_four in digit:
                all_numbers[digit] = '9'
            else:
                all_numbers[digit] = '0'
        else:
            all_numbers[digit] = '6'

    digit_code  = display.split("|")[1].split()
    decoded_digit = ''
    for digit in digit_code:
        unordered = set(digit)
        for number in all_numbers:
            if unordered == set(number):
                correct_digit = all_numbers[number]
                break
        decoded_digit += correct_digit
    result += int(decoded_digit)
print(result)