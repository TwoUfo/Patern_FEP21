#include "Sort.h"

using namespace std;

int x1, x2;
int n;
int a[1000];
int b[1000];

int main() 
{
	cin >> n;
	for (int i = 0; i < n; i++) cin >> a[i];

	int flag = 0;
	cin >> x1 >> x2;
	for (int i = x1; i <= x2; i++) {

		
		b[flag] = a[i];
		flag++;

	}

	

	//SortBubble(b, flag);
	//SortSelection(b, flag);
	SortInsertion(b, flag);




	for (int i = 0; i < x1; i++) {
		cout << a[i] << " ";
	}

	cout << "| ";

	for (int i = 0; i < flag; i++) {
		cout << b[i] << " ";
	}
	
	cout << "| ";

	for (int i = x2+1; i < n; i++) {
		cout << a[i] << " ";
	}



	int resMin = MinItem(a, x1, x2);
	int resMax = MaxItem(a, x1, x2);

	cout << endl << "min: " << a[resMin] << " max: " << a[resMax];
}



// 45 9 12 -78 5 85 12
// 41 20 -90 1 -9 78 -12 841 12 -52