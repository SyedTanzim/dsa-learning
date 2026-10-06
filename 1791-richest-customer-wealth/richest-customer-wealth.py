class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxWealth = 0

        for account in accounts:
            wealth = 0
            for money in account:
                wealth += money
            if wealth > maxWealth:
                maxWealth = wealth
                
        return maxWealth

