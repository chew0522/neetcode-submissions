class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x, i in Counter(nums).most_common(k)]