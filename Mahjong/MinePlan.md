# MinePlan

# First

I need to store all the kinds of the mohjong in my global variable
東南西北中發白 *4
梅蘭竹菊春夏秋冬 *1
一筒～九筒 *4
一萬～九萬 *4
一條～九條 *4

已完成部分：
- 隨機產生四家的牌
- 排序
- 將花牌替換掉

# Second

我需要試著美化我產生的牌並顯示於Terminal，並且將他們整理成一個class，方便後續取得每家的花牌數量及種類

## ClassPlayer
    這裡面應該要是最簡單的，所以應該是讓ClassAllPlayer處理其他事情

| 名稱 | 作用 | 種類 | 參數 |
|---|---|---|---|
| `__init__` | 初始化 | 函式 | isBanker |
|`isBanker`| 是否為莊家 | 變數 |  |
|||||
|||||
|||||


## ClassAllPlayer
    把所有玩家外面再包一層，以同步或控制所有人共用的牌庫、規則制定

# Third
    制度

    首先我們知道麻將一開始需要骰骰子，決定誰是莊家，骰出骰子後，必須要記錄目前是什麼風什麼局，從東風東局到北風北局
    我決定，產生牌組歸`所有玩家`呼叫`玩家`，玩家打牌以及AI電腦打牌歸`玩家`，流程控制歸`流程`
