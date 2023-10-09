import datetime

def valid_date(date_str):
    try:
        # Try to parse the date using datetime.strptime
        datetime.datetime.strptime(date_str, "%B %d, %Y")
        return True
    except ValueError:
        return False


def main(input_source):
    current_date = datetime.datetime.now()

    while True:
        date_str = input_source.readline().strip()

        if date_str == "-1":
            break

        if valid_date(date_str):
            date_obj = datetime.datetime.strptime(date_str, "%B %d, %Y")

            if date_obj <= current_date:
                formatted_date = date_obj.strftime("%m/%d/%Y")
                print(formatted_date)



if __name__ == "__main__":
    print("Enter the dates in the format 'Month Day, Year' (ex: March 1, 1990)")
    print("Enter -1 to end the input")
    input_source = input # To call the function
    input_file = "inputDates.txt" # File to be reading
    input_source = open(input_file, 'r') # Opening the file to read

    main(input_source)

    input_source.close()