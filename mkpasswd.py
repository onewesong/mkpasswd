#!/usr/bin/env python3
import random
import argparse
import pyperclip

SPECIAL_CHARACTERS = '''~!@#$%^&*()[{]}-_=+|;:'",<.>/?`'''


def gen_random_digit():
    return str(random.randint(0,9))

def gen_random_uppercase():
    return chr(random.randint(65, 90))

def gen_random_lowercase():
    return chr(random.randint(97, 122))

def gen_random_special_character():
    return SPECIAL_CHARACTERS[random.randint(0, len(SPECIAL_CHARACTERS)-1)]


def get_args():
    parser = argparse.ArgumentParser(description='generate new random passwd')
    parser.add_argument("-l", "--length", default=15, type=int, help='the passwd length')
    parser.add_argument("-d",
                        "--digits-length",
                        default=3,
                        type=int,
                        help=' the digits length in the password')
    parser.add_argument("-C",
                        "--uppercase-length",
                        default=3,
                        type=int,
                        help='uppercase alphabetic characters length in the password')
    parser.add_argument("-s",
                        "--special-characters-length",
                        default=2,
                        type=int,
                        help='the special characters length in the password')

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    passwd = ''
    count = 0
    digits_length = args.digits_length
    uppercase_length = args.uppercase_length
    special_characters_length = args.special_characters_length
    while count < args.length:
        if digits_length > 0:
            passwd += gen_random_digit()
            digits_length -= 1
            count += 1
        if uppercase_length > 0:
            passwd += gen_random_uppercase()
            uppercase_length -= 1
            count += 1
        if special_characters_length > 0:
            passwd += gen_random_special_character()
            special_characters_length -= 1
            count += 1
        passwd += gen_random_lowercase()
        count += 1
    print("passwd is: ", passwd)
    pyperclip.copy(passwd)
    print("which is copied to your clipboard")



if __name__ == "__main__":
    main()