def roman_calculator_main ():
    service = int(input("What wants to be calculated? Input: "))

    ## Translating number input to roman numerals
    if service == 1:
        num_rom = int(input("What number to Roman Numerals? Input: "))
        ntr = numbers_to_roman_numerals(num_rom)
        print(ntr)

    ## Translating roman numeral input to number
    elif service == 2:
        checker = 0
        rom_num = input("What Roman Numerals to number? Input: ")
        cap_rom_num = rom_num.upper()

        if not is_valid_roman(cap_rom_num):
            print("Invalid Roman Numeral")
            return

        character_list = list(cap_rom_num)
        for i, char in enumerate(character_list):
            if char not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
                character_list[i] += " - INVALID"
                checker += 1
        if checker != 0:
            print("Roman Numerals contained invalid characters.")
            print(character_list)
        else:
            print("Roman Numerals contained valid characters.")
            result_list = roman_numerals_to_numbers(character_list)
            final_sum = 0
            for index in range(len(result_list) - 1):
                if result_list[index] < result_list[index + 1]:
                    final_sum -= result_list[index]
                else:
                    final_sum += result_list[index]
            final_sum += result_list[len(result_list) - 1]
            print(final_sum)


    ## Adding two roman numeral inputs
    elif service == 3:
        final_sum_one = 0
        final_sum_two = 0
        checker_one = 0
        rom_one = input("First Roman Numeral? Input: ")
        cap_rom_one = rom_one.upper()

        if not is_valid_roman(cap_rom_one):
            print("Invalid Roman Numeral")
            return

        character_list_one = list(cap_rom_one)
        for i, char in enumerate(character_list_one):
            if char not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
                character_list_one[i] += " - INVALID"
                checker_one += 1
        if checker_one != 0:
            print("Roman Numerals contained invalid characters.")
            print(character_list_one)
        else:
            print("Roman Numerals contained valid characters.")
            result_list_one = roman_numerals_to_numbers(character_list_one)
            for index in range(len(result_list_one) - 1):
                if result_list_one[index] < result_list_one[index + 1]:
                    final_sum_one -= result_list_one[index]
                else:
                    final_sum_one += result_list_one[index]
            final_sum_one += result_list_one[len(result_list_one) - 1]
            print(final_sum_one)

        checker_two = 0
        rom_two = input("Second Roman Numeral? Input: ")
        cap_rom_two = rom_two.upper()

        if not is_valid_roman(cap_rom_two):
            print("Invalid Roman Numeral")
            return

        character_list_two = list(cap_rom_two)
        for i, char in enumerate(character_list_two):
            if char not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
                character_list_two[i] += " - INVALID"
                checker_two += 1
        if checker_two != 0:
            print("Roman Numerals contained invalid characters.")
            print(character_list_two)
        else:
            print("Roman Numerals contained valid characters.")
            result_list_two = roman_numerals_to_numbers(character_list_two)
            for index in range(len(result_list_two) - 1):
               if result_list_two[index] < result_list_two[index + 1]:
                    final_sum_two -= result_list_two[index]
               else:
                    final_sum_two += result_list_two[index]
            final_sum_two += result_list_two[len(result_list_two) - 1]
            print(final_sum_two)

        if checker_two == 0 and checker_one == 0:
            big_sum = final_sum_one + final_sum_two
            big_final = numbers_to_roman_numerals(big_sum)
            print(big_final)



    elif service < 1 or service > 3:
        print("Invalid service number, please try again")

def roman_numerals_to_numbers(string_list):
    ## Map of Roman Numerals
    numeral_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    converted_list = []
    for s in string_list:
        if s in numeral_map:
            converted_list.append(numeral_map[s])
        else:
            converted_list.append(s)  # keep invalid stuff if needed
    return converted_list

def numbers_to_roman_numerals(num):
    value_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""
    for value, symbol in value_map:
        while num >= value:
            result += symbol
            num -= value
    return result

def is_valid_roman(roman: str) -> bool:

    ## Rule 1: invalid repetitions
    if "IIII" in roman or "XXXX" in roman or "CCCC" in roman or "MMMM" in roman:
        print("Invalid: I, X, C, and M cannot repeat more than 3 times.")
        return False
    if "VV" in roman or "LL" in roman or "DD" in roman:
        print("Invalid: V, L, and D cannot repeat.")
        return False

    ## Rule 2: legal subtractions
    invalid_subtractions = [
        "IL", "IC", "ID", "IM",   # I only before V or X
        "XD", "XM",               # X only before L or C
        "VX", "VL", "VC", "VD", "VM",  # V cannot subtract
        "LC", "LD", "LM",         # L cannot subtract
        "DM"                      # D cannot subtract
    ]
    for bad in invalid_subtractions:
        if bad in roman:
            print(f"Invalid: {bad} is not a legal subtractive pair.")
            return False

    ## Rule 3: descending order check
    numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    values = [numeral_map[ch] for ch in roman]
    for i in range(len(values) - 1):
        if values[i] < values[i + 1]:
            pair = roman[i:i+2]
            if pair not in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                print(f"Invalid: numerals not in descending order at {pair}.")
                return False

    return True

roman_calculator_main()