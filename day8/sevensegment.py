'''
Advent Of Code - 2021
Day 8 - Seven segment search
'''

result = 0
results_sum = 0

with open('input') as input:
    for line in input:
        signals = line.split('|')[0].strip().split()
        numbers = line.split('|')[1].strip().split()
        for digit in numbers:
            if len(digit) in [2, 4, 3, 7]:
                result += 1

        for digit in signals:
            if len(digit) == 2:
                one_comps = digit
            if len(digit) == 3:
                seven_comps = digit
            if len(digit) == 4:
                four_comps = digit
            if len(digit) == 7:
                eight_comps = digit

        for char in seven_comps:
            if char not in one_comps:
                zero_pos = char

        two_ambiguous = one_comps

        four_ambiguous = ""
        for char in four_comps:
            if char not in one_comps:
                four_ambiguous += char

        eight_ambiguous = ""
        for char in eight_comps:
            if char not in one_comps and char not in seven_comps and char not in four_comps:
                eight_ambiguous += char

        for digit in signals:
            if len(digit) == 6:
                for char in eight_ambiguous:
                    if char not in digit:
                        four_pos = char
                        for nochar in eight_ambiguous:
                            if nochar != char:
                                six_pos = nochar
                for char in two_ambiguous:
                    if char not in digit:
                        two_pos = char
                        for nochar in two_ambiguous:
                            if nochar != char:
                                five_pos = nochar
                for char in four_ambiguous:
                    if char not in digit:
                        three_pos = char
                        for nochar in four_ambiguous:
                            if nochar != char:
                                one_pos = nochar

        final_result = ""
        for digit in numbers:
            if len(digit) == 2:
                final_result += '1'
            elif len(digit) == 3:
                final_result += '7'
            elif len(digit) == 4:
                final_result += '4'
            elif len(digit) == 7:
                final_result += '8'
            elif set([zero_pos, two_pos, five_pos, six_pos, four_pos,
                      one_pos]) == set(digit):
                final_result += '0'
            elif set([zero_pos, one_pos, three_pos, five_pos,
                      six_pos]) == set(digit):
                final_result += '5'
            elif set(
                [zero_pos, one_pos, three_pos, five_pos, six_pos,
                 four_pos]) == set(digit):
                final_result += '6'
            elif set([zero_pos, two_pos, three_pos, four_pos,
                      six_pos]) == set(digit):
                final_result += '2'
            elif set([zero_pos, two_pos, three_pos, five_pos,
                      six_pos]) == set(digit):
                final_result += '3'
            else:
                final_result += '9'

        final_result = int(final_result)
        results_sum += final_result

print(f"Digit 1, 4, 7 and 8 appears {result} times")
print(f"Sum of all output values is {results_sum}")
