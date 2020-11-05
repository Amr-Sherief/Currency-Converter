try:
    currencies = ["1: EUR To USD" "     2: USD To EUR",
                  "3: EGP To USD" "     4: USD To EGP",
                  "5: EUR To EGP" "     6: EGP To EUR",
                  "7: GBP To USD" "     8: USD To GBP",
                  "9: GBP To EUR" "     10: EUR To GBP",
                  "11: GBP To EGP" "    12: EGP To GBP", ]  # a list of all possible currencies input

    print("Choose one of the options below:")

    for i in currencies:
        print(i)

    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # a list of possible correct inputs

    print("\nYour Choice:")

    c = int(
        input())  # todo: do something to change the ValueError that appears if the variable (c) is a letter and NOT a digit

    if c in inputs:
        print("Type the number to convert:")
        if c == inputs[0]:  # converts EUR To USD
            n = int(input())
            n = n * 1.18163
            n = round(n, 2)
            print("Result:")
            print(str(n) + "$")
        if c == inputs[1]:  # converts USD To EUR
            n = int(input())
            n = n * 0.846177
            n = round(n, 2)
            print("Result:")
            print(str(n) + "€")
        if c == inputs[2]:  # converts EGP to USD
            n = int(input())
            n = n * 0.0637487
            n = round(n, 2)
            print("Result:")
            print(str(n) + "$")
        if c == inputs[3]:  # converts USD to EGP
            n = int(input())
            n = n * 15.6866
            n = round(n, 2)
            print("Result:")
            print(str(n) + "L.E")
        if c == inputs[4]:  # converts EUR to EGP
            n = int(input())
            n = n * 18.5430
            n = round(n, 2)
            print("Result:")
            print(str(n) + "L.E")
        if c == inputs[5]:  # converts EGP To EUR
            n = int(input())
            n = n * 0.0539317
            n = round(n, 2)
            print("Result:")
            print(str(n) + "€")
        if c == inputs[6]:  # converts GBP To USD
            n = int(input())
            n = n * 1.30981
            n = round(n, 2)
            print("Result:")
            print(str(n) + "$")
        if c == inputs[7]:  # converts USD To GBP
            n = int(input())
            n = n * 0.763544
            n = round(n, 2)
            print("Result:")
            print(str(n) + "£")
        if c == inputs[8]:  # converts GBP To EUR
            n = int(input())
            n = n * 1.10826
            n = round(n, 2)
            print("Result:")
            print(str(n) + "€")
        if c == inputs[9]:  # converts EUR To GBP
            n = int(input())
            n = n * 0.901906
            n = round(n, 2)
            print("Result:")
            print(str(n) + "£")
        if c == inputs[10]:  # converts GBP To EGP
            n = int(input())
            n = n * 20.5552
            n = round(n, 2)
            print("Result:")
            print(str(n) + "L.E")
        if c == inputs[11]:  # converts EGP To GBP
            n = int(input())
            n = n * 0.0486344
            n = round(n, 2)
            print("Result:")
            print(str(n) + "£")

    else:
        print("Error: Choose one of the above choices")
except ValueError:
    print("Insert digits ONLY")
