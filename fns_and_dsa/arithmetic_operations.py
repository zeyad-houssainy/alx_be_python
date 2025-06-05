# Another Way
# def perform_operation(num1, num2, operation):
#     num1 = float(num1)
#     num2 = float(num2)
#     operation_dictionary = {
#         "add": num1 + num2,
#         "subtract": num1 - num2,
#         "multiply": num1 * num2,
#         "divide": num1 / num2 if num2 != 0 else None
#     }
#     return operation_dictionary.get(operation)

def perform_operation(num1, num2, operation):
        num1 = float(num1)
        num2 = float(num2)
        if operation == "add":
            return num1 + num2
        if operation == "subtract":
            return num1 - num2
        if operation == "multiply":
            return num1 * num2
        if operation == "divide":
            return num1 / num2 if num2 != 0 else None
