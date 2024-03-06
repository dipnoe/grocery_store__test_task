def output_n_elements(n: int) -> str:
    nums = ''
    for i in range(1, n + 1):
        nums += (str(i) * i)
    return nums


if __name__ == "__main__":
    n = int(input())
    print(output_n_elements(n))
