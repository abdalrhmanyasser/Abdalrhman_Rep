#include <iostream>

void fillAges(int Ages[], int numStudents);
void printAges(int Ages[], int numStudents);
int findHighestAge(int Ages[], int numStudents);
int findLowestAge(int Ages[], int numStudents);
double findAverageAge(int Ages[], int numStudents);
void bubbleSort(int Ages[], int numStudents);

using namespace std;

int main()
{
    int numStudents = 10, Ages[10];
    fillAges(Ages, numStudents);
    printAges(Ages, numStudents);
    cout << "Highest Age : " << findHighestAge(Ages, numStudents) << "\n";
    cout << "Lowest Age : " << findLowestAge(Ages, numStudents) << "\n";
    cout << "Average Age : " << findAverageAge(Ages, numStudents) << "\n";
    cout << "Before sort : \n";
    printAges(Ages, numStudents);
    bubbleSort(Ages, numStudents);
    cout << "After sort : \n";
    printAges(Ages, numStudents);
}
void fillAges(int Ages[], int numStudents)
{
    cout << "Enter Ages for " << numStudents << " students:\n";
    for (int i = 0; i < numStudents; ++i)
    {
        cout << "Enter Age for student " << i + 1 << ": ";
        cin >> Ages[i];
    }
}

void printAges(int Ages[], int numStudents)
{
    cout << "Student Ages:\n";
    for (int i = 0; i < numStudents; ++i)
    {
        cout << "Student " << i + 1 << ": " << Ages[i] << endl;
    }
}

int findHighestAge(int Ages[], int numStudents)
{
    int highestAge = Ages[0];
    for (int i = 1; i < numStudents; ++i)
    {
        if (Ages[i] > highestAge)
        {
            highestAge = Ages[i];
        }
    }
    return highestAge;
}

int findLowestAge(int Ages[], int numStudents)
{
    int lowestAge = Ages[0];
    for (int i = 1; i < numStudents; ++i)
    {
        if (Ages[i] < lowestAge)
        {
            lowestAge = Ages[i];
        }
    }
    return lowestAge;
}

double findAverageAge(int Ages[], int numStudents)
{
    int total = 0;
    for (int i = 0; i < numStudents; ++i)
    {
        total += Ages[i];
    }
    return (double)(total) / numStudents;
}

void bubbleSort(int Ages[], int numStudents)
{
    int i, j, temp;
    for (i = (numStudents - 1); i >= 0; i--)
        for (j = 1; j <= i; j++)
            if (Ages[j - 1] > Ages[j])
            {
                temp = Ages[j - 1];
                Ages[j - 1] = Ages[j];
                Ages[j] = temp;
            }
}