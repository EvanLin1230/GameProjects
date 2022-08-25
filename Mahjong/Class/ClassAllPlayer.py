from .ClassPlayer import ClassPlayer

AllMahjongs = ["東","東","東","東","西","西","西","西","南","南","南","南","北","北","北","北","中","中","中","中","發","發","發","發","白","白","白","白","一筒","一筒","一筒","一筒","二筒","二筒","二筒","二筒","三筒","三筒","三筒","三筒","四筒","四筒","四筒","四筒","五筒","五筒","五筒","五筒","六筒","六筒","六筒","六筒","七筒","七筒","七筒","七筒","八筒","八筒","八筒","八筒","九筒","九筒","九筒","九筒","一萬","一萬","一萬","一萬","二萬","二萬","二萬","二萬","三萬","三萬","三萬","三萬","四萬","四萬","四萬","四萬","五萬","五萬","五萬","五萬","六萬","六萬","六萬","六萬","七萬","七萬","七萬","七萬","八萬","八萬","八萬","八萬","九萬","九萬","九萬","九萬","一條","一條","一條","一條","二條","二條","二條","二條","三條","三條","三條","三條","四條","四條","四條","四條","五條","五條","五條","五條","六條","六條","六條","六條","七條","七條","七條","七條","八條","八條","八條","八條","九條","九條","九條","九條","春","夏","秋","冬","梅","蘭","竹","菊"]

class ClassAllPlayer:

    def __init__(Self, Playerlist, BankerNum) -> None:

        Self.PlayerList = Playerlist
        Self.players[BankerNum] = ClassPlayer(True)
        Self.Player1 = ClassPlayer(False)
        Self.Player2 = ClassPlayer(False)
        Self.Player3 = ClassPlayer(False)

    def InitCards(Self):
        tempCards = AllMahjongs
        tempCards = Self.Banker.GetRandomCardsAndDelete()

    def SetUpPlayer(Self):
        
        pass

    def ReplaceFlowerCard():
        pass
