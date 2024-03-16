stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

mantissa = stdform[:stdform.index("x")]
exponents = stdform[stdform.index("^")+1:]
valid = True

if(stdform.count(".") <= 1) and (stdform.count("x") <= 1) and (stdform.count("^") <= 1) and ("." not in exponents):
    for i in stdform:
        if i not in ("0123456789x^-."):
            print("Error converting to scientific E notation.")
            valid = False
            break
        else:
            valid = True
    if(valid):
        Enotation = stdform.replace(stdform.rstrip(exponents).lstrip(mantissa), "E")
        print(f"This number in E notation is {Enotation}.")
else:
    print("Error converting to scientific E notation.")