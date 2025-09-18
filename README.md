This is a Roman Numerals Calculator I was inspired to make from my Ethics in AI class. We were discussing Turing Machines and the idea of a Turing Machine developing its own method of calculating Roman numerals, so I was like, why don't I try and make one?
When the code is run, there is a prompt asking what would you like the calculator to do? Right now (9/17/25) there are three options: input "1" translates regular numbers to numerals, input "2" translate numerals to regular numbers, and input "3" adds to sets of roman numerals together. Any other digit input for the first question prints an error message and terminates the program.\

Depending on the answer to the first prompt, the user can then input the number or numerals for the desired action. However, there are rules for the numerals that can be inputted into the algorithm. If one of the rules is broken, an error message is printed and the program is terminated.
 - **Rule 1:** The user must input valid numerals, which include I (1), V (5), X (10), L (50), C (100), D (500), and M (1000)
 - **Rule 2:** There can not be more than 3 of the same numeral in a row. For example: III = valid, IIII = not valid. 
          Additionally: V, L, and D can only appear once in a given set of numerals
 - **Rule 3:** Adhere to the valid subtractions of numerals. The invalid subtractions of numerals are : "IL", "IC", "ID", "IM", "XD", "XM", "VX", "VL", "VC", "VD", "VM", "LC", "LD", "LM", and "DM". 
 - **Rule 4:** The numerals have to be in descending order (besides the valid subtractions)
  
I am hoping to increase the functions of this calculator in the future. For now, the baseline rules of Roman Numerals are in place and the basic functionality is working nicely :D
