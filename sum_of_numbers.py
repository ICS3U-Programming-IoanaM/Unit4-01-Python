#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Nov. 10, 2022
# a program that displays the sum of all the numbers leading
# up to the user's imputed number


def main():
    # Variables
    user_num_string = input("Please input a whole number: ")
    counter = 0
    total_sum = 0

    # Makes sure user imputed an integer
    try:
        user_num_int = int(user_num_string)

    # if user didn't enter a number
    except Exception:
        print("Input invalid! Please enter a WHOLE number.")

    # user imputed a number
    else:
        # checks to make sure user imputed a whole number
        if user_num_int < 0:
            print("Input invalid! Please enter a WHOLE number.")

        # user imputed a whole number
        else:
            # adds every number until the user's num
            while counter <= user_num_int:
                total_sum += counter
                counter += 1

            # displays the sum of all the numbers until user's number
            print(f"The sum of all the numbers until {user_num_int} is {total_sum}")

    finally:
        print("thank you for using this program!")


if __name__ == "__main__":
    main()
