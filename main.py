import math
from menu import *
import csv
def read_csv() -> list:
    list_of_points = []
    with open('employees.csv', newline='') as csvfile:
        line = csv.reader(csvfile, delimiter=',')
        next(line, None)  # skip the headers
        for element in line:
            list_of_points.append((int(element[0]), int(element[1])))
    return list_of_points



class KDTreeNode:
    """
    Class that represents a K-d tree node
    """
    def __init__(self, point: tuple, left, right):
        """
        Initialises a kd node
        :param point: The point it holds
        :param left: The left child, if it is a leaf node holds None
        :param right: The right child, if it is a leaf node holds None
        """
        self.point = point
        self.left = left
        self.right = right

    def __str__(self):
        """
        Returns a string
        :return:  The string version of a k-d node object
        """
        return f"point: {self.point}, left: {self.left}, right:{self.right}"

    def __eq__(self, other):
        return self.point == other.point


def construct_kd_tree(points: list, depth: int) -> KDTreeNode:
    """
    This function recursively constructs a k-d tree
    :param points: A list of points
    :param depth: The current depth of the tree
    :return: The head of the k-d Tree
    """
    if len(points) == 0:
        return None
    points.sort(key=lambda tup: tup[depth % 2])
    if len(points) == 1:
        return KDTreeNode(points[0], None, None)
    else:
        l = math.ceil(len(points) / 2)
        p1 = points[:l]
        p2 = points[l:]
        left_branch = construct_kd_tree(p1, depth + 1)
        right_branch = construct_kd_tree(p2, depth + 1)
        return KDTreeNode(points[l - 1], left_branch, right_branch)


def search_Kd_tree(root: KDTreeNode, range_list: list, list_of_points: list) -> list:
    """
    Searches a k-d tree for nodes that are contained in the range_list
    :param root:
    :param range_list:
    :param list_of_points:
    :return:
    """
    if root is None:
        return []
    if root.left is None and root.right is None:
        if (range_list[0][0] <= root.point[0] <= range_list[0][1]) and (
                range_list[1][0] <= root.point[1] <= range_list[1][1]):
            list_of_points.append(root.point)
    else:
        if is_fully_contained(root, root.left, range_list):
            list_of_points += report_subtree(root.left, range_list, [])
        elif does_intersect_with_range(root, root.left, range_list):
            search_Kd_tree(root.left, range_list, list_of_points)

        if is_fully_contained(root, root.right, range_list):
            list_of_points += report_subtree(root.right, range_list, [])
        elif does_intersect_with_range(root, root.right, range_list):
            search_Kd_tree(root.right, range_list, list_of_points)
    return list_of_points


def is_fully_contained(root: KDTreeNode, subtree: KDTreeNode, range_list: list) -> bool:
    return ((min(root.point[0], subtree.point[0]) >= range_list[0][0] and max(root.point[0], subtree.point[0]) <=
             range_list[0][1])
            and (min(root.point[1], subtree.point[1]) >= range_list[1][0] and max(root.point[1], subtree.point[1]) <=
                 range_list[1][1]))


def does_intersect_with_range(root: KDTreeNode, subtree: KDTreeNode, range_list: list) -> bool:
    return ((min(root.point[0], subtree.point[0]) >= range_list[0][0] or max(root.point[0], subtree.point[0]) <=
             range_list[0][1])
            or (min(root.point[1], subtree.point[1]) >= range_list[1][0] or max(root.point[1], subtree.point[1]) <=
                range_list[1][1]))


def report_subtree(subtree: KDTreeNode, range_list, list_of_points=[]) -> list:
    if subtree.left is None and subtree.right is None:
        if (range_list[0][0] <= subtree.point[0] <= range_list[0][1]) and (
                range_list[1][0] <= subtree.point[1] <= range_list[1][1]):
            list_of_points.append(subtree.point)
    else:
        report_subtree(subtree.left, range_list, list_of_points)
        report_subtree(subtree.right, range_list, list_of_points)
    return list_of_points


if __name__ == '__main__':
    DEPTH = 0
    points = read_csv()
    if select_options() == 1:
        range_list = [(23, 29), (20_000, 25_000)]
    else:
        range_list = user_input_range()
    kd_tree = construct_kd_tree(points, DEPTH)
    list_of_points = search_Kd_tree(kd_tree, range_list, [])
    print("The points returned from the range search: ", list_of_points)
