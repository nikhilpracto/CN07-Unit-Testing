from tabnanny import check

def check_luhn(card_no):
    length_digits = len(card_no)
    sum_digits = 0
    is_second = False

    for ind in range(length_digits-1, -1, -1):
        d = ord(card_no[ind]-ord('0'))

        if(is_second == True):
            d = d * 2

        sum_digits += d // 10
        sum_digits += d % 10

        is_second = not is_second

    if(sum_digits % 10 == 0):
        return True
    else:
        return False

if __name__ == "__main__":

    card_no = input("Credit card number:")

    if(check_luhn(card_no)):
        print("Valid card no")
    else:
        print("Not valid card no")
