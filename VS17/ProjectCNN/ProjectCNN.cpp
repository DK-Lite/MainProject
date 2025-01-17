// test.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
#include <memory>
using namespace std;
class dimension {

public:
	dimension() {};
	~dimension() { delete Mat; };
	dimension(const dimension& copy) {
		this->mCol = copy.mCol;
		this->mRow = copy.mRow;
		this->Mat = new float[mCol * mRow];
		for (int i = 0; i < mCol*mRow; i++) 
			this->Mat[i] = copy.Mat[i];
		
	}
	dimension(int col, int row) {
		mCol = col;
		mRow = row;
		Mat = new float[mCol * mRow];
	}

	int cols() { return mCol; }
	int rows() { return mRow; }
	float at(int col, int row)
	{ 
		return Mat[col * mRow + row]; 
	}
	void at(int col, int row, float value)
	{ 
		Mat[col * mRow + row] = value; 
	}

	dimension operator * (dimension& another)
	{
		dimension retMat(this->cols(), another.rows());

		if (this->rows() != another.cols()) return retMat;


		for (int col = 0; col < this->mCol; col++) {
			for (int row = 0; row < another.mRow; row++) {

				float sum = 0;
				for (int i = 0; i < another.cols(); i++)
					sum += this->at(col, i) * another.at(i, row);

				retMat.at(col, row, sum);
			}
		}
		return retMat;
	}

	dimension operator + (dimension& another)
	{

		dimension retMat(this->cols(), another.rows());

		if (this->cols() != another.cols() || this->mRow != another.rows()) return retMat;


		for (int col = 0; col < another.cols(); col++) {
			for (int row = 0; row < another.mRow; row++) {
				float sum = this->at(col, row) + another.at(col, row);
				retMat.at(col, row, sum);
			}
		}
		return retMat;
	}

	dimension operator == (dimension& another)
	{

		dimension retMat(this->cols(), another.rows());

		for (int col = 0; col < another.cols(); col++) 
			for (int row = 0; row < another.mRow; row++) 
				retMat.at(col, row, another.at(col, row));
		

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


void print_dim(dimension& dim) {
	for (int i = 0; i < dim.cols(); i++) {
		for (int j = 0; j < dim.rows(); j++) {
			cout << dim.at(i, j) << " ";
		}
		cout << endl;
	}
}

template<size_t cols, size_t rows>
dimension array_to_dim(float (&buf)[cols][rows])
{
	dimension retMat(cols,rows);
	
	for (int i = 0; i < cols; i++)
		for (int j = 0; j < rows; j++)
			retMat.at(i, j, buf[i][j]);

	return retMat;
}




int main()
{

	float dummy1[2][3] = { {1, 2, 3},{1, 2, 3} };
	float dummy2[3][2] = { { 3,3},{ 1,1 },{2,1} };
	float dummy3[2][2] = { {1,1}, {1,1} };

	//dimension y(3, 1);
	//dimension  x, y, b, ret;

	dimension x = array_to_dim(dummy1);
	dimension y = array_to_dim(dummy2);
	dimension b = array_to_dim(dummy3);

	print_dim(y);

	x * y;
	//y = x * y + b;

	print_dim(y);

}