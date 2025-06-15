def safe_divide(numerator, denominator):
    try:
        value = numerator / denominator
    except ZeroDivisionError:
        print("")
    except ValueError:
        print("")