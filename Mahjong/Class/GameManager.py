from msilib.schema import Class
from tkinter.tix import INTEGER
from Mahjong.DemoFile import InputPlayersName
from .ClassPlayer import Player
from .Setting import AllMahjongs
import random

class GameManager():
    def __init__(Self) -> None:
        ''' 初始化遊戲管理物件 '''
        pass
# -------- 設定玩家順序、初始化所有玩家 -------- #
    def SetSeqPlayerlist(Self,PlayerList,DiceNum):
        ''' 依骰子數確定玩家的正確順序，並初始化他們，可以使用Self.PlayerList調用 '''
        # 排序
        if DiceNum != 1:
            PlayerList = PlayerList[DiceNum-1:]
            tempPlayerlist = PlayerList[0:DiceNum-1]
            for tempPlayer in tempPlayerlist:
                PlayerList.append(tempPlayer)
        # 初始化
        for PlayerName in PlayerList:
            Self.PlayerList.append(Player(PlayerName))
# --------
    def SetDiceNum(Self, DiceNum):
        Self.DiceNum = DiceNum

    def InitPlayersCards(Self):
        ''' 初始化卡牌 '''
        Self.AllCards = AllMahjongs
        for Player in Self.PlayerList:
            Player.Cards, Self.AllCards = Self.GetRandomCardsAndDelete(16)

    def SetPlayerList(Self, Playerlist):
        ''' 設定玩家清單 '''
        Self.PlayerList = Playerlist

    def SetBanker(Self, Banker):
        ''' 目前莊家 '''
        Self.Banker = Banker
    
    def ReplaceFlowerCard():
        ''' 補牌動作 '''
        pass

    def SetWinds():
        ''' 紀錄幾局 '''
        pass
# -------- 與牌有關的 -------- #
    def GetRandomCardsAndDelete(Self, num:int = 1):
        ''' 取得隨機的剩餘牌(數量: num) 並 從剩餘牌庫(牌庫: AllCards)中刪除，回傳隨機的牌、剩餘的牌 '''
        Cards = random.sample(Self.AllCards, num)
        for x in Cards:
            Self.AllCards.remove(x)
        return Cards, Self.AllCards