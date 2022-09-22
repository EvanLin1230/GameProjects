# 下面那串可以讓我們成功輸出中文字
# coding: utf-8
from gc import garbage
import random
from Class.GameManager import GameManager
# 全域變數
AllMahjongs = ["東","東","東","東","西","西","西","西","南","南","南","南","北","北","北","北","中","中","中","中","發","發","發","發","白","白","白","白","一筒","一筒","一筒","一筒","二筒","二筒","二筒","二筒","三筒","三筒","三筒","三筒","四筒","四筒","四筒","四筒","五筒","五筒","五筒","五筒","六筒","六筒","六筒","六筒","七筒","七筒","七筒","七筒","八筒","八筒","八筒","八筒","九筒","九筒","九筒","九筒","一萬","一萬","一萬","一萬","二萬","二萬","二萬","二萬","三萬","三萬","三萬","三萬","四萬","四萬","四萬","四萬","五萬","五萬","五萬","五萬","六萬","六萬","六萬","六萬","七萬","七萬","七萬","七萬","八萬","八萬","八萬","八萬","九萬","九萬","九萬","九萬","一條","一條","一條","一條","二條","二條","二條","二條","三條","三條","三條","三條","四條","四條","四條","四條","五條","五條","五條","五條","六條","六條","六條","六條","七條","七條","七條","七條","八條","八條","八條","八條","九條","九條","九條","九條","春","夏","秋","冬","梅","蘭","竹","菊"]
FlowerMahjongs = ["春","夏","秋","冬","梅","蘭","竹","菊"]
SortedMahjongs1 = ["一","二","三","四","五","六","七","八","九"]
SortedMahjongs2 = ["","萬","筒","條"]
SortedMahjongs3 = ["","東","南","西","北","中","發","白"]


def initGame():
    random.shuffle(AllMahjongs)
    tempMahjongs, result1 = GetRandomCardsAndDelete(AllMahjongs,16)
    tempMahjongs, result2 = GetRandomCardsAndDelete(tempMahjongs,16)
    tempMahjongs, result3 = GetRandomCardsAndDelete(tempMahjongs,16)
    tempMahjongs, result4 = GetRandomCardsAndDelete(tempMahjongs,16)
    sYourCard = listToString(SortCards(result1))
    sPlayer1Card = listToString(SortCards(result2))
    sPlayer2Card = listToString(SortCards(result3))
    sPlayer3Card = listToString(SortCards(result4))
    lastCards = listToString(SortCards(tempMahjongs))
    print("===========================================")
    print("你的牌: "+ sYourCard)
    print("player1的牌: " + sPlayer1Card)
    print("player2的牌: " + sPlayer2Card)
    print("player3的牌: " + sPlayer3Card)
    print("剩餘所有牌: " + lastCards)
    print("===========================================")
    print("準備替換花牌...")
    print("===========================================")
    tempMahjongs, result1 = ReplaceFlowerCards(result1,tempMahjongs)
    tempMahjongs, result2 = ReplaceFlowerCards(result2,tempMahjongs)
    tempMahjongs, result3 = ReplaceFlowerCards(result3,tempMahjongs)
    tempMahjongs, result4 = ReplaceFlowerCards(result4,tempMahjongs)
    sYourCard = listToString(SortCards(result1))
    sPlayer1Card = listToString(SortCards(result2))
    sPlayer2Card = listToString(SortCards(result3))
    sPlayer3Card = listToString(SortCards(result4))
    lastCards = listToString(SortCards(tempMahjongs))
    print("你的牌: "+ sYourCard)
    print("player1的牌: "+ sPlayer1Card)
    print("player2的牌: "+ sPlayer2Card)
    print("player3的牌: "+ sPlayer3Card)
    print("===========================================")
    print("剩餘所有牌: " + lastCards)

def listToString(list):
    ''' 陣列轉字串 |a|b|c|...'''
    a = ""
    for item in list:
        a += "|" + item
    return a + "|"

def GetRandomCardsAndDelete(LastMahjongs, num):
    ''' 取得隨機的剩餘牌(數量: num) 並 從剩餘牌庫(牌庫: tempMahjongs)中刪除 '''
    templist = random.sample(LastMahjongs,num)
    for x in templist:
        LastMahjongs.remove(x)
    return LastMahjongs, templist

def SortValue(str):
    ''' 排序用的key, 數字依照index, 萬筒條依照index*10, 國字依照index*100 '''
    ''' 為了避免第一個index是0會被吃掉, 可以將排序陣列第一個設置為空值 '''
    num = 0
    for a in SortedMahjongs1:
        if a in str:
            num += SortedMahjongs1.index(a)
    for b in SortedMahjongs2:
        if b in str:
            num += SortedMahjongs2.index(b)*10
    for c in SortedMahjongs3:
        if c in str:
            num += SortedMahjongs3.index(c)*100
    return num

def SortCards(MahjongsList):
    ''' 回傳排序好的牌 '''
    MahjongsList = sorted(MahjongsList,key=SortValue)
    return MahjongsList

def ReplaceFlowerCards(MahjongsList, LastMahjongs):
    ''' 將花牌替換掉 '''
    num = 0
    for x in FlowerMahjongs:
        if x in MahjongsList:
            num+=1
            MahjongsList.remove(x)
    if num != 0:
        tempMahjongs, result = GetRandomCardsAndDelete(LastMahjongs, num)
        for x in result:
            MahjongsList.append(x)
        return tempMahjongs, MahjongsList
    else:
        return LastMahjongs, MahjongsList

def initGame2():

    # 遊戲開始
    GM = GameManager()

    # 初始化玩家清單
    print("請依序輸入四位玩家姓名：")
    InputListPlayer = InputPlayersName()

    # 決定由誰當今天的第一個玩家，也就是東風東局
    DiceNum = ThrowDice()
    print("骰子數為:{}".format(DiceNum))
    DiceNumMod4 = DiceNum%4

    # 放進去AllPlayer進行重新排列
    GM.SetSeqPlayerlist(InputListPlayer,DiceNumMod4) # ListPlayer 將會作為之後16局遊戲的順序
    print("所有玩家順序為：{}".format(GM.PlayerList))
    print("第一個玩家為：{}".format(GM.PlayerList[0])) # ListPlayer[0] 為第一場莊家

    GM.InitPlayers()

    # 以第一位玩家開始擲骰子並決定場風
    DiceResultDesideEastWind = ThrowDice()
    print("莊家骰到的點數為:{}" .format(DiceResultDesideEastWind))

    # 遊戲開始
    AllPlayer = GameManager()
    #print(AllPlayer.Banker.cards)

def ThrowDice():
    ''' 取得 0-3 的隨機整數 '''
    num = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    return num

def InputPlayersName():
    ''' 回傳List '''
    num = 4
    playerList = []
    for i in range(num):
        playerList.append(input("玩家{}:".format(i+1)))
    return playerList

initGame2()

#initGame2()