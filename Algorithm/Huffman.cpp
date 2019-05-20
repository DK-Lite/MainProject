#include <iostream>
#include <vector>
#include <queue>
using namespace std;


vector<char> text;
vector<char> text_c;
vector<char> text_r;

int seed = 1124;
int pseudo_rand()
{
	seed = seed * 214013 + 2531011;
	return (seed >> 16) & 0x7FFF;
}


struct Node
{
    char alpabet;
    int freq;
    Node* leftNode;
    Node* RigtNode;
    Node(int freq, char alpabet): freq(freq), alpabet(alpabet) {};
}

class Huffman
{

public:

    void set()
    {

    }
    void encode();
    void decode();

private:
    Node* head;
    priority_queue< Node, vector<Node>,  cmp > pq;
    struct cmp{
    bool operator()(Node t, Node u){
        return t.freq > u.freq;
    }
};
    



}

void init(vector<char>& text)
{
    int text_len = 50 + pseudo_rand()%950;
    for(int i = 0 ;i < text_len; i++)
    {
        text.push_back('A' + pseudo_rand()%26);
    }
}

int main()
{

    for(int c= 0 ; c < 1000; c++)
    {
        init();
        Huffman hm;

        hm.encode();
        score += compressionRate(text, text_);
        hm.decode();

        for(int i = 0; i< text.size(), i++)
        {
            if(text[i] != res[i]) score += 1000;
        }

        cout << score << endl;

    }




    return 0;
}