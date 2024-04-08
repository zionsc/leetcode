#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        deque<int> student(students.begin(),students.end());
        int idx=0;
        int visit=0;

        while(!student.empty() && visit!=student.size()){
            if(sandwiches[idx]==student.front()){
                idx++;
                visit=0;
                student.pop_front();
            } else{
                visit++;
                int st=student.front();
                student.pop_front();
                student.push_back(st);
            }
        }

        return student.size();
    }
};