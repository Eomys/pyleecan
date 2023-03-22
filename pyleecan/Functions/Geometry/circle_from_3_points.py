from numpy import sqrt


def circle_from_3_points(Z1, Z2, Z3):
    """Return the center and radius of a circle defined by 3 points

    Parameters:
    -----------
    Z1 : complex
        First point coordinates
    Z2 : complex
        Second point coordinates
    Z3 : complex
        Third point coordinates

    Returns:
    --------
    R : float
        Radius of the circle [m]
    Zc : complex
        Coordinate of the circle center
    """

    if Z1.imag == Z2.imag and Z1.imag == Z3.imag:
        raise Exception("Error: The 3 points are aligned !")
    if Z1.real == Z2.real and Z1.real == Z3.real:
        raise Exception("Error: The 3 points are aligned !")

    # Avoid div by 0
    if Z3.imag == Z1.imag:
        # Change Z1 and Z2
        tmp = Z2
        Z2 = Z1
        Z1 = tmp

    X1 = Z1.real
    Y1 = Z1.imag

    X2 = Z2.real
    Y2 = Z2.imag

    X3 = Z3.real
    Y3 = Z3.imag

    # All three points are on the circle :
    # (X1-Xc)² + (Y1-Yc)² - R² =0  (Eq1)
    # (X2-Xc)² + (Y2-Yc)² - R² =0  (Eq2)
    # (X3-Xc)² + (Y3-Yc)² - R² =0  (Eq3)

    # (Eq1-Eq2)
    # (X1² -2*X1*Xc + Xc² + Y1² -2*Y1*Yc + Yc² - R²) - (X2² -2*X2*Xc + Xc² + Y2² -2*Y2*Yc + Yc² - R²) = 0
    # X1² - X2² + 2*(X2-X1)*Xc + Y1² - Y2² + 2*(Y2-Y1)*Yc = 0

    # (Eq1-Eq3)
    # X1² - X3² + 2*(X3-X1)*Xc + Y1² - Y3² + 2*(Y3-Y1)*Yc = 0
    # Yc = (-X1² + X3² - 2*(X3-X1)*Xc - Y1² + Y3²)/2*(Y3-Y1)

    # Yc into (Eq1-Eq2)
    # X1² - X2² + 2*(X2-X1)*Xc + Y1² - Y2² + 2*(Y2-Y1)*(-X1² + X3² - 2*(X3-X1)*Xc - Y1² + Y3²)/2*(Y3-Y1)= 0
    # A = (Y2-Y1)/(Y3-Y1)
    # -X1² + X2² - Y1² + Y2² = 2*(X2-X1)*Xc  + A(-X1² + X3² - 2*(X3-X1)*Xc - Y1² + Y3²)
    # -X1² + X2² - Y1² + Y2² + A(X1² -X3² +Y1² -Y3²) = 2*(X2-X1)*Xc - 2*A*(X3-X1)*Xc
    A = (Y2 - Y1) / (Y3 - Y1)
    Xc = (
        -(X1 ** 2)
        + X2 ** 2
        - Y1 ** 2
        + Y2 ** 2
        + A * (X1 ** 2 - X3 ** 2 + Y1 ** 2 - Y3 ** 2)
    ) / (2 * (X2 - X1) - 2 * A * (X3 - X1))

    # Eq1-Eq3
    Yc = (-(X1 ** 2) + X3 ** 2 - 2 * (X3 - X1) * Xc - Y1 ** 2 + Y3 ** 2) / (
        2 * (Y3 - Y1)
    )

    # Eq1
    R = sqrt((X1 - Xc) ** 2 + (Y1 - Yc) ** 2)

    return (R, Xc + 1j * Yc)
