// HackerRank Problem: For Loop
// Link: https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem
// Difficulty: Easy
// Language: cpp

#include<bits/stdc++.h>
using namespace std;
int main(){
int a,b,i;
string arr[]={"zero","one","two","three","four","five","six","seven","eight","nine"};
cin>>a>>b;
for(i=a;i<=b;i++){
    if(i<=9){
        cout<<arr[i]<<endl;
            }
    else{
        
        if(i%2==0){
            cout<<"even"<<endl;
                    }
        else{
            cout<<"odd"<<endl;
        }
    }
    
}

}
    
    



