import datetime

def valid_date(date_str):
    try:
        # Try to parse the date using datetime.strptime
        datetime.datetime.strptime(date_str, "%B %d, %Y")
        return True
    except ValueError:
        return False


def main():
    current_date = datetime.datetime.now()

    while True:
        # Where the date is to be inputted
        date_str = input_file
        # Until -1 is inputted, the program will keep parsing
        if date_str == "-1":
            break
        # Converts date to proper format
        if valid_date(date_str):
            date_obj = datetime.datetime.strptime(date_str, "%B %d, %Y")
        # Prevents future dates from being processed
            if date_obj <= current_date:
                formatted_date = date_obj.strftime("%m/%d/%Y")
                print(formatted_date)
            else:
                print("Date is in the future. Ignoring it.")
        else:
            print("Invalid date format. Please enter a date in the format: Month Day, Year")


if __name__ == "__main__":
    main()
