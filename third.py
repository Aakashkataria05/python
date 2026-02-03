# student1 = {
#     "name" : "aakash",
#     "class" : "12th standard",
#     "grade" : "A+",
#     "contact" : "93508xxxxx",
#     "moto" : "gaand fadna"
# }

# print(student1["moto"])
# print(student1["grade"])

# collection = { 1, 5, 5, 5, 6, "jai", "baba ki", 9}
# print(collection)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []