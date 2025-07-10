def digit_root(num):
    if num < 10:
        return num
    num_str = str(num)
    digits_list = []
    for digit_char in num_str:
        digit_num = int(digit_char)
        digits_list.append(digit_num)
    digits_sum = sum(digits_list)
    return digit_root(digits_sum)