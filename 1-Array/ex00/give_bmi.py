def give_bmi(height: list[int | float], weight: list[int | float]) -> \
        list[float]:
    """
    Calculate BMI for each person given their height and weight.
    """
    try:
        if len(height) != len(weight):
            raise ValueError

        return [w / (h ** 2) for h, w in zip(height, weight)]
    except TypeError:
        print("Both height and weight should be lists of integers or floats.")
    except ZeroDivisionError:
        print("Height must be greater than zero to calculate BMI.")
    except ValueError:
        print("Height and weight lists must be of the same length.")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if the BMI of each person is greater than the given limit.
    """
    try:
        return [b > limit for b in bmi]
    except TypeError:
        print("BMI list and limit must be integers or floats.")


def main():
    height = [1.75, 1.65, 1.85, 1.55]
    weight = [70, 55, 80, 45]
    bmi = give_bmi(height, weight)
    print(bmi)
    limit = 25
    print(apply_limit(bmi, limit))


if __name__ == "__main__":
    main()
