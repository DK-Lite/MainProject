#include <iostream>
using namespace std;

int seed = 1124;
int pseudo_rand()
{
	seed = seed * 214013 + 2531011;
	return (seed >> 16) & 0x7FFF;
}

class PriorityQ
{
#define ROOT 1
#define PARENT(x) x / 2
#define LEFT_NODE(x) (x * 2)
#define RIGT_NODE(x) (x * 2) + 1

public:
    PriorityQ() {};
    void push(int val)
    {
        _size++;
        _data[_size] = val;

        int child = _size;
        while(
            PARENT(child) > 0 && 
            _data[child] > _data[PARENT(child)])
        {
            _swap(_data[PARENT(child)], _data[child]);
            child = PARENT(child);
        }
    }
    int pop()
    {
        _size--;
        _data[ROOT] = _data[_size];

        int parent = ROOT;
        while(parent < _size)
        {
           if(
            _data[LEFT_NODE(parent)] > _data[RIGT_NODE(parent)] &&
            _data[LEFT_NODE(parent)] > _data[parent])
            {
                _swap(_data[LEFT_NODE(parent), _data[parent]);
                parent = LEFT_NODE(parent);
            } 
            else if(
            _data[RIGT_NODE(parent)] > _data[LEFT_NODE(parent)] &&
            _data[RIGT_NODE(parent)] > _data[parent])
            {
                _swap(_data[RIGT_NODE(parent), _data[parent]);
                parent = RIGT_NODE(parent);
            } 
            else break;
        }
    
    }
    int size()
    {
        return _size;
    }
    int top()
    {
        return _data[ROOT];
    }


private:
    int _data[100];
    int _size;
    void _swap(int& a, int& b)
    {
        int tmp = a;
        a = b;
        b = tmp;
    }


};

int main(){

    PriorityQ pq;
    int n;
    cin >> n;
    for(int i = 0 ;i <n; i++)
    {
        pq.push(pseudo_rand()%1000);
    }

    for(int i = 0 ;i <n; i++){
        cout << pq.top() << endl;
        pq.pop();
    }

    return 0;
}