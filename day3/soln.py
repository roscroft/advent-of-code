import re

def main():
    with open('input.txt', 'r+') as datafile:
        data = datafile.readlines()

    num_regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    data_tups = []
    for item in data:
        num_match = num_regex.match(item)
        nums = num_match.groups()
        data_tups.append(nums)

    def gen_coordinates(left, top, wide, tall):
        coords = set()
        for i in range(left+1, left+wide+1):
            for j in range(top+1, top+tall+1):
                coords.add((i,j))
        return coords

    def part1and2():
        seen_set = set()
        collided_set = set()

        for idx, left, top, wide, tall in data_tups:
            coords = gen_coordinates(int(left), int(top), int(wide), int(tall))
            for coord in coords:
                if coord in seen_set:
                    collided_set.add(coord)
                else:
                    seen_set.add(coord)

        print(len(collided_set))

        for idx, left, top, wide, tall in data_tups:
            coords = gen_coordinates(int(left), int(top), int(wide), int(tall))
            collided = False
            for coord in coords:
                if coord in collided_set:
                    collided = True
                    continue
            if collided == False:
                return idx

    print(part1and2())
if __name__ == "__main__":
    main()
