#include "knn.h"

template <typename T>
class knn::cmp_distance {
    public: 
        bool operator()(T a, T b) {
            return a.distance < b.distance;
        }
};

knn :: knn()
{

}

knn :: knn(int dimension, int k, vector<vector<double> > train_data, vector<int> train_label, vector<vector<double> > test_data, vector<int> test_label)
{
    this->dimension = dimension;
    this->train_data = train_data;
    this->train_label = train_label;
    this->test_data = test_data;
    this->test_label = test_label;
    this->k = k;
}

void knn::normalize()
{
    int ROW = train_data.size();
    int ROW_TEST = test_data.size();
    for(int d=0 ; d<dimension ; d++)
    {
        double MAX = INT_MIN;
        double MIN = INT_MAX;
        for(int row=0; row<ROW ; row++)
        {
            if(train_data[row][d] > MAX) MAX = train_data[row][d];
            if(train_data[row][d] < MIN) MIN = train_data[row][d];
        }
        train_max.push_back(MAX);
        train_min.push_back(MIN);
    }
    
    for(int d=0 ; d<dimension ; d++)
    {
        for(int row=0; row<ROW ; row++)
        {
            train_data[row][d] = (train_data[row][d] - train_min[d])/(train_max[d] - train_min[d]);
        }
        for(int row=0; row<ROW_TEST ; row++)
        {
            test_data[row][d] = (test_data[row][d] - train_min[d])/(train_max[d] - train_min[d]);
        }
    }
}

double knn::distance(vector<double>& tar1, vector<double>& tar2)
{
    double dsum = 0;
    for(int i=0; i<dimension; i++)
    {
        dsum += pow((tar1[i] - tar2[i]),2);
    }
    return sqrt(dsum);
}

int knn::classify(vector<double>& target)
{
    typedef struct
    {
        double distance;
        int label;
    } data;
    
    priority_queue<data, vector<data>, cmp_distance<data> > pq;
    int label_arr[100] = {0};
    int max = INT_MIN;
    int max_index;
    
    for(int row=0; row<train_label.size(); row++)
    {
        data m_data = {this->distance(target,train_data[row]), train_label[row]};
        pq.push(m_data);
    }

    for(int i=0 ; i<k ; i++)
    {
        data d = pq.top();
        ++label_arr[d.label];
        pq.pop();
    }

    for(int i=0 ; i<100 ; i++)
    {
        if(label_arr[i]>max)
        {
            max = label_arr[i];
            max_index = i;
        }
    }
    return max_index;
}

void knn::training()
{
    ans_label.erase(ans_label.begin(), ans_label.end());
    for(int row=0; row<test_data.size(); row++)
    {
        ans_label.push_back( this->classify(test_data[row]) );
    }
}

double knn::get_correct()
{
    int correct_num = 0;
    int label_num = test_label.size();
    for(int i=0; i<label_num; i++)
    {
        correct_num += (test_label[i] == ans_label[i]);
    }
    return correct_num/label_num;
}