from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students) # number of students who can't eat total 
        students_count = Counter(students)

        for s in sandwiches:
            if students_count[s] > 0:
                res -= 1
                students_count[s] -= 1
            else:
                break
        
        return res

         


# 00111 00011

        # students_count = {}
        # sandwiches_count = {}

        # for student in students:
        #     if students[student] == 1:
        #         students_count.get(student, 0) + 1
        #     elif students[student] == 0:
        #         students_count.get(student, 0) + 1
        
        # for sandwich in sandwiches:
        #     if sandwiches[sandwich] == 1:
        #         sandwiches_count.get(sandwich, 0) + 1
        #     elif sandwiches[sandwich] == 0:
        #         sandwiches_count.get(sandwich, 0) + 1

        # sandwiches_remaining = sandwiches_count.get(0, 0) + sandwiches_count.get(1, 0)
        # students_remaining = students_count.get(0, 0) + students_count.get(1, 0)

        # return sandwiches_remaining + students_remaining