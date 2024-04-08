class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student=deque()
        sandwich=deque()
        for i in range(len(students)):
            student.append((students[i],i))
            sandwich.append(sandwiches[i])

        visited=set()
        
        while sandwich:
            if (student[0][1],len(sandwich)) in visited:
                return len(student)
            if sandwich[0]==student[0][0]:
                sandwich.popleft()
                student.popleft()
            else:
                visited.add((student[0][1],len(sandwich)))
                st,idx=student.popleft()
                student.append((st,idx))
        return 0
