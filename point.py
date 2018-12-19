from curve import EllipticCurve

class Point(object):

    """
      This class represents a point on the given Elliptic Curve
    """

    def __init__(self, curve, x, y):
        self.curve = curve  # the curve containing this point
        self.x = x
        self.y = y

        if not curve.testPoint(x, y):
            raise Exception("The point %s is not on the given curve %s" % (self, curve))

    def __add__(self, other):
        if isinstance(other, Ideal):
            return self

        x_1, y_1, x_2, y_2 = self.x, self.y, other.x, other.y

        if (x_1, y_1) == (x_2, y_2):
            # use the tangent method
            ...
        else:
            if x_1 == x_2:
                return Ideal(self.curve)  # vertical line

            # Using Vieta's formula for the sum of the roots
            m = (y_2 - y_1) / (x_2 - x_1)
            x_3 = m * m - x_2 - x_1
            y_3 = m * (x_3 - x_1) + y_1

            return Point(self.curve, x_3, -y_3)
