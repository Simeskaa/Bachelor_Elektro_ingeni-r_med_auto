import numpy as np


def angle_calc(tdoas: list, spd_sound: float, spacing: float):
    diff = max(tdoas[2], tdoas[1]) - min(tdoas[2], tdoas[1])
    dist = diff * spd_sound
    angle = 90 - np.arccos(dist/spacing) * 180/np.pi
    return angle

def angle_calc2(tdoas: list, spd_sound: float, spacing: float):
    tdoas_temp = tdoas
    ref = np.argmin(tdoas_temp)
    if ref == 0:
        offsett = 90
        print("ref: front")
    elif ref == 1:
        offsett = 180
        print("ref: right")
    elif ref == 2:
        offsett = 270
        print("ref: left")
    else:
        print("ref: multiple or error")

    #print(tdoas_temp)
    tdoas_temp.remove(tdoas_temp[ref])
    #print(tdoas_temp)
    diff = (max(tdoas_temp[1], tdoas_temp[0]) - min(tdoas_temp[1], tdoas_temp[0]))*10**-3
    #print("diff:", diff)
    dist = diff * spd_sound
    #print("dist:", dist)
    angle = offsett - np.arccos(dist/spacing) * 180/np.pi
    return angle
