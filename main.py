def find_rank(dataset, value):
    sorted_dataset = sorted(dataset, reverse=True)
    try:
        rank = sorted_dataset.index(value) + 1
        print(f"The rank of {value} is {rank}.")
    except ValueError:
        print(f"{value} is not in the dataset.")

# Read input from the user
dataset_input = input( )
value_input = input()

# Convert the inputs to appropriate types
dataset = list(map(int, dataset_input.split()))
value = int(value_input)

find_rank(dataset, value)