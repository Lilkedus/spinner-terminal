#include <iostream>
#include <vector>
using namespace std;

int main()
{
    srand(time(0));

    int randNum = rand() % 35;
    int numOfItems;

    cout << "How many items do you want to you in the spinner?\n";
    cin >> numOfItems;

    vector<string> items;

    for (int i = 0; i < numOfItems; i++)
    {
        cout << "Enter an item (" << i << "/" << numOfItems << "): \n";
        cin >> items[i];
    }

    return 0;
}