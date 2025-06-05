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
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0: 
                 return None
            else:
                return num1 / num2

