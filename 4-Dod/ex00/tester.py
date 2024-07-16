from statistics import ft_statistics


def main():
    ft_statistics(1, 42, 360, 11, 64, too="mean", pe="median", jo="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ehhe="eh", eejn="kd")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(12, toto="var", tutu="mean", tata="quartile")


if __name__ == "__main__":
    main()
