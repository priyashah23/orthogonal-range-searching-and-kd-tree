from unittest import TestCase

from main import construct_kd_tree, search_Kd_tree, KDTreeNode


class Test(TestCase):
    def test_can_handle_a_list_containing_no_points(self):
        list_of_points = []
        kd_tree = construct_kd_tree(list_of_points, 0)
        self.assertEqual(kd_tree, None)

    def test_can_handle_an_empty_tree(self):
        range_list = [(23, 29), (20_000, 25_000)]
        list_in_range = search_Kd_tree(None, range_list, [])
        self.assertEqual(list_in_range, [])

    def test_can_create_a_kd_tree(self):
        # Given
        test_points = [(2, 3000), (5, 4000), (9, 6000), (4, 7000), (8, 1000), (7, 2000)]

        expected_results = KDTreeNode(
            point=(5, 4000),
            left=KDTreeNode(
                point=(5, 4000),
                left=KDTreeNode(
                    point=(2, 3000),
                    left=KDTreeNode(
                        point=(2, 3000),
                        right=None,
                        left=None
                    ),
                    right=KDTreeNode(
                        point=(5, 4000),
                        right=None,
                        left=None
                    )
                ),
                right=KDTreeNode(
                    point=(4, 7000),
                    left=None,
                    right=None
                )
            ),
            right=KDTreeNode(
                point=(7, 2000),
                left=KDTreeNode(
                    point=(7, 2000),
                    left=KDTreeNode(
                        point=(7, 2000),
                        left=None,
                        right=None
                    ),
                    right=KDTreeNode(
                        point=(8, 1000),
                        left=None,
                        right=None
                    )
                ),
                right=KDTreeNode(
                    point=(9, 6000),
                    left=None,
                    right=None
                )
            )
        )

        # When
        tree = construct_kd_tree(test_points, 0)
        print(tree)
        print(expected_results)
        self.assertEqual(tree, expected_results)

    def test_returns_no_list_of_points_if_outside_range(self):
        # Given
        test_points = [(2, 3000), (5, 4000), (9, 6000), (4, 7000), (8, 1000), (7, 2000)]
        range_1 = [(1, 3), (5_000, 10_000)]

        # When
        tree = construct_kd_tree(test_points, 0)
        expected_results = []

        # Then
        results = search_Kd_tree(tree, range_1, [])
        self.assertEqual(results, expected_results)

    def test_another_range(self):
        test_points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
        range_1 = [(2, 6), (4, 9)]
        tree = construct_kd_tree(test_points, 0)
        expected_results = [(5, 4), (4, 7)]

        results = search_Kd_tree(tree, range_1, [])
        self.assertEqual(results, expected_results)

    def test_returns_the_entire_tree(self):
        test_points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
        range = [(1, 10), (1, 8)]
        tree = construct_kd_tree(test_points, 0)
        expected_results = [(2, 3), (5, 4), (4, 7), (7, 2), (8, 1), (9, 6)]

        results = search_Kd_tree(tree, range, [])
        self.assertListEqual(results, expected_results)

    def test_the_partial_range(self):
        # Given
        test_points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
        range_1 = [(2, 5), (3, 7)]

        # When
        tree = construct_kd_tree(test_points, 0)
        expected_results = [(2, 3), (5, 4), (4, 7)]

        # Then
        results = search_Kd_tree(tree, range_1, [])
        self.assertEqual(results, expected_results)
