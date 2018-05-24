def divide(a, b):
    answer = 0
    try:
        answer = a/b
    except ZeroDivisionError as err:
        print("Error: {}".format(err))
    else:
        print("Division Successful")
    finally:
        print("No matter what")
    return answer

print(divide(3, 0))
