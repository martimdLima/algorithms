class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ranks.sort()
        # suits.sort()

        poker = {}
        i = 0

        highest = "High Card"
        if len(set(suits)) == 1:
            return "Flush"

        while i <= len(ranks) - 1:
            if ranks[i] not in poker:
                poker[ranks[i]] = 1
            else:
                poker[ranks[i]] += 1

            if poker[ranks[i]] == 3:
                highest = "Three of a Kind"
                break
            elif poker[ranks[i]] == 2:
                highest = "Pair"
            print(ranks[i], poker[ranks[i]])
            i += 1

        return highest

    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # Check for Flush
        if len(set(suits)) == 1:
            return "Flush"

        # Count the frequency of each rank
        rank_count = Counter(ranks)

        # Determine the best hand
        if max(rank_count.values()) >= 3:
            return "Three of a Kind"
        elif max(rank_count.values()) == 2:
            return "Pair"
        else:
            return "High Card"
