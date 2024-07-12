import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Given a 2D list, return a new 2D list that
    is a slice of the original list
    """
    try:

        if not isinstance(family, list) or not \
                all(isinstance(row, list) for row in family):
            raise ValueError("Input must be a list of lists")

        row_length = len(family[0])
        print(([len(row) == row_length for row in family]))
        if not all(len(row) == row_length for row in family):
            raise ValueError("All rows must have the same length")

        family_array = np.array(family)

        initial_shape = family_array.shape
        print(f"My shape is : {initial_shape}")

        truncated_family = family_array[start:end]

        new_shape = truncated_family.shape
        print(f"My new shape is : {new_shape}")

        return truncated_family.tolist()

    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
