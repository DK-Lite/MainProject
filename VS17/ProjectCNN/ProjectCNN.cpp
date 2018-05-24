// test.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
class dimension {

public:
	dimension() {};
	~dimension() { delete Mat; };
	dimension(const dimension& copy) {
		Mat = new float[mCol * mRow];
		for (int i = 0; i < mCol*mRow; i++) {
			Mat[i] = copy.Mat[i];
		}
	}
	dimension(int col, int row) {
		mCol = col;
		mRow = row;
		Mat = new float[mCol * mRow];
	}

	int cols() {
		return mCol;
	}
	int rows() {
		return mRow;
	}
	int at(int col, int row)
	{
		return Mat[col * mRow + row];
	}
	void at(int col, int row, float value)
	{
		Mat[col * mRow + row] = value;
	}

	dimension operator * (dimension& another)
	{
		if (this->mRow != another.cols()) return;

		dimension retMat(mCol, another.mRow);

		for (int col = 0; col < this->mCol; col++) {
			for (int row = 0; row < another.mRow; row++) {

				int sum = 0;
				for (int i = 0; i < another.rows(); i++)
					sum += this->at(col, i) * another.at(i, row);

				retMat.at(col, row, sum);
			}
		}
		return retMat;
	}

	dimension operator + (dimension& another)
	{
		if (this->cols != another.cols() || this->mRow != another.rows()) return;

		dimension retMat(mCol, another.mRow);

		for (int col = 0; col < another.cols(); col++) {
			for (int row = 0; row < another.mRow; row++) {
				int sum = this->at(col, row) + another.at(col, row);
				retMat.at(col, row, sum);
			}
		}
		return retMat;
	}



private:
	float* Mat;
	int mCol, mRow;
};


class CNN {

public:

	int constuct();

	int run();

	int predict();



};
void print_dim(dimension dim) {
	for (int i = 0; i < dim.cols(); i++) {
		for (int j = 0; j < dim.rows(); j++) {
			cout << dim.at(i, j) << " ";
		}
		cout << endl;
	}
}

template<size_t X, size_t Y>
dimension array_to_dim(void* buf[Y][X], int row, int col)
{
	dimension retMat;


	return retMat;
}




int main()
{

	float dummy1[1][3] = { 1, 2, 3 };
	float dummy2[3][1] = { { 3 },{ 1 },{ 1 } };


	//dimension y(3, 1);
	dimension x = array_to_dim(dummy1, 1, 3);
	dimension y = array_to_dim(dummy2, 3, 1);

	dimension ret = x * y;

	print_dim(ret);

}