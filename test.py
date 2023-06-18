# Prompt the user to input an integer sequence
input_sequence = input("Please input an integer sequence (space-separated): ")

# Split the input sequence by spaces and convert the values to integers
try:
    integer_array = [int(value) for value in input_sequence.split()]
    # Print the array of integers
    print(integer_array)
except ValueError:
    print("Error: Invalid input. Please provide a valid sequence of integers separated by spaces.")