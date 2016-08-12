def digit_to_word(num):
    if num == 1: return "one "
    if num == 2: return "two "
    if num == 3: return "three "
    if num == 4: return "four "
    if num == 5: return "five "
    if num == 6: return "six "
    if num == 7: return "seven "
    if num == 8: return "eight "
    if num == 9: return "nine "
    return ""
def written_form(num):
    out = ""
    ones = num % 10
    tens = num // 10 % 10
    hund = num // 100 % 10
    thou = num // 1000 % 10
    if thou: out += "one thousand "
    if hund: out += digit_to_word(hund) + "hundred "
    if hund and (tens or ones): out += "and "
    if tens:
        if tens == 1:
            if ones == 0: out += "ten "
            if ones == 1: out += "eleven "
            if ones == 2: out += "twelve "
            if ones == 3: out += "thirteen "
            if ones == 4: out += "fourteen "
            if ones == 5: out += "fifteen "
            if ones == 6: out += "sixteen "
            if ones == 7: out += "seventeen "
            if ones == 8: out += "eighteen "
            if ones == 9: out += "nineteen "
        if tens == 2: out += "twenty "
        if tens == 3: out += "thirty "
        if tens == 4: out += "forty "
        if tens == 5: out += "fifty "
        if tens == 6: out += "sixty "
        if tens == 7: out += "seventy "
        if tens == 8: out += "eighty "
        if tens == 9: out += "ninety "
    if ones:
        if tens != 1:
            out += digit_to_word(ones)
    return out
count = 0
for i in range(1,1000+1):
    count += sum(len(token) for token in written_form(i).split())
print(count)
