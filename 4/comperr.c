#include<stdio.h>

void fun1(){
	static int a = 5;
	static int b = a;
	printf("%d",b);
}

int main(){
	fun1();
}