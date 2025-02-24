class Solution:
    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])

        print(intervals)

        merged_intervals = []

        # for interval in intervals:
        #     if merged_intervals:
        #         temp = merged_intervals.pop()
        #         if interval[0] <= temp[1]:
        #             merged_intervals.append([temp[0],interval[1]])
        #         else:
        #             merged_intervals.append(temp)
        #             merged_intervals.append(interval)
        #     else:
        #         merged_intervals.append(interval)

        for interval in intervals:
            if merged_intervals and interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(interval[1], merged_intervals[-1][1])
            else:
                merged_intervals.append(interval)

        return merged_intervals


obj = Solution()
ans = obj.merge([[1,3],[4,6],[8,10],[9,18]])
# ans = obj.merge([[1,4],[4,5]])

print(ans)
        