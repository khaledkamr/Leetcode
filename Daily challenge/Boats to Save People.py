class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        start, end = 0, len(people) - 1
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            count += 1
            end -= 1
        return count