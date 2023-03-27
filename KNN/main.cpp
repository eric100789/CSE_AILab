#include "knn_diabetes.h"

using namespace std;

int main()
{
    fstream test_file("DataA/test_data.csv");
    fstream train_file("DataA/train_data.csv");

    knn_diabetes data(train_file, test_file, 8, 5);
    data.training();
    double ans = data.get_correct();
    cout << ans << endl;

    return 0;
}