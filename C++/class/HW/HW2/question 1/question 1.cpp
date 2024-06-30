#include <iostream>

const int MAX_STUDENTS = 20;

void fillGrades(int grades[], int numStudents);
void printGrades(int grades[], int numStudents);
int findHighestGrade(int grades[], int numStudents);
int findLowestGrade(int grades[], int numStudents);
double findAverageGrade(int grades[], int numStudents);
bool sequentialSearch(int grades[], int numStudents, int target);
void bubbleSort(int grades[], int numStudents);

using namespace std;

int main()
{
    int numStudents, grades[MAX_STUDENTS], target;
    cout << "Enter the number of students: ";
    cin >> numStudents;
    fillGrades(grades, numStudents);
    printGrades(grades, numStudents);
    cout << "Highest Grade : " << findHighestGrade(grades, numStudents) << "\n";
    cout << "Lowest Grade : " << findLowestGrade(grades, numStudents) << "\n";
    cout << "Average Grade : " << findAverageGrade(grades, numStudents) << "\n";
    cout << "Enter the target you want to sequential search for" << "\n";
    cin >> target;
    cout << "Does " << target << " exist in the grades : "  << (sequentialSearch(grades, numStudents, target) ? "true" : "false") << "\n";
    cout << "Before sort : \n";
    printGrades(grades, numStudents);
    bubbleSort(grades, numStudents);
    cout << "After sort : \n";
    printGrades(grades, numStudents);
}
void fillGrades(int grades[], int numStudents)
{
    cout << "Enter grades for " << numStudents << " students:\n";
    for (int i = 0; i < numStudents; ++i)
    {
        cout << "Enter grade for student " << i + 1 << ": ";
        cin >> grades[i];
    }
}

void printGrades(int grades[], int numStudents)
{
    cout << "Student grades:\n";
    for (int i = 0; i < numStudents; ++i)
    {
        cout << "Student " << i + 1 << ": " << grades[i] << endl;
    }
}

int findHighestGrade(int grades[], int numStudents)
{
    int highestGrade = grades[0];
    for (int i = 1; i < numStudents; ++i)
    {
        if (grades[i] > highestGrade)
        {
            highestGrade = grades[i];
        }
    }
    return highestGrade;
}

int findLowestGrade(int grades[], int numStudents)
{
    int lowestGrade = grades[0];
    for (int i = 1; i < numStudents; ++i)
    {
        if (grades[i] < lowestGrade)
        {
            lowestGrade = grades[i];
        }
    }
    return lowestGrade;
}

double findAverageGrade(int grades[], int numStudents)
{
    int total = 0;
    for (int i = 0; i < numStudents; ++i)
    {
        total += grades[i];
    }
    return (double)(total) / numStudents;
}

bool sequentialSearch(int grades[], int numStudents, int target)
{
    for (int i = 0; i < numStudents; ++i)
    {
        if (grades[i] == target)
        {
            return true;
        }
    }
    return false;
}
void bubbleSort(int grades[], int numStudents)
{
    int i, j, temp;
    for (i = (numStudents - 1); i >= 0; i--)
        for (j = 1; j <= i; j++)
            if (grades[j - 1] > grades[j])
            {
                temp = grades[j - 1];
                grades[j - 1] = grades[j];
                grades[j] = temp;
            }
}