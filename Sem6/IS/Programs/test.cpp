#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tt;
    cin >> tt;
    while (tt--)
    {
        int n,m;
        cin >> n >> m;
        int arr[n];
        for(int i=0;i<n;i++)
            cin >> arr[i];
            
        int ans = 0,sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
            if (sum >= m) {
                ans++;
                sum = 0;
            }
        }
        cout << ans << endl;
    }
}