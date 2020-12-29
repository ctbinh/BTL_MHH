import math


# formula 3
def cal_MCBlowAir(nHeatCO2, UBlow, PBlow, AFlr):
    return nHeatCO2 * UBlow * PBlow / AFlr
# formula 4
def cal_MCExtAir(UExtCO2, phiExtCO2, AFlr):
    return UExtCO2 * phiExtCO2 / AFlr
# formula 5
def cal_MCPadAir_1(fPad, CO2Out, CO2Air):
    return fPad * (CO2Out - CO2Air)
def cal_MCPadAir_2(UPad, phiPad, AFlr, CO2Out, CO2Air):
    fPad = UPad * phiPad / AFlr
    return fPad * (CO2Out - CO2Air)
# formula 6
def cal_MCAirTop(fThScr, CO2Air, CO2Top):
    return fThScr * (CO2Air - CO2Top)
# formula 7
def cal_fThScr(UThScr, kThScr, tAir, tTop, g, PAir, PTop):
    a = UThScr * kThScr * pow(abs(tAir - tTop), 2/3)
    PMean_Air = (PAir + PTop) / 2
    b = (1 - UThScr) * pow(g * (1 - UThScr) * abs(PAir - PTop) / (2 * PMean_Air), 1/2)
    return a + b
# formula 9
def cal_MCAirOut(fVentSide, fVentForce, CO2Air, CO2Out):
    return (fVentSide + fVentForce) * (CO2Air - CO2Out)
# formula 10
def cal_fVentRoofSide(cD, AFlr, URoof, USide, ARoof, ASide, g, h, tAir, tOut, tMean_Air, cW, vWind):
    a = cD / AFlr
    b = pow(URoof * USide * ARoof * ASide, 2) / (pow(URoof * ARoof, 2) + pow(USide * ASide, 2))
    c = 2 * g * h * (tAir - tOut) / tMean_Air
    _d = (URoof * ARoof + USide * ASide) / 2
    d = pow(_d, 2) * cW * pow(vWind, 2)
    return a * pow(b * c + d, 1 / 2)
# formula 11
def cal_nInsScr(sInsScr):
    return sInsScr * (2 - sInsScr)

#19
def hCBuf(CBuf, CBufMax):
    return (int)(CBufMax >= CBuf)
#22
def get_abc(Res,CO2Air,CO2_05,PMax):
    return Res,-(CO2Air+CO2_05+Res*PMax),CO2Air*PMax
def cal_P(get_abc):
    a,b,c = get_abc
    return (-b-math.sqrt(b*b-4*a*c))/(2*a)
#23
def k(T, T0, kT0, Ha, R):
    return kT0 * math.exp(-Ha / R * (1 / T - 1 / T0))
#24
def f(T, T0, Hd, R, S):
    return (1 + math.exp(-Hd / R * (1 / T0 - S / Hd)))/(1 + math.exp(-Hd / R * (1 / T - S / Hd)))
#25
def PMax_T(k, f):
    return k * f
#27
def L(L0, K, LAI, m):
    return L0 * (1 - (K * math.exp(-K * LAI)) / (1 - m))
#28
def k_expand(LAI, T, T0, kT0, Ha, R):
    return LAI * k(T, T0, kT0, Ha, R)


# fomular 1
def dxCO2Air():
    
    return 0
# formula 2
def dxCO2Top(capCO2Top, MCAirTop, MCAirOut):
    return (MCAirTop - MCAirOut) / capCO2Top


