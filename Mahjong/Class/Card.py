# coding: utf-8
from ast import Return
from select import select
from typing import Any
from Setting import SortMahjongsSetting

numList = SortMahjongsSetting[0]

# 以下為麻將分類及取得麻將分類的函式
class EnumCardType():
    Wong = "萬"
    Tong = "筒"
    Tiao = "條"
    Wind = "東南西北中發白"
    Flower = "春夏秋冬梅蘭竹菊"

def GetCardType(Card) -> str:
    ''' 取得卡牌種類，回傳字串 '''
    for x in Card:
        if EnumCardType.Wong.__contains__(x): return "萬"
        if EnumCardType.Tong.__contains__(x): return "筒"
        if EnumCardType.Tiao.__contains__(x): return "條"
        if EnumCardType.Wind.__contains__(x): return "字"
        if EnumCardType.Flower.__contains__(x): return "花"

# --------- 排序牌 ---------- #
def SortValue(value):
        ''' 排序用的key, 數字依照index, 萬筒條依照index*10, 國字依照index*100, 花牌依照index*1000. 詳細請看Setting.py '''
        num = 0
        for a in SortMahjongsSetting[0]:
            if a in value:
                num += SortMahjongsSetting[0].index(a)+1
        for b in SortMahjongsSetting[1]:
            if b in value:
                num += (SortMahjongsSetting[1].index(b)+1)*10
        for c in SortMahjongsSetting[2]:
            if c in value:
                num += (SortMahjongsSetting[2].index(c)+1)*100
        for d in SortMahjongsSetting[3]:
            if d in value:
                num += (SortMahjongsSetting[3].index(d)+1)*1000
        return num

def SortCards(Cards):
    ''' 排序牌 '''
    return sorted(Cards,key=SortValue)

# 打出一張牌 二萬 要怎麼吃？ 第一條件：擁有萬才有機會吃；第二條件：擁有一三萬、三四萬才可以吃
# 牌裡面滿足 同時擁有一三萬 或 同時擁有三四萬 才能吃
# CardTarget 不可能有花牌存在，所以先不假設有花牌，如果要平民化一點，再加進去導向相公的狀態。
def GetFirstMotion(CardArr,CardTarget):
    ''' 吃、碰、槓、胡 '''
    MotionType = ["吃","碰","槓","胡"]
    Result = dict()
    for i in range(len(MotionType)):
        Result[MotionType[i]] = GetMotionByType(MotionType[i],CardArr,CardTarget)
    return Result

def GetMotionByType(MotionType, CardArr, CardTarget):
    match MotionType:
        case "吃":
            return GetEatCard(CardArr, CardTarget)
        case "碰":
            return GetTwoCard(CardArr, CardTarget)
        case "槓":
            return GetThreeCard(CardArr, CardTarget)
        case "胡":
            return []
# ------ 吃牌處理 ------- #
def GetEatCard(CardArr,CardTarget):
    ''' 依照自己的牌，取得吃牌的方式，結果為二維陣列，[[第一種方式], [第二種方式]...] '''
    CardTargetTypeInCardArr = [Card for Card in CardArr if GetCardType(CardTarget) == GetCardType(Card)]
    CardTargetType = GetCardType(CardTarget)
    Result = []
    if CardTargetType != "字":
        Arr = GetTwoOfCardNear(CardTarget)
        for x in Arr:
            # 如果所有x裡的牌，都出現在我的牌裡，那就會回傳True
            if all(y in CardTargetTypeInCardArr for y in x):
                x.append(CardTarget)
                x = SortCards(x)
                Result.append(x)
    return Result

def GetTwoOfCardNear(CardTarget):
    ''' 「吃牌專用」：取得牌附近的兩張牌 '''
    num = numList.index(CardTarget[0])
    resultArr = []
    for x in range(0,3):
        tempArr = []
        for y in range(2,-1,-1):
            # 只要其中一個會小於0或大於8(=不在數字陣列中)，即歸零tempArr並跳出迴圈
            if num+x-y < 0 or num+x-y > len(numList)-1:
                tempArr.clear()
                break
            if num != num+x-y:
                tempArr.append(numList[num+x-y] + CardTarget[1])
        resultArr.append(tempArr)
    return resultArr

# ------- 碰牌處理 ------- #
def GetTwoCard(CardArr, CardTarget) -> list:
    Arr = [x for x in CardArr if x == CardTarget]
    if len(Arr) == 2:
        Arr.append(CardTarget)
    else:
        Arr = []
    return Arr

# ------- 槓牌處理 ------- #
def GetThreeCard(CardArr, CardTarget) -> list:
    Arr = [x for x in CardArr if x == CardTarget]
    if len(Arr) == 3:
        Arr.append(CardTarget)
    else:
        Arr = []
    return Arr

# ------- 胡牌、自摸處理 ------- #
# 把剩餘的牌配對完(每個都三個三個配對，吃的全部配完後，再配碰的，順序是從第一個開始)，再看要怎麼胡。
# 需要再寫一個函式處理配對回來的處理 => 這部份做好就算是寫好一大部分的AI了
def GetWinCard(CardArr, CardTarget):
    return
    
def RecursiveTest(CardArr: list, CardTarget):
    CardArr.append(CardTarget)
    MaxIndex = len(CardArr)-1
    MinIndex = 0
    while(len(CardArr)>2 or MinIndex+1!=MaxIndex):
        print(MinIndex, MaxIndex)
        DelCardList = GetEatCard(CardArr[MinIndex+1:], CardArr[MinIndex])
        if len(DelCardList)>0:
            print("吃：{}，CardArr：{}".format(DelCardList,CardArr))
            for x in DelCardList[0]:
                CardArr.remove(x)
        else:
            DelCardList = GetTwoCard(CardArr[MinIndex+1:], CardArr[MinIndex])
            if len(DelCardList) > 0:
                print("碰：{}，CardArr：{}".format(DelCardList,CardArr))
                for x in DelCardList:
                    CardArr.remove(x)
            else:
                MinIndex+=1
    if CardArr[0] == CardArr[1]:
        return CardArr,True
    else:
        return CardArr,False


#dictMotion = GetFirstMotion(["一萬","五萬","六萬","九萬","二筒","五筒","六筒","三條","四條","七條","七條","東","東","西","中","中"],"七萬")

#print(dictMotion["吃"])

#print(GetEatCard(["一萬","五萬","七萬","八萬","九萬","二筒","五筒","六筒","三條","四條","七條","七條","東","東","西","中","中"],"六萬"))

print(RecursiveTest(["一萬","五萬","五萬","六萬","六萬"],"六萬"))