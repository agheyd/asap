def significant_miso(x):

    if ((x.miso_dpsi >= 0.1) or (x.miso_dpsi <= -0.1)) and (x.miso_bf > 5):
        return "yes"
    else:
        return "no"

    return None

def significant_rmats(x):

    if ((x.rmats_dpsi >= 0.1) or (x.rmats_dpsi <= -0.1)) and (x.rmats_fdr <= 0.1):
        return "yes"
    else:
        return "no"

    return None

def significant_whippet(x):

    if ((x.whippet_dpsi >= 0.1) or (x.whippet_dpsi <= -0.1)) and (x.whippet_prob >= 0.9):
        return "yes"
    else:
        return "no"

    return None

def define_group(x):

    if ((x.miso_significant == "yes") and
        (x.rmats_significant == "yes") and
        (x.whippet_significant == "yes")):
        return "mrw"
    elif ((x.miso_significant == "yes") and
          (x.rmats_significant == "yes") and
          (x.whippet_significant == "no")):
        return "mr"
    elif ((x.miso_significant == "yes") and
          (x.rmats_significant == "no") and
          (x.whippet_significant == "yes")):
        return "mw"
    elif ((x.miso_significant == "no") and
          (x.rmats_significant == "yes") and
          (x.whippet_significant == "yes")):
        return "rw"
    elif ((x.miso_significant == "yes") and
          (x.rmats_significant == "no") and
          (x.whippet_significant == "no")):
        return "m"
    elif ((x.miso_significant == "no") and
          (x.rmats_significant == "yes") and
          (x.whippet_significant == "no")):
        return "r"
    elif ((x.miso_significant == "no") and
          (x.rmats_significant == "no") and
          (x.whippet_significant == "yes")):
        return "w"
    elif ((x.miso_significant == "no") and
          (x.rmats_significant == "no") and
          (x.whippet_significant == "no")):
        return "not_significant"

    return None
