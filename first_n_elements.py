def output_n_elements(n: int) -> str:
    nums = ''
    if n <= 0:
        return ''
    for i in range(1, n + 1):
        nums += (str(i) * i)
        if len(nums) >= n:
            return nums[:n]


if __name__ == "__main__":
    n = int(input('Введите n: '))
    print(output_n_elements(n))
