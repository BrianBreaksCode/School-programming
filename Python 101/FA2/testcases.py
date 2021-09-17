import functies

test_cases = [[11, False, 40], [12, False, 40], [64, False, 40], [65, False, 40], [11, True, 40], [12, True, 40],
            [64, True, 40], [65, True, 40], [11, False, 60], [12, False, 60], [64, False, 60], [65, False, 60],
            [11, True, 60], [12, True, 60], [64, True, 60], [65, True, 60], [11, False, -10], [12, False, -10],
            [64, False, -10], [65, False, -10], [11, True, -10], [12, True, -10], [64, True, -10], [65, True, -10]]

for test_count in test_cases:
    print(f"€{functies.ritprijs(*test_count)}")
