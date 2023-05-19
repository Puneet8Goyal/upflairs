#include<iostream>
using namespace std;

bool search(int arr[], int size, int key){
    for(int i=0;i<size;i++){
        if (arr[i]==key);
       { return 1;
    }


}
return 0;}


int main(){

    int arr[15]={1,2,3,4,5,6,7,8,9,0};
    cout<<endl<<"enter the element  to search"<<endl;
    int key;
    cin>> key;

    bool found=search(arr,15,key);

    if(found){
        cout<<"yes found";

    
    }

     else{
        cout<<"not found";
     }




}