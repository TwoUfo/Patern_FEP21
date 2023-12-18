/*     Допоміжні функції     */

#include <iostream>

void Swap(int &a, int &b) {
	int flag = a;
	a = b;
	b = flag;
}

int MinItem(int a[], int pos, int n) {
    int min = a[pos];
    int minIndex = pos;
    for (int i = pos+1; i <= n; i++) {
        if (a[i] < min) {
            min = a[i];
            minIndex = i;
        }
    }
    return minIndex;
}

int MaxItem(int a[], int pos, int n) {
    int max = a[pos];
    int maxIndex = pos;
    for (int i = pos + 1; i <= n; i++) {
        if (a[i] > max) {
            max = a[i];
            maxIndex = i;
        }
    }
    return maxIndex;
}

/*     Функції сортування     */

void SortBubble(int a[], int n) {
	for (int i = 0; i < n-1; i++) {
		for (int j = 0; j < n-i-1; j++) {
			if(a[j] > a[j+1]) Swap(a[j], a[j+1]);
		}
	}
}

void SortInsertion(int a[], int n) {
    int flag, j;
    for (int i = 0; i < n; i++) {
        flag = a[i];

        j = i - 1;
        while (j >= 0 && a[j] > flag) {
            a[j + 1] = a[j]; 
            j--;
        }
        a[j + 1] = flag;
    }
}

void SortSelection(int a[], int n) {
    for (int i = 0; i <= n; i++) {
        int min = MinItem(a, i, n-1);

        Swap(a[i], a[min]);

    }
}
