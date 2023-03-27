#include "knn_diabetes.h"

knn_diabetes::knn_diabetes(fstream& train_file, fstream& test_file, int dimension) : knn()
{
    vector< vector<double> > train_data, test_data;
    vector<int> train_label, test_label;

    string line;
    getline(train_file, line);
    while(true)
    {
        vector<double> temp;
        double val;
        for(int i=0 ; i<dimension; i++)
        {
            if(!(train_file >> val)) goto BREAK1;
            temp.push_back(val);
        }
        train_file >> val;
        temp.push_back(val);
        train_label.push_back((int)val);
        train_data.push_back(temp);
    }
    BREAK1:

    while(true)
    {
        vector<double> temp;
        double val;
        for(int i=0 ; i<dimension; i++)
        {
            if(!(test_file >> val)) goto BREAK2;
            temp.push_back(val);
        }
        test_file >> val;
        temp.push_back(val);
        test_label.push_back((int)val);
        test_data.push_back(temp);
    }
    BREAK2:
    this->dimension = dimension;
    this->train_data = train_data;
    this->train_label = train_label;
    this->test_data = test_data;
    this->test_label = test_label;
}


void knn_diabetes::read_file(fstream& train_file, fstream& test_file, int dimension)
{
    vector< vector<double> > train_data, test_data;
    vector<int> train_label, test_label;

    string line;
    getline(train_file, line);
    while(true)
    {
        vector<double> temp;
        double val;
        for(int i=0 ; i<dimension; i++)
        {
            if(!(train_file >> val)) goto BREAK1;
            temp.push_back(val);
        }
        train_file >> val;
        temp.push_back(val);
        train_label.push_back((int)val);
        train_data.push_back(temp);
    }
    BREAK1:

    while(true)
    {
        vector<double> temp;
        double val;
        for(int i=0 ; i<dimension; i++)
        {
            if(!(test_file >> val)) goto BREAK2;
            temp.push_back(val);
        }
        test_file >> val;
        temp.push_back(val);
        test_label.push_back((int)val);
        test_data.push_back(temp);
    }
    BREAK2:
    this->dimension = dimension;
    this->train_data = train_data;
    this->train_label = train_label;
    this->test_data = test_data;
    this->test_label = test_label;
}