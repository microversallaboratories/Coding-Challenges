//Prompt: There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a 
//function that returns the number of unique ways you can climb the staircase. 
//The order of the steps matters. 

#include <iostream>

using namespace std;

int fibo(int n){ 	//Recursive definition:
	int output = 0; 	//Initialize as zero.
	if (n == 0){		//Base case.
		return 0;
	}
	else if (n == 1){
		return 1;
	}
	else{
		output = fibo(n-2) + fibo(n-1);
	}
	return output;
}

int main(){
	int n;
	cout << "Enter a value for n: ";
	cin >> n;
	cout << fibo(n) << "unique ways to climb the staircase." << endl;
	
	return 0;
}

