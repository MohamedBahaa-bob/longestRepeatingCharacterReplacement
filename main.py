# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def characterReplacement(self, s, k) -> int:
        arrays = []
        length = len(s)
        for i in range(0, length):
            array = []
            array.extend(s[i])
            array.append(i)
            arrays.append(array)
        arrays.sort()
        i = 0
        maxCount = 0
        initialK = k
        end = 0
        print(arrays)
        allDiff = True
        start = 0
        while i < length:
            k = initialK
            lastStart = start
            start = i
            c = arrays[start][0]
            countc = 0
            while i < length and c == arrays[i][0]:
                if countc > 0:
                    allDiff = False
                countc += 1
                end = i
                i += 1
            # print(countc)
            # print("start " + str(start))
            # print("end " + str(end))
            while start != end:
                diff = arrays[end][1] - arrays[start][1] - 1
                # print(diff)
                # print(countc)
                if diff <= k + countc - 2:
                    count = min(k, length - end - 1 + (start - lastStart)) + countc
                    if count > maxCount:
                        maxCount = count
                    break
                else:
                    # print("hasal")
                    if arrays[end][1] - arrays[end - 1][1] > arrays[start + 1][1] - arrays[start][1]:
                        end -= 1
                        countc -= 1
                    else:
                        start += 1
                        countc -= 1
            print(countc)
        if allDiff:
            return min(length, k + 1)
        return maxCount


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.characterReplacement("ABCDFAEGDGAHGSAKBWBUWBEUBDAABDAWBBCEBAB", 10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
