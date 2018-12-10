from functools import reduce

def main():
    with open('input.txt', 'r+') as datafile:
        data = datafile.readlines()

    def manhattan(coord_1, coord_2):
        return abs(int(coord_1[0]) - int(coord_2[0])) + abs(int(coord_1[1]) - int(coord_2[1]))

    def argmin(distances):
        min_idx = 0
        min_dist = 100000000000
        seen = False
        for idx, dist in distances:
            if dist == min_dist:
                seen = True
            if dist < min_dist:
                min_dist = dist
                min_idx = idx
                seen = False
        if seen:
            return None
        return min_idx

    def get_distances(coord, area_dict):
        distances = []
        for key, value in area_dict.items():
            ref_point = [value["x"], value["y"]]
            distances.append((key, manhattan(coord, ref_point)))
        return distances

    def elementwise_more(list_1, list_2):
        for i in range(len(list_1)):
            if list_1[i] < list_2[i]:
                return False
        return True

    def tuplesum(tup_lst):
        return sum(n for _, n in tup_lst)

    def part1(data):
        area_dict = {}
        idx = 0
        for item in data:
            coords = item.strip().split(", ")
            area_dict[idx] = {"x": coords[0], "y": coords[1], "area": 0, "inf": False}
            idx += 1

        start = (0, 0)
        coord_dict = {}
        to_explore = set()
        explored = set()
        to_explore.add(start)
        explored.add(start)
        last_distances = get_distances(start, area_dict)
        coord_dict[start] = last_distances
        closest_point = argmin(last_distances)
        area_dict[closest_point]["area"] += 1

        while to_explore:
            cur = to_explore.pop()
            last_distances = coord_dict[cur]
            coord_dict.pop(cur)

            up = (cur[0], cur[1]+1)
            down = (cur[0], cur[1]-1)
            left = (cur[0]-1, cur[1])
            right = (cur[0]+1, cur[1])
            for direction in [up, down, left, right]:
                if direction not in explored:
                    new_distances = get_distances(direction, area_dict)
                    closest_point = argmin(new_distances)
                    if elementwise_more(new_distances, last_distances):
                        if closest_point is not None:
                            area_dict[closest_point]["inf"] = True
                    else:
                        if closest_point is not None:
                            area_dict[closest_point]["area"] += 1
                        to_explore.add(direction)
                        coord_dict[direction] = new_distances
                    explored.add(direction)

        max_area = 0
        for key, value in area_dict.items():
            area = value["area"]
            is_inf = value["inf"]
            if area > max_area and not is_inf:
                max_area = area

        return max_area

    def part2(data):
        area_dict = {}
        idx = 0
        for item in data:
            coords = item.strip().split(", ")
            area_dict[idx] = {"x": coords[0], "y": coords[1], "area": 0}
            idx += 1

        part2_size = 0
        start = (0, 0)
        coord_dict = {}
        to_explore = set()
        explored = set()
        to_explore.add(start)
        explored.add(start)
        last_distances = get_distances(start, area_dict)
        print(last_distances)
        print(tuplesum(last_distances))
        if tuplesum(last_distances) < 10000:
            part2_size += 1
        coord_dict[start] = last_distances
        closest_point = argmin(last_distances)
        area_dict[closest_point]["area"] += 1

        while to_explore:
            cur = to_explore.pop()
            last_distances = coord_dict[cur]
            coord_dict.pop(cur)

            up = (cur[0], cur[1]+1)
            down = (cur[0], cur[1]-1)
            left = (cur[0]-1, cur[1])
            right = (cur[0]+1, cur[1])
            for direction in [up, down, left, right]:
                if direction not in explored:
                    new_distances = get_distances(direction, area_dict)
                    closest_point = argmin(new_distances)
                    if elementwise_more(new_distances, last_distances):
                        if closest_point is not None:
                            area_dict[closest_point]["inf"] = True
                        if tuplesum(new_distances) < 10000:
                            part2_size += 1
                    else:
                        if closest_point is not None:
                            area_dict[closest_point]["area"] += 1
                        if tuplesum(new_distances) < 10000:
                            part2_size += 1
                        to_explore.add(direction)
                        coord_dict[direction] = new_distances
                    explored.add(direction)

        return part2_size

    print(part2(data))
if __name__ == "__main__":
    main()
