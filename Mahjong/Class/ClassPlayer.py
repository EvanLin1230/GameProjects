from email.headerregistry import ContentDispositionHeader
import random
import this
from Setting import SortMahjongsSetting
from Card import SortCards, GetCardType, EnumCardType
class Player:

    def __init__(self, Name):
        ''' 參數中第一個 self 代表該物件被命名產生 '''
        ''' 裡面寫的 self.xxx 代表物件 '''
        self.Name = Name
        self.DropedCards = []
        self.Cards = []

    def SetPlayer(self, isPlayer):
        ''' 設定是否為player, True = 玩家, False = 電腦 '''
        self.isPlayer = isPlayer

    def SetBanker(self, isBanker):
        ''' 設定是否為莊家 '''
        self.isBanker = isBanker

    def SetWind(self, wind):
        ''' 設定自己當局的場風 '''
        self.wind = wind

# --------- 丟牌 ---------- #
    def DropCards(self):
        if self.isPlayer == False:
            # AI will drop the card.
            self.DropedCards.append(self.AIDropCard())
        else:
            # wait player to drop the card.
            print("Wait")
            self.DropedCards.append()

    def AIDropCard(self):
        ''' 寫AI去分析該丟什麼牌 '''
        #TODO 寫出丟牌演算法 

# --------- 排序牌 ---------- #
    def SortCards(self) -> None:
        ''' 排序牌，做法可以參照Card.py'''
        self.Cards = SortCards(self.Cards)

# --------- 動作 ---------- #
    def MotionDetect(self, Card):
        ''' 動作偵測 '''
        CardArr = []
        CardType = GetCardType(Card)
        for card in self.Cards:
            if GetCardType(card) == CardType:
                CardArr.append(card)
        Result = self.GetCardResult(CardArr, CardType)

    def GetCardResult(CardArr, CardType):
        ''' 回傳dict ["吃":["...","..."], "碰":["..."], "槓":["..."], "胡":[True or False]] '''
        # 吃 只有萬筒條 | 碰 萬筒條字 | 槓 萬筒條字 | 胡 需要全部判斷
        

# --------- 擲骰子 ---------- #
    def ThrowDice(self) -> None:
        ''' 取得 3~18 的隨機整數 '''
        num = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        self.Dice = num