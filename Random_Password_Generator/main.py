import string as str
import random as ran


if __name__ == '__main__':
    s1 = str.ascii_lowercase
    # print(s1)
    s2 = str.ascii_uppercase
    # print(s2)
    s3 = str.digits
    # print(s3)
    s4 = str.punctuation
    # print(s4)

    pass_len = int(input("Enter the password length\n"))
    s = list()

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)

    ran.shuffle(s)
    print("".join(s[:pass_len]))