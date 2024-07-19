def solution(binomial):
    answer = 0
    binomial_divi = binomial.split(' ')
    if binomial_divi[1] == '+':
        answer = int(binomial_divi[0]) + int(binomial_divi[2])
    elif binomial_divi[1] == '-':
        answer = int(binomial_divi[0]) - int(binomial_divi[2])
    elif binomial_divi[1] == '*':
        answer = int(binomial_divi[0]) * int(binomial_divi[2])
    elif binomial_divi[1] == '/':
        answer = int(binomial_divi[0]) / int(binomial_divi[2])
    return answer