import math

age = [18, 22, 24, 29, 31, 25, 23, 20, 21]
salary = [18_000, 17_500, 22_000, 30_000, 24_000, 19_000, 25_000, 20_000, 19_500]

class KDTreeNode:
    def __init__(self, point: tuple, left, right):
        self.point = point
        self.left = left
        self.right = right

    def __str__(self):
        return f"point: {self.point}, left: {self.left}, right:{self.right}"
def construct_kd_tree(points: list, depth: int) -> KDTreeNode:
    points.sort(key=lambda tup: tup[len(points) % 2])
    if len(points) == 1:
        return KDTreeNode(points[0], None, None)
    else:
        if depth % 2 == 0:
            l = math.ceil(len(points) / 2)
            p1 = points[:l]
            p2 = points[l:]
        else:
            l = math.ceil(len(points) / 2)
            p1 = points[:l]
            p2 = points[l:]
        left_branch = construct_kd_tree(p1, depth+1)
        right_branch = construct_kd_tree(p2, depth+1)
        return KDTreeNode(points[l], left_branch, right_branch)

def search_Kd_tree(root: KDTreeNode, range_list: list, list_of_points: list) -> list:
    if root.left is None and root.right is None:
        if (range_list[0][0] <= root.point[0] <= range_list[0][1]) and (range_list[1][0] <= root.point[1] <= range_list[1][1]):
            list_of_points.append(root.point)
    else:
        if is_fully_contained(root, root.left, range_list):
            list_of_points += report_subtree(root.left)
        else:
            if does_intersect_with_range(root, root.left, range_list):
                search_Kd_tree(root.left, range_list, list_of_points)
        if is_fully_contained(root, root.right, range_list):
            list_of_points += report_subtree(root.right)
        else:
            if does_intersect_with_range(root, root.left, range_list):
                search_Kd_tree(root.right, range_list, list_of_points)
    return list_of_points
def is_fully_contained(root:KDTreeNode, subtree: KDTreeNode, range_list: list) -> bool:
    return ((min(root.point[0], subtree.point[0]) >= range_list[0][0] and max(root.point[0], subtree.point[0]) <= range_list[0][1])
            and (min(root.point[1], subtree.point[1]) >= range_list[1][0] and max(root.point[1], subtree.point[1]) <= range_list[1][1]))
def does_intersect_with_range(root:KDTreeNode, subtree: KDTreeNode, range_list: list) -> bool:
    return ((min(root.point[0], subtree.point[0]) >= range_list[0][0] or max(root.point[0], subtree.point[0]) <=
             range_list[0][1])
            or (min(root.point[1], subtree.point[1]) >= range_list[1][0] or max(root.point[1], subtree.point[1]) <=
                 range_list[1][1]))
def report_subtree(subtree: KDTreeNode, list_of_points=[]) -> list:
    if subtree.left is None and subtree.right is None:
        list_of_points.append(subtree.point)
    else:
        report_subtree(subtree.left, list_of_points)
        report_subtree(subtree.right, list_of_points)
    return list_of_points

if __name__ == '__main__':
    points = list(zip(age, salary))
    kd_tree = construct_kd_tree(points, 0)
    range_list = [(23, 29), (20_000, 25_000)]
    list_of_points = search_Kd_tree(kd_tree, range_list, [])
    print(list_of_points)