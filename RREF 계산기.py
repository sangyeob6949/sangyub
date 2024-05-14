def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]
def scale_row(matrix, i, scale):
    matrix[i] = [element * scale for element in matrix[i]]
def add_row(matrix, i, j, scale):
    matrix[i] = [a + b * scale for a, b in zip(matrix[i], matrix[j])]
def rref(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    lead = 0
    pivot_variables = []
    free_variables = []

    for r in range(num_rows):
        if lead >= num_cols:
            break
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == num_rows:
                i = r
                lead += 1
                if num_cols == lead:
                    break
        if lead >= num_cols:
            break

        swap_rows(matrix, i, r)
        scale_row(matrix, r, 1 / matrix[r][lead])

        pivot_variables.append(lead)
        for i in range(num_rows):
            if i != r:
                add_row(matrix, i, r, -matrix[i][lead])

        lead += 1

    for i in range(num_cols):
        if i not in pivot_variables:
            free_variables.append(i)

    return pivot_variables, free_variables

def print_matrix(matrix):
    for row in matrix:
        print(" | ".join(map(lambda x: f"{x:.2f}", row)))

def main():
    # 행렬의 크기 입력 받음
    rows, cols = map(int, input("행렬의 행과 열의 크기를 입력하세요: ").split())

    # 행렬 요소 입력 받음
    print("행렬의 요소를 한 줄씩 입력하세요:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    # rref 계산
    pivot_variables, _ = rref(matrix)
    # 변수 이름 설정
    variables = [f"X{i + 1}" for i in range(cols)]
    # 결과 출력
    print("Reduced Row Echelon Form (rref):")
    print_matrix(matrix)
    if not pivot_variables:
        print("이 행렬에는 피벗 변수도 자유 변수도 없습니다.")
    else:
        print("피벗 변수 및 자유 변수:")
        for i, variable in enumerate(variables):
            if i in pivot_variables:
                print(f"{variable} (피벗 변수)")
            else:
                print(f"{variable} (자유 변수)")


if __name__ == "__main__":
    main()


