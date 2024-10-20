# 1번 퀴즈
import random
def lotto():
    result = []
    while len(result) < 6:
        number = random.randint(1,45)
        if number not in result:
            result.append(number)
    return result

result = lotto()
print(f"생선된 로또 번호는{result}입니다.")

# 2번 퀴즈
class gugudan:
    def __init__(self, num):
        self.num = num
    def output(self):
        print(f"---{self.num}단---")
        for dan in range(1, 10):
            print(f"{self.num} x {dan} = {self.num * dan}")

user_input = int(input("구구단을 입력하세요:"))
Gugudan = gugudan(user_input)
Gugudan.output()

# 3번 퀴즈
class Exercise:
    def __init__(self, name, weight, reps):
        self.name = name  # 운동 이름 (예: 벤치프레스)
        self.weight = weight  # 사용한 중량 (kg)
        self.reps = reps  # 반복 횟수

    def calculate_1rm(self):
        # 맷브리키 공식: (중량 * 36) / (37 - 반복횟수)
        return self.weight * 36 / (37 - self.reps)

    def show_info(self):
        # 운동 정보 출력
        return f"운동: {self.name}, 중량: {self.weight} kg, 반복 횟수: {self.reps}"

class Gym:
    def __init__(self):
        self.exercises = []  # 운동 목록을 저장하는 리스트

    def add_exercise(self, exercise):
        # 운동 객체를 리스트에 추가
        self.exercises.append(exercise)

    def calculate_total_1rm(self):
        #모든 운동의 1RM을 합산
        total_1rm = sum(exercise.calculate_1rm() for exercise in self.exercises)
        # <1RM 합산 방법> 각 운동 객체에서 calculate_1rm() 함수를 호출하여 1RM을 계산
        # 1. 운동 객체 생성 ex) exercise = Exercise("벤치프레스,80,5)와 같이 생성
        # 2. 1RM 계산 함수 호출 - calculate_total_1rm 함수 내에서 sum() 함수를 사용하여 1RM 합산
        # 이 과정에서 exercise.calculate_1rm()을 호출하여 계산
        # 3. 맷브리키 공식 적용
        # 4. sum()함수가 각 운동의 1RM 값을 모두 더하여 total_1rm에 저장
        return total_1rm  # 총 1RM 반환
    def show_exercises(self):
        # 운동 목록 출력
        for exercise in self.exercises:
        # self.exercises는 Gym 클래스의 인스턴스가 가지고 있는 운동 목록, for문을 통해 목록에 있는
        # 각 exercise 객체를 하나씩 반복
            print(exercise.show_info())


if __name__ == "__main__":
    # 모듈을 재사용할 때 불필요한 코드 실행을 방지
    gym = Gym()  # Gym 객체 생성

    # 운동 목록에 추가할 운동 이름
    exercises_list = ["벤치프레스", "데드리프트", "스쿼트"]

    for exercise_name in exercises_list:
        # 중량과 반복 횟수 입력
        weight = float(input(f"{exercise_name}의 중량 (kg)을 입력하세요: "))  # 중량 입력
        # 중량은 소수점 이하 값을 가질 수 있기 때문에 int 대신 float 사용
        reps = int(input(f"{exercise_name}의 반복 횟수를 입력하세요: "))  # 반복 횟수 입력

        # Exercise 객체 생성
        exercise = Exercise(exercise_name, weight, reps)
        gym.add_exercise(exercise)  # Gym에 운동 추가

        # 해당 운동의 1RM 계산 및 출력
        print(f"{exercise_name}의 추정 1RM: {exercise.calculate_1rm():.2f} kg\n")
        # <.2f> .:소수점 이하 2: 소수점 이하 2자리 까지 표시 f: float ex)75.12345 값이 75.12로 출력

    # 전체 1RM 계산 및 출력
    total_1rm = gym.calculate_total_1rm()
    print(f"3대 1RM: {total_1rm:.2f} kg")

    print("운동 목록:")
    gym.show_exercises()
