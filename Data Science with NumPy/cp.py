from point import Point


def closestPoint(s, p):
    """Returns the subset of points in s that are closest to point p."""
    if not s:
        return set()

    # Compute distances and find the minimum distance
    min_dist = min(p.distance_from(pt) for pt in s)

    # Return the subset of points at the minimum distance
    return {pt for pt in s if p.distance_from(pt) == min_dist}


if __name__ == "__main__":

    def test(s, p):
        ans = closestPoint(s, p)
        # We'll turn the set into a sorted list before
        # we print it to avoid any issues with what order things
        # are in
        sorted_ans = sorted(ans, key=lambda p: (p.x, p.y))
        print(sorted_ans)
        pass

    p1 = Point()
    p2 = Point(3, 4)
    p3 = Point(-3, 4)
    p4 = Point(3, -4)
    p5 = Point(1, 9)
    p6 = Point(8, 2)
    p7 = Point(-2, -5)
    p8 = Point(-6, 8)
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    for i in range(0, len(points)):
        s = set(points[:i]).union(set(points[i + 1 :]))
        test(s, points[i])
        pass
    # check that empty set gives empty set
    test({}, p1)
    # if the target point is in the list, we should get that point itself
    test(set(points), p5)
