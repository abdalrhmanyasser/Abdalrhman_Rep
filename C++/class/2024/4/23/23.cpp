#include <iostream>

const int MAX_STUDENTS = 20;

void fillGrades(int grades[], int numStudents);
void printGrades(int grades[], int numStudents);

using namespace std;

int main()
{
    int numStudents, grades[MAX_STUDENTS], target;
    cout << "Enter the number of students: ";
    cin >> numStudents;
    fillGrades(grades, numStudents);
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