#ifndef KNN_H
#define KNN_H

#include<iostream>
#include<math.h>
#include <vector>
#include<fstream>
#include <queue>

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

    void training();

    double get_correct();

protected:
    int dimension;
    int k;
    template <typename T> class cmp_distance;
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
    public:
    int a;
};

#endif