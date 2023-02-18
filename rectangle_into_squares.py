def sq_in_rect(lng, wdth):
    x = []
    if lng == wdth:
        return None
    if wdth > lng:
        width = lng
        lng = wdth
        wdth = width

    x.append(wdth)
    while lng > 0 and wdth > 0:
        if lng - wdth != 0:
            if wdth > lng:
                width = lng
                lng = wdth
                wdth = width
            x.append(lng - wdth)
            lng = lng - wdth
        else:
            break

    return x


print(sq_in_rect(5, 3))
