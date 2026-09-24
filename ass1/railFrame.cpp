#include <bits/stdc++.h>

using namespace std ;
// objective - > create rail frame algorithm for encrypting a string
// plane text -> hello world 
// h   o   l 
//  e l w r d 
//   l   o 
// encrypted text -> holelwrdlo
string en (string s,int key){
    char rail[key][s.length()];
    
    for(int i = 0 ; i < key ; i ++){
        for(int j = 0 ; j < (int)s.length(); j++){
            rail[i][j] ='\n';
        }
    }
    bool dir_down = false;
    int row = 0 ;int col = 0 ;
    for(int i = 0;i<s.length();i++){
        if ( row == 0||row == key -1){
            dir_down= !dir_down;
        }
        rail[row][col++] = s[i];

        dir_down?row++:row--;
    }

    string res =""; 
    for(int i =0 ;i<key;i++){
        for(int j = 0; j<s.length();j++){
            if(rail[i][j]!='\n'){
                res+=rail[i][j];
            }
        }
    }

    return res;
}
string de (string s,int key){
    char rail[key][s.length()];
    
    for(int i = 0 ; i < key ; i ++){
        for(int j = 0 ; j < (int)s.length(); j++){
            rail[i][j] ='\n';
        }
    }
    bool dir_down = false;
    int row = 0 ;int col = 0 ;
    for(int i = 0;i<s.length();i++){
        if ( row == 0||row == key -1){
            dir_down= !dir_down;
        }
        rail[row][col++] = s[i];

        dir_down?row++:row--;
    }

    string res =""; 
    for(int i =0 ;i<key;i++){
        for(int j = 0; j<s.length();j++){
            if(rail[i][j]!='\n'){
                res+=rail[i][j];
            }
        }
    }

    return res;
}


int main(){
    string s ="hello world";
    cout<<"plane text -> "<<s<<endl;
    cout<<"encrypted text -> "<< en(s,3)<<endl;
    cout<<"decrypted text -> "<<de(en(s,3) , 3)<<endl;
    return 0;
}