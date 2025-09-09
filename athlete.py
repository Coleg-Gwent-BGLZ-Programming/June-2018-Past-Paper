def validate_time_input(time_str):
    try:
        time = float(time_str)
        if time <= 0:
            raise ValueError("Time must be positive.")
        return round(time, 2)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid positive number for time.")

def check_records(gender, time):
    records = {
        "male": {"WR": 9.58, "ER": 9.86, "BR": 9.87},
        "female": {"WR": 10.49, "ER": 10.73, "BR": 10.99}
    }
    alerts = []
    for record, value in records[gender].items():
        if time <= value:
            alerts.append(record)
    return alerts

def get_valid_gender():
    while True:
        gender = input("Enter gender of athletes (male/female): ").strip().lower()
        if gender in ["male", "female"]:
            return gender
        print("Invalid gender. Please enter 'male' or 'female'.")

def get_valid_athlete_count():
    while True:
        try:
            num = int(input("Enter number of athletes (4 to 8): "))
            if 4 <= num <= 8:
                return num
            else:
                print("Number must be between 4 and 8.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_valid_time(lane_number):
    while True:
        time_str = input(f"Enter time for athlete in lane {lane_number} (in seconds, e.g. 9.58): ")
        try:
            return validate_time_input(time_str)
        except ValueError as e:
            print(e)

def record_race_times():
    gender = get_valid_gender()
    num_athletes = get_valid_athlete_count()

    athlete_times = []
    for i in range(1, num_athletes + 1):
        time = get_valid_time(i)
        athlete_times.append((i, time))  # Store athlete number and time

    sorted_times = sorted(athlete_times, key=lambda x: x[1])
    print("\n🏁 Race Results (Fastest to Slowest):")
    for athlete_num, time in sorted_times:
        print(f"Athlete {athlete_num}: {time:.2f}s")
        alerts = check_records(gender, time)
        for alert in alerts:
            print(f"🚨 ALERT: Athlete {athlete_num} broke the {alert} record with time {time:.2f}s!")

# Run the program
record_race_times()
