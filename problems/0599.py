"599. Minimum Index Sum of Two Lists"

# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        index = []
        index_sum = 0

        for i, v in enumerate(list1):
            if (v in list2):
                if (index == [] or index_sum > i + list2.index(v)):
                    index = [i]
                    index_sum = i + list2.index(v)
                elif (index_sum == i + list2.index(v)):
                    index.append(i)

        return [list1[i] for i in index]
