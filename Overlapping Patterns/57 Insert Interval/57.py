class Solution:
    def insert(self, intervals, newInterval):
        print(intervals)

        intervals.append(newInterval)

        print(intervals)

        intervals.sort(key = lambda x: x[0])

        print(intervals)

        merged_intervals = []

        for interval in intervals:
            if merged_intervals and interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(interval[1], merged_intervals[-1][1])
            else:
                merged_intervals.append(interval)

        return merged_intervals


obj = Solution()
ans = obj.insert([[1,3],[6,9]],[2,5])
print(ans)

        