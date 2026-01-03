COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> dict:
    if amount <= 0:
        return {}

    result = {}
    remaining = amount

    for coin in COINS:
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= coin * count

        if remaining == 0:
            break

    return result


def find_min_coins(amount: int) -> dict:
    if amount <= 0:
        return {}

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [None] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    current = amount
    while current > 0:
        coin = coin_used[current]
        if coin is None:
            return {}
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


def main():
    amount = 113
    print(find_coins_greedy(amount))
    print(find_min_coins(amount))


if __name__ == "__main__":
    main()
