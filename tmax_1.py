def solution(stock_price):
    answer = []
    long_term = 1
    short_term = 1
    long_term_max = 1
    short_term_max = 1

    for idx, price in enumerate(stock_price):
        if idx == 0:
            continue
        # print(price - stock_price[idx-1], price, long_term, short_term)
        if price - stock_price[idx-1] > 0:
            long_term += 1
            short_term_max = max(short_term_max, short_term)
            short_term = 1
        elif price - stock_price[idx-1] < 0:
            short_term += 1
            long_term_max = max(long_term_max, long_term)
            long_term = 1
        else:
            long_term_max = max(long_term_max, long_term)
            long_term = 1
            short_term_max = max(short_term_max, short_term)
            short_term = 1
        
    answer = [max(long_term_max, long_term), max(short_term_max, short_term)]
    return answer

stock_price = [[2, 1, 2, 3, 4, 4, 5, 4, 3], [1, 2, 4, 5, 6, 7], [5, 5, 5, 5, 5]]

for stock  in stock_price:
    print(solution(stock))