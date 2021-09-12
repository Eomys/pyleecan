from ....Methods.Machine.Lamination import LaminationCheckError


class Lam_SlotCheckError(LaminationCheckError):
    """ """

    pass


class LSC_OutSlotInLam(Lam_SlotCheckError):
    """ """

    pass


class LSC_InSlotOutLam(Lam_SlotCheckError):
    """ """

    pass


class LSC_SlotTooLong(Lam_SlotCheckError):
    """ """

    pass


class LSC_OverlappingSlot(Lam_SlotCheckError):
    """ """

    pass
