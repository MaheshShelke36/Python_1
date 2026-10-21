def get_Max(*num):
    if len(num)==0:
        return None

    max_num=num[0]
    for n in num:
        if n> max_num:
            max_num=n
    return max_num

print(get_Max(3,12,9,21))
print(get_Max('mahesh','sahil','vaibhav','atharva'))        