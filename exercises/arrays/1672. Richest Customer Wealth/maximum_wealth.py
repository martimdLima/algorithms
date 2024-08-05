class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthiest_customer = 0

        for account in accounts:
            wealthiest_customer = max(wealthiest_customer, sum(account))

        return wealthiest_customer
