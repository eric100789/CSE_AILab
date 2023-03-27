#ifndef KNN_DIABETES_H
#define KNN_DIABETES_H

#include "knn.h"
#include <sstream>
#include <string>

class knn_diabetes : public knn
{
    public:
    knn_diabetes(fstream& train_file, fstream& test_file, int dimension, int k);
    void read_file(fstream& train_file, fstream& test_file, int dimension, int k);
};

#endif