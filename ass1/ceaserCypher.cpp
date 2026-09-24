
//CEASER CYPHER
#include <bits/stdc++.h>

using namespace std;

string en(string s,int key) {
    string temp ="";
    for(int i = 0 ;i<s.size();i++){
        int countt = (int)s[i] + key; 
        if(countt>26){
            countt = countt % 26;
        }
        char hh = (char)countt;
        temp+=hh;
    }

    return temp;
}

string dn(string s,int key){
    string temp = "";
    for(int i = 0;i<s.size();i++){
        if(isalpha (s[i])){
            char base = islower(s[i]) ? 'a' :'A';
            char aa = (s[i] -base- key +26)%26+base;
            
            temp += aa;
        }
        else temp+=s[i];
    }
    
    return temp;
}


int main() { 
    string s = "mit wpu";
    string encrys = en(s,3);
    cout<<"plane text ->" <<s<<endl;
    cout<<"encrypted text (ceaser cypher) ->" << encrys << endl ;
    string decrys = dn(encrys,3);
    cout<<"decrypted text (ceaser cypher) -> "<<decrys<<endl;
    return 0;
}
