import itertools

def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve(equation):
    left, right = equation.lower().replace(' ', '').split('=')
    left = left.split('+')
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)


    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            values_left = [str(get_value(word, sol)) for word in left]
            value_right = get_value(right, sol)
            result = ' + '.join(values_left) + " = {} (mapping: {})".format(value_right, sol)
            print(result)

if __name__ == '__main__':
    solve('D A Y S + T O O=S H O R T ')