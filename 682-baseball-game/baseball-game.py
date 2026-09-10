class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        score = 0

        for i in range(len(operations)):
            if (operations[i] == '+'):
                sumOfPrevScore = record[-1] + record[-2]
                record.append(sumOfPrevScore)
            elif (operations[i] == 'D'):
                doublePrevScore = record[-1] * 2
                record.append(doublePrevScore)
            elif (operations[i] == 'C'):
                record.pop()
            else:
                record.append(int(operations[i]))
        
        for i in record:
            score += int(i)
        
        return score
