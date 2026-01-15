months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date_input = input("Date: ").strip()

            # Format: MM/DD/YYYY
            if "/" in date_input:
                month, day, year = date_input.split("/")
                month = int(month)
                day = int(day)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    continue

            # Format: Month Day, Year  ← MUST include a comma
            elif "," in date_input:
                month_name, rest = date_input.split(" ", 1)
                day, year = rest.replace(",", "").split()

                month_name = month_name.capitalize()

                if month_name in months:
                    month_number = months.index(month_name) + 1
                    day = int(day)
                    if 1 <= day <= 31:
                        print(f"{year}-{month_number:02}-{day:02}")
                        break
                # if invalid month/day → reprompt
                else:
                    continue

            else:
                continue

        except ValueError:
            continue

if __name__ == "__main__":
    main()