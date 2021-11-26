#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, p, q;
	cin >> n >> p >> q;
	vector<int> a(n);
	for (int i=0; i<n; i++) {
		cin >> a[i];
	}

	int counter = 0;
	for (int i=0; i<n; i++) {
		for (int j=0; j<i; j++) {
			for (int k=0; k<j; k++) {
				for (int l=0; l<k; l++) {
					for (int m=0; m<l; m++) {
						int residual = 1LL * a[i] % p * a[j] % p * a[k] % p * a[l] % p * a[m] % p;
						if (residual == q) {
							counter += 1;
						}
					}
				}
			}
		}
	}

	cout << counter << endl;

	return 0;
}
