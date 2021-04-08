import scipy.constants as spc


def lam(U):
    return (spc.h * spc.c) / (spc.e * U)
