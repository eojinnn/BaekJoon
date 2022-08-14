#include <stdio.h>
int sum(int x,int y);
int main(){
    int a,b,result;
    scanf("%d",&a);
    scanf("%d",&b);
    result = sum(a,b);
    printf("%d",result);
}
int sum(int x,int y){
    return x+y;
}

