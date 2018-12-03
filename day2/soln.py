from functools import reduce

def main():
    with open('day2input.txt', 'r+') as datafile:
        data = datafile.readlines()

    def part1():
        total_2 = 0
        total_3 = 0
        for item in data:
            item = item.strip()
            data_dict = {}
            set_2 = False
            set_3 = False
            for char in item:
                data_dict[char] = data_dict.get(char, 0) + 1
            for char in item:
                if data_dict[char] == 2 and not set_2:
                    total_2 += 1
                    set_2 = True
                elif data_dict[char] == 3 and not set_3:
                    total_3 += 1
                    set_3 = True
        return total_2*total_3

    def part2():
        for item1 in data:
            for item2 in data:
                diff_1_and_ind = [(item1[i], i) for i in range(len(item1)) if item1[i] != item2[i]]
                diff_2_and_ind = [(item2[i], i) for i in range(len(item2)) if item2[i] != item1[i]]
                
                if len(diff_1_and_ind) == 1 and len(diff_2_and_ind) == 1:
                    ind = diff_1_and_ind[0][1]
                    item1 = item1[:ind] + item1[ind+1:]
                    return item1

    print(part2())
if __name__ == "__main__":
    main()
