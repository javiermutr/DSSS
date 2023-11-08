import random


def function_A(min, max):
    """
    Random integer.
    All values needs to be int
    """
    return random.randint(min, int(max))


def function_B():
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, operator):
    problem = f"{n1} {operator} {n2}"
    if operator == '+': answer = n1 + n2
    elif operator == '-': answer = n1 - n2
    else: answer = n1 * n2
    return problem, answer

def math_quiz():
    score = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):
        n1 = function_A(1, 10); n2 = function_A(1, 5.5); operator = function_B()

        problem, answer = function_C(n1, n2, operator)
        print(f"\nQuestion: {problem}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
    math_quiz()