import math
import matplotlib.pyplot as plt


age = [18, 22, 24, 29, 31, 25, 23, 22, 21]
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

def search_Kd_tree(root: KDTreeNode, range_list: list, list_of_points):
    pass
def region_search(subtree: KDTreeNode, range_list: list, full: bool) -> bool:
    pass
def report_subtree(subtree: KDTreeNode, list_of_points=[]) -> list:
    pass

if __name__ == '__main__':
    points = list(zip(age, salary))
    kd_tree = construct_kd_tree(points, 0)
    print(kd_tree)
    range_list = [(23, 29), (20_000, 25_000)]
    # points_in_range = search_Kd_tree(kd_tree, range_list, [])
    # print(points_in_range)
    plt.scatter(age, salary)
    plt.axvline(24)
    plt.show()
