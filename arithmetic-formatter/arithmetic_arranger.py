def arithmetic_arranger(problems, solve = False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    line_1 = []
    line_2 = []
    # Split each arithmetical problem and format checking
    for problem in problems:
        problem = problem.split()
        if ((problem[1] == '-') or (problem[1] == '+')):
            if (problem[0].isnumeric() and problem[2].isnumeric()
              and len(problem[0]) <= 4 and len(problem[2]) <= 4):
                line_1.append(problem[0])
                line_2.append(problem[1:])
            elif len(problem[0]) > 4 or len(problem[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            else:
                return 'Error: Numbers must only contain digits.'
        else:
            return "Error: Operator must be '+' or '-'."
    
    # Get length of each problem
    problem_length = []
    for i in range(len(line_1)):
        length = 2 + len(line_1[i])
        if length < (len(line_2[i][1]) + 2):
            length = len(line_2[i][1]) + 2
        problem_length.append(length)

    arranged_problems = ''
    # Get first line
    for i in range(len(line_1)):
        arranged_problems += (' ' * (problem_length[i] - len(line_1[i]))) + line_1[i]
        if i < (len(line_1) - 1):
            arranged_problems += ' ' * 4

    arranged_problems += '\n'

    # Get second line
    for i in range(len(line_1)):
        arranged_problems += line_2[i][0]
        arranged_problems += (' ' * (problem_length[i] - 1 - len(line_2[i][1])) + (line_2[i][1]))
        if i < (len(line_1) - 1):
            arranged_problems += ' ' * 4
    
    arranged_problems += '\n'

    # Get separator
    for i in range(len(line_1)):
        arranged_problems += '-' * problem_length[i]
        if i < (len(line_1) - 1):
            arranged_problems += ' ' * 4
    
    # Get solutions
    if(solve):
      arranged_problems += '\n'
      for i in range(len(line_1)):
          arranged_problems += operate(int(line_1[i]), line_2[i][0], int(line_2[i][1]), problem_length[i])
          if i < (len(line_1) - 1):
              arranged_problems += ' ' * 4
    
    return arranged_problems

def operate(n1, s, n2, l):
    if s == '+':
        result = str(n1 + n2)
    else:
        result = str(n1 - n2)
    operation = ' ' * (l - len(result)) + result
    return operation