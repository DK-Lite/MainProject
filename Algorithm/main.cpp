#include "stdafx.h"
#include <iostream>
#include <string.h>
using namespace std;

struct Node {
	int data;
	Node * next;
	Node(Node* p, int value) : data(value), next(p) {};
};


class Stack {
    public:

    int     _size;
    Node*   _top;

    Stack() : _top(NULL), _size(0) {};

    void push(int value)
    {
        _size++;
        if(empty())
        {
            _top = new Node(NULL, value);
            return;
        }
        _top = new Node(_top, value);
    }
    void pop()
    {
        if(empty()) return;
        _size--;
        Node* tptr = _top;
        _top = _top->next;
        delete (tptr);
    }
    bool empty()
    {
        return (_top == NULL);
    }
    int size()
    {
        return _size;
    }
    int top()
    {
        if(empty()) return -1;
        return _top->data;
    }
}

int main() {


	Stack stk;
	int n;
	cin >> n;
	char s[10];
	for (int i = 0; i < n; i++) {
		cin >> s;
		if (!strcmp(s, "push")) {
			int value;
			cin >> value;
			stk.push(value);
		}
		if (!strcmp(s, "top")) {
			cout << stk.top() << endl;
		}
		if (!strcmp(s, "size")) {
			cout << stk.size() << endl;
		}
		if (!strcmp(s, "empty")) {
			cout << stk.empty() << endl;
		}
		if (!strcmp(s, "pop")) {
			cout << stk.top() << endl;
            stk.pop();
		}
	}
}



class Queue {

public:

	int		_size;
	Node*	_front;
	Node*	_rear;

	Queue() : _front(NULL), _rear(NULL), _size(0) {};

	void push(int value)
	{
		_size++;
		if (empty())
		{
			_front = _rear = new Node(NULL, value);
			return;
		}
		_rear = _rear->next = new Node(NULL, value);
	}

	void pop()
	{
		if (empty()) return;
		_size--;

		Node* ptr = _front;
		_front = _front->next;

		if (_front == NULL)
			_rear = _front;

		delete (ptr);
	}
	bool empty()
	{
		return (_front == NULL && _rear == NULL);
	}
	int size()
	{
		return _size;
	}
	int front()
	{
		if (empty()) return -1;
		return _front->data;
	}
	int back()
	{
		if (empty()) return -1;
		return _rear->data;
	}


};
int main() {

	int n;
	cin >> n;

	Queue q;
	char s[1000];
	for (int i = 0; i < n; i++) {
		cin >> s;

		if (!strcmp(s, "push")) {
			int a;
			cin >> a;
			q.push(a);
		}
		if (!strcmp(s, "front")) {
			cout << q.front() << endl;
		}
		if (!strcmp(s, "back")) {
			cout << q.back() << endl;
		}
		if (!strcmp(s, "size")) {
			cout << q.size() << endl;
		}
		if (!strcmp(s, "empty")) {
			cout << q.empty() << endl;
		}
		if (!strcmp(s, "pop")) {
			cout << q.front() << endl;
			q.pop();
		}
	}
	return 0;
}