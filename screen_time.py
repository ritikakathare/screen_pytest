def analyze_screen_time(hours):
    total_time = sum(hours)

    if total_time <= 3:
        category = "Healthy Usage"
        suggestion = "Good job! Maintain balance."
    elif total_time <= 6:
        category = "Moderate Usage"
        suggestion = "Consider reducing screen time."
    else:
        category = "Excessive Usage"
        suggestion = "Take breaks and limit usage."

    return total_time, category, suggestion


if __name__ == "__main__":

    print("====================================")
    print("     Daily Screen Time Analyzer      ")
    print("====================================")

    try:
        try:
            # Try taking user input (works locally)
            n = int(input("Enter number of apps used today: "))
        except EOFError:
            # Jenkins fallback (no input available)
            print("No input detected. Running with default values for CI.")
            n = 3
            hours = [1.5, 2.0, 1.0]

        if n <= 0:
            raise ValueError("Number of apps must be positive")

        if 'hours' not in locals():
            hours = []
            for i in range(1, n + 1):
                h = float(input(f"Enter screen time (hours) for App {i}: "))
                if h < 0:
                    raise ValueError("Screen time cannot be negative")
                hours.append(h)

        total, category, suggestion = analyze_screen_time(hours)

        print("\n--- Screen Time Analysis ---")
        print(f"Total Screen Time : {total:.2f} hours")
        print(f"Usage Category    : {category}")
        print(f"Suggestion        : {suggestion}")

    except ValueError as e:
        print("Input Error:", e)
