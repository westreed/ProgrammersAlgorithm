# 2023 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/150368

def solution(users, emoticons):
    import itertools
    
    emojiLen = len(emoticons)
    saleRates = [10,20,30,40]
    salePrices = {idx:[emoticons[idx]*(100-sale)//100 for sale in saleRates] for idx in range(emojiLen)}
    Answer = []
    
    for sales in itertools.product(*[[0,1,2,3] for _ in range(emojiLen)]):
        currentPrices = [(saleRates[sales[idx]], salePrices[idx][sales[idx]]) for idx in range(emojiLen)]
        EmojiPlus = 0
        EmojiSell = 0
        for rate, plusPrice in users:
            usePrice = 0
            for saleRate, salePrice in currentPrices:
                if saleRate >= rate:
                    usePrice += salePrice
            
            if usePrice >= plusPrice:
                EmojiPlus += 1
            else:
                EmojiSell += usePrice
        
        Answer.append([EmojiPlus, EmojiSell])
    return max(Answer)