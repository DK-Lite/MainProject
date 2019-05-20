// Binary Search Tree

#include "stdafx.h"
#include <iostream>
using namespace std;
#define MAX_INT 0x7fffffff
struct Node {
	int data;
	Node* left;
	Node* right;
	Node():data(MAX_INT), left(NULL), right(NULL) {};
	Node(int val):data(val), left(NULL), right(NULL) {};
};
class BST{

public:
	Node* head;

	BST(): head(NULL) {};
	~BST() 
	{
		delete[] head;
	}

	void insert(int data)
	{
		if (head == NULL)
		{
			head = new Node(data);
			return;
		}
		_insert(head, data);
	}
	void rotation()
	{

	}

	bool search(int data)
	{
		return _search(head, data);
	}
	void printPreoder()
	{
		_preorder(head);
	}
	void printInorder()
	{
		_inorder(head);
	}
	void printPostorder()
	{
		_postorder(head);
	}
	
private:
	void _insert(Node* p, int data)
	{
		if (p->data > data)
		{
			if (p->left == NULL) 
			{
				p->left = new Node(data);
			}
			else _insert(p->left, data);
			return;
		}

		if (p->right == NULL)
		{
			p->right = new Node(data);
		}
		else _insert(p->right, data);	
	}
	bool _search(Node* p, int data)
	{
		if (p == NULL) 
			return false;

		if (p->data == data) 
			return true;

		if (p->data < data) 
			return _search(p->left, data);
		
		return _search(p->right, data);
	}

	void _preorder(Node* p)
	{
		if (p == NULL) return;
		cout << p->data <<" ";
		_preorder(p->left);
		_preorder(p->right);
	}
	void _inorder(Node* p)
	{
		if (p == NULL) return;
		_inorder(p->left);
		cout << p->data << " ";
		_inorder(p->right);
	}
	void _postorder(Node* p)
	{
		if (p == NULL) return;
		_postorder(p->left);
		_postorder(p->right);
		cout << p->data << " ";
	}

};
void create(int* s, int size)
{

}
int main() {

	BST bs;

	int n;
	int s[1000];
	cin >> n;


	for (int i = 0; i < n; i++)
	{
		cin >> s[i];
		bs.insert(s[i]);
	}
	
	//create(s, n);

	bs.printPreoder();
	cout << endl;
	bs.printInorder();
	cout << endl;
	bs.printPostorder();
	cout << endl;

	return 0;
}