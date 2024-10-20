import random
def lotto():
    results = []
    while len(results) < 6:
        number = random.randint(1,45)
        if number not in results:
            results.append(number)
    results.sort()
    return results

results = lotto()
print(f"생성된 로또 번호는 {results}입니다.")

