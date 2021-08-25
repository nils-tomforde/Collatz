import matplotlib.pyplot as plt


def main():
    sequence = collatz_sequence(73483, 100)
    plot_sequence(sequence)

    return None


def collatz_sequence(starting_value, length):
    sequence = [starting_value]
    for i in range(length):
        if sequence[i] % 2 == 0:
            sequence.append(int(sequence[i]/2))
        else:
            sequence.append(sequence[i]*3 + 1)

    print(sequence)

    return sequence


def plot_sequence(sequence):
    plt.plot(sequence)
    plt.ylabel("Zahlen")
    plt.show()

    return None


if __name__ == "__main__":
    main()