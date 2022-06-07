def merge_notch_list(notch_list_1, notch_list_2):
    """Merge two notches list

    Parameters
    ----------
    notch_list_1 : list
        First notch list to merge
    notch_list_2 : list
        Second notch list to merge

    Returns
    -------
    notch_list : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    """
    N1 = len(notch_list_1)
    N2 = len(notch_list_2)

    merged = []
    ii, jj = 0, 0  # Index to go thought the lists

    while ii < N1 and jj < N2:
        if (
            notch_list_1[ii]["begin_angle"] < notch_list_2[jj]["begin_angle"]
            and notch_list_1[ii]["end_angle"] <= notch_list_2[jj]["begin_angle"]
        ):  # Add a notch from notch_list_1
            merged.append(notch_list_1[ii])
            ii += 1
        elif (
            notch_list_2[jj]["begin_angle"] < notch_list_1[ii]["begin_angle"]
            and notch_list_2[jj]["end_angle"] <= notch_list_1[ii]["begin_angle"]
        ):  # Add a notch from notch_list_2
            merged.append(notch_list_2[jj])
            jj += 1
        else:
            raise NotchError(
                "Notches and/or Slots are colliding"
            )

    # One of the list is not "finished"
    merged = merged + notch_list_1[ii:] + notch_list_2[jj:]

    return merged


class NotchError(Exception):
    """Raised when notch are coliding"""

    pass
