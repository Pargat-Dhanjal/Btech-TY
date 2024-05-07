#include <bits/stdc++.h>

using namespace std;

vector<string> words, wordOg;
string result, resultOg;
bool solExists = false;

void reverse(string &str)
{
    reverse(str.begin(), str.end());
}

void printProblem()
{
    cout << "\n";
    for (int i = 0; i < words.size(); i++)
    {
        for (int j = 0; j < words[i].size(); j++)
            cout << words[i][j];
        cout << "\n";
    }
    cout << "---------\n";
    for (int i = 0; i < result.size(); i++)
        cout << result[i];
    cout << "\n";
}

void printSolution(unordered_map<char, int> charValue)
{
    cout << "\n";
    for (int i = 0; i < words.size(); i++)
    {
        for (int j = 0; j < words[i].size(); j++)
            cout << charValue[wordOg[i][j]];
        cout << "\n";
    }
    cout << "---------\n";
    for (int i = 0; i < result.size(); i++)
        cout << charValue[resultOg[i]];
    cout << "\n";
}

void solve(int colIdx, int idx, int carry, int sum, unordered_map<char, int> charValue, vector<int> domain)
{

    if (colIdx < words.size())
    {
        if (idx < words[colIdx].size())
        {
            char ch = words[colIdx][idx];
            if (charValue.find(ch) != charValue.end())
            {
                solve(colIdx + 1, idx, carry, sum + charValue[ch], charValue, domain);
            }
            else
            {
                for (int i = 0; i < 10; i++)
                {
                    if (i == 0 && idx == words[colIdx].size() - 1)
                        continue;
                    if (domain[i] == -1)
                    {
                        domain[i] = 0;
                        charValue[ch] = i;
                        solve(colIdx + 1, idx, carry, sum + i, charValue, domain);
                        domain[i] = -1;
                    }
                }
            }
        }
        else
            solve(colIdx + 1, idx, carry, sum, charValue, domain);
    }
    else
    {
        if (charValue.find(result[idx]) != charValue.end())
        {
            if (((sum + carry) % 10) != charValue[result[idx]])
                return;
        }
        else
        {
            if (domain[(sum + carry) % 10] != -1)
                return;
            domain[(sum + carry) % 10] = 0;
            charValue[result[idx]] = (sum + carry) % 10;
        }
        carry = (sum + carry) / 10;
        if (idx == result.size() - 1 && (charValue[result[idx]] == 0 || carry == 1))
            return;
        if (idx + 1 < result.size())
            solve(0, idx + 1, carry, 0, charValue, domain);
        else
        {
            solExists = true;
            printSolution(charValue);
        }
    }
}

int main()
{
    unordered_map<char, int> charValue;
    vector<int> domain(10, -1);

    int n;
    cout << "\nEnter number of input words: ";
    cin >> n;
    cout << "\nEnter the words: ";
    for (int i = 0; i < n; i++)
    {
        string inp;
        cin >> inp;
        words.push_back(inp);
    }
    cout << "\nEnter the resultant word: ";
    cin >> result;

    printProblem();

    wordOg = words;
    resultOg = result;

    reverse(result);
    for (auto &itr : words)
        reverse(itr);

    solve(0, 0, 0, 0, charValue, domain);

    if (!solExists)
        cout << "\nNo Solution Exists!";
    return 0;
}