regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

import re
n = input()

print (bool(re.match(regex_integer_in_range, n)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, n)) < 2)