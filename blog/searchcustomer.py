def search_customer_in_file(first_name, last_name):
    file_path = 'blog/customername.txt'  # Adjust the file path accordingly
    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) >= 2:
                    file_first_name, file_last_name = data[:2]
                    if file_first_name.lower() == first_name.lower() and file_last_name.lower() == last_name.lower():
                        return line.strip()  # Return the entire line containing the customer details
        return None  # Return None if customer not found
    except FileNotFoundError:
        return None