class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        best_sum = curr_sum = sum(cardPoints[-k:])

        for i in range(k):
            curr_sum -= cardPoints[-k + i]
            curr_sum += cardPoints[i]

            best_sum = max(curr_sum, best_sum)

        return best_sum