from utils import helpers
def calculate_reticulocyte_index(reticulocytes, hematocrit, normal_hematocrit=45):
    """
    Berechnet den Retikulozytenindex.
    :param reticulocytes: Retikulozytenzahl in %
    :param hematocrit: Patientenspezifischer Hämatokrit-Wert in %
    :param normal_hematocrit: Normaler Hämatokrit-Wert (Standard: 45%)
    :return: Retikulozytenindex
    """
    return (reticulocytes * hematocrit / normal_hematocrit)
