#include <iostream>
#include <cctype>
#include <string>
using namespace std;
class Solution {
public:
    bool hasSameDigits(string s) {
        while(s.length()!=2){
            int sum = 0;
            int x = 1;
            int i = s.length()-1;
            while(i>=1){
            sum+=((int)s[i]+(int)s[i-1])*x;
            x=x*10;
            i--;
            }
            s=to_string(sum);
        }
        if(s[0]==s[1]){
            return true;
        }
        else{
            return false;
        }
    }
};
int main(){
    Solution obj;
    bool temp = obj.hasSameDigits("3902");
    if(temp){
        cout<<"true";
    }
    else{
        
        cout<<"false";
    }
}