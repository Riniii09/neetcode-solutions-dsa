class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # senior_citizens = 0
        # for person in details:
        #     age = str(person[11]) + str(person[12])
        #     if int(age) > 60:
        #         senior_citizens += 1
        # return senior_citizens
        return sum(1 for info in details if int(info[11:13]) > 60)