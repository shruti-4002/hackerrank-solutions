// LeetCode Problem: Spiral Matrix
// Link: https://leetcode.com/problems/spiral-matrix/
// Difficulty: Medium
// Language: cpp

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m= matrix[0].size();
        int n=matrix.size();

        int total=n*m;
        int c=0;

        int startrow=0;
        int startcol=0;
        int endcol=m-1;
        int endrow=n-1;
        vector<int>temp;
        while(c<total){

            //startrow=(startcol=>endcol);

            for(int i=startcol ;i<=endcol;i++){
                temp.push_back(matrix[startrow][i]);
                c++;
            }

            if(c==total)break;

            startrow++;

            //endcol=(startrow->endrow)

            for(int i=startrow ;i<=endrow;i++){
                temp.push_back(matrix[i][endcol]);
                c++;
            }

            if(c==total)break;

                endcol--;
            
            for(int i=endcol ;i>=startcol;i--){
                temp.push_back(matrix[endrow][i]);
                c++;
            }

            if(c==total)break;

                endrow--;
            
            for(int i=endrow ;i>=startrow;i--){
                temp.push_back(matrix[i][startcol]);
                c++;
            }

          
                startcol++;



        }

return temp;



    }
};