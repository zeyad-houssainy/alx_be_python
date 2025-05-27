task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = "that requires immediate attention today!" if input(
    "Is it time-bound? (yes/no):" == "yes" else "Consider completing it when you have free time."

match priority:
    case "high":
        if time_bound == 'yes':
            print(
                f"Reminder: \'{task}\' is a {priority} priority task {time_bound}")
            break
        elif time_bound == "no":
            print(
                f"Note: '{task}' is a {priority} priority task. {time_bound}")
    case "medium":
        if time_bound == 'yes':
            print(
                f"Reminder: \'{task}\' is a {priority} priority task {time_bound}")
            break
        elif time_bound == "no":
            print(
                f"Note: '{task}' is a {priority} priority task. {time_bound}")

    case "low":
        if time_bound == 'yes':
            print(
                f"Reminder: \'{task}\' is a {priority} priority task {time_bound}")
            break
        elif time_bound == "no":
            print(
                f"Note: '{task}' is a {priority} priority task. {time_bound}")
