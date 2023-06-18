# Split the input sequence by spaces and validate the values
def validate(input_sequence):
    integer_array = []
    try:
        integer_array = [int(value) for value in input_sequence.split()]
        return integer_array
    except ValueError:
        print("Error: Invalid input. Please provide a valid sequence of integers separated by spaces.")
        return


# Predict the next ten integers based on the input sequence
def predict_next_integers(integer_array):
    prediction = []
    if len(integer_array) >= 2:
        diff = integer_array[-1] - integer_array[-2]  # Calculate the difference between the last two integers
        next_integer = integer_array[-1] + diff  # Predict the next integer based on the difference

        for _ in range(10):
            prediction.append(next_integer)
            next_integer += diff

    return prediction


def main():
    # Prompt the user to input an integer sequence
    input_sequence = input("Please input an integer sequence (space-separated): ")

    integer_array = validate(input_sequence)
    prediction = predict_next_integers(integer_array)

    # Print the prediction
    if prediction:
        print("Predicted next ten integers:", " ".join(map(str, prediction)))

if __name__ == '__main__':
    main()