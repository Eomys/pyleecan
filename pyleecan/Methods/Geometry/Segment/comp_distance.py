from numpy import sqrt, array
from numpy import arccos, array, dot, pi, cross
from numpy.linalg import det, norm


def distance_numpy(A, B, P):
    # from: https://gist.github.com/nim65s/5e9902cd67f094ce65b0
    """segment line AB, point P, where each one is an array([x, y])"""
    if all(A == P) or all(B == P):
        return 0
    if arccos(dot((P - A) / norm(P - A), (B - A) / norm(B - A))) > pi / 2:
        return norm(P - A)
    if arccos(dot((P - B) / norm(P - B), (A - B) / norm(A - B))) > pi / 2:
        return norm(P - B)
    return norm(cross(A - B, A - P)) / norm(B - A)


def comp_distance(self, Z):
    """Compute the distance of a point to the Segment

    Parameters
    ----------
    self : Segment
        A Segment object
    Z : complex
        Complex coordinate of the point

    Returns
    -------
    D : float
        distance of a point to the Segment
    """

    Z1 = array([self.begin.real, self.begin.imag])
    Z2 = array([self.end.real, self.end.imag])
    Z3 = array([Z.real, Z.imag])
    return distance_numpy(Z1, Z2, Z3)
