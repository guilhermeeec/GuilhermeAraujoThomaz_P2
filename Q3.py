def isCollisionDetected (dict_retang1, dict_retang2):
    BLx1 = dict_retang1['BottomLeft'](0)
    BLy1 = dict_retang1['BottomLeft'](1)
    TRx1 = dict_retang1['TopRight'](0)
    TRy1 = dict_retang1['TopRight'](1)
    BLx2 = dict_retang2['BottomLeft'](0)
    BLy2 = dict_retang2['BottomLeft'](1)
    TRx2 = dict_retang2['TopRight'](0)
    TRy2 = dict_retang2['TopRight'](1)
    if ((TRx2 >= BLx1) and (TRy2 >= BLy1)) or ((TRx1 >= BLx2) and (TRy1 >= BLy2)):
        return True
    elif ((TRx1 >= BLx2) and (BLy1 <= TRy2)) or ((TRx2 >= BLx1) and (BLy2 <= TRy1)):
        return True
    elif ((TRx1 <= BLx2) and (BLy1 <= TRy2)) or ((TRx2 <= BLx1) and (BLy1 <= TRy1)):
        return True
    elif ((BLx1 <= TRx2) and (TRy1 >= BLy2)) or ((BLx2 <= TRx1) and (TRy2 >= BLy1)):
        return True
    else:
        return False

    def main ():
    BLx1 = int(input('BLx1: '))
    BLy1 = int(input('BLy1: '))
    TRx1 = int(input('TRx1: '))
    TRy1 = int(input('TRy1: '))
    tupla_BL1 = (BLx1, BLy1)
    tupla_TR1 = (TRx1, TRy1)
    dict_retang1 = {'BottomLeft':tupla_BL1, 'TopRight': tupla_TR1}
    BLx2 = int(input('BLx2: '))
    BLy2 = int(input('BLy2: '))
    TRx2 = int(input('TRx2: '))
    TRy2 = int(input('TRy2: '))
    tupla_BL2 = (BLx2, BLy2)
    tupla_TR2 = (TRx2, TRy2)
    dict_retang2 = {'BottomLeft':tupla_BL2, 'TopRight': tupla_TR2}
    colisao = isCollisionDetected(dict_retang1, dict_retang2)
    if colisao:
        print('Colisão detectada')
    else:
        print('Colisão não detectada')

main()

