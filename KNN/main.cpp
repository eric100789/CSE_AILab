#include "knn_diabetes.h"

using namespace std;

int main()
{
    fstream test_file("DataA/test_data.csv");
    fstream train_file("DataA/train_data.csv");

    cout << "Input K: ";
    int k;
    cin >> k; 
    knn_diabetes data(train_file, test_file, 8, k);
    data.training();
    double ans = data.get_correct();
    cout << "Correct Rate: " << ans << endl;

    return 0;
}