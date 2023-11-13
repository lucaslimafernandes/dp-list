a = 2

try:
    if a != 3:
        raise Exception()
    else:
        print('OK')

except:
    print('NOK')