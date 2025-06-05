def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    operation_dictionary = {
        "add": num1 + num2,
        "subtract": num1 - num2,
        "multiply": num1 * num2,
        "divide": num1 / num2 if num2 != 0 else None
    }
    return operation_dictionary.get(operation)


