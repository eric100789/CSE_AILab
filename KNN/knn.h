#ifndef KNN_H
#define KNN_H

#include<iostream>
#include<math.h>
#include <vector>
#include<fstream>

using namespace std;

class knn
{

public:
    knn(int dimension, 
        vector<vector<double>> train_data, 
        vector<int> train_label, 
        vector<vector<double>> test_data,
        vector<int> test_label);

    void normalize();

    double distance(vector<double>& tar1, vector<double>& tar2);

    int classify(vector<double>& target);

protected:
    int dimension;
    int k;
    vector<vector<double>> train_data;
    vector<int> train_label;
    vector<double> train_max;
    vector<double> train_min;
    vector<vector<double>> test_data;
    vector<int> test_label;
    vector<int> ans_label;
};

class knn_diabetes : public knn
{

};

#endif