import re

def max_idx(lst):
    max_idx = 0
    max_item = 0
    for idx, item in enumerate(lst):
        if item > max_item:
            max_item = item
            max_idx = idx
    return max_idx

def main():
    with open('input.txt', 'r+') as datafile:
        data = datafile.readlines()

    def reacts(char_1, char_2):
        return (char_1 != char_2) and (char_1.lower() == char_2.lower())

    def part1(inputlst):
        work_idx = 0
        while work_idx < len(inputlst)-1:
            if reacts(inputlst[work_idx], inputlst[work_idx+1]):
                inputlst.pop(work_idx)
                inputlst.pop(work_idx)
                work_idx -= 1
            else:
                work_idx += 1
        return len(inputlst)

    def part2():
        inputstr = data[0].strip()
        inputlst = [x for x in inputstr]

        alphabetstr = 'abcdefghijklmnopqrstuvwxyz'
        alphabetlst = [x for x in alphabetstr]

        least_letter_amount = 1000000000
        for letter in alphabetlst:
            newlst = [x for x in inputlst if x not in [letter, letter.upper()]]
            letter_amount = part1(newlst)
            if letter_amount < least_letter_amount:
                least_letter_amount = letter_amount

        return least_letter_amount

    print(part2())

if __name__ == "__main__":
    main()
