import random
import this

class ClassPlayer:

    def __init__(self, isBanker) -> None:
        ''' 參數中第一個 self 代表該物件被命名產生 '''
        ''' 裡面寫的 self.xxx 代表物件 '''
        self.isBanker = isBanker

    def SortValue(str):
        ''' 排序用的key, 數字依照index, 萬筒條依照index*10, 國字依照index*100 '''
        ''' 為了避免第一個index是0會被吃掉, 可以將排序陣列第一個設置為空值 '''
        SortedMahjongs1 = ["一","二","三","四","五","六","七","八","九"]
        SortedMahjongs2 = ["","萬","筒","條"]
        SortedMahjongs3 = ["","東","南","西","北","中","發","白"]
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
        MahjongsList = sorted(MahjongsList,key=this.SortValue)
        return MahjongsList

    def GetRandomCardsAndDelete(self,LastMahjongs,num):
        ''' 取得隨機的剩餘牌(數量: num) 並 從剩餘牌庫(牌庫: tempMahjongs)中刪除，回傳剩餘的牌 '''
        self.cards = random.sample(LastMahjongs,num)
        # 刪除已拿取的牌(可以考慮拉出來寫)
        for x in self.cards:
            LastMahjongs.remove(x)
        return LastMahjongs