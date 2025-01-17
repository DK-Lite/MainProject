// ImageProc.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h"

#include <opencv\cv.h>
#include <opencv\highgui.h>

using namespace std;

void imgSharpening(cv::Mat& img, float sigma)
{
	cv::Mat tmp;
	cv::GaussianBlur(img, tmp, cv::Size(0, 0), sigma);
	cv::addWeighted(img, 1.5, tmp, -0.5, 0, img);
}


//Image processing 
// 1. image read
// 2. pre proessing 
// 3. recognition

#define MAX_BUF_IMAGE_NAME 100
#define RESIZE_WIDTH 720
#define RESIZE_HEIGHT 480

char INPUT_IMAGE_PATH[MAX_BUF_IMAGE_NAME] = { ".\\image\\1.png" };

char INPUT_VIDEO_PATH[MAX_BUF_IMAGE_NAME] = { ".\\image\\TestVideo.avi" };



int main()
{


	// image read
	//Mat img = imread(INPUT_IMAGE_PATH);

	VideoCapture video(INPUT_VIDEO_PATH);

	if (!video.isOpened())
		cout << " video error" << endl;

	video.set(CV_CAP_PROP_FRAME_WIDTH, 720);
	video.set(CV_CAP_PROP_FRAME_HEIGHT, 480);


	while (1) {
		Mat frame;
		video >> frame;

		resize(frame, frame, Size(RESIZE_WIDTH, RESIZE_HEIGHT), 0, 0, CV_INTER_NN);

		Mat gray, binary;
		Mat dst = Mat::zeros(frame.rows, frame.cols, CV_8UC3);
		cvtColor(frame, gray, CV_RGB2GRAY);



		/*	vector<KeyPoint> keypoints;
		Ptr<FeatureDetector> detector = FastFeatureDetector::create()
		vector<Mat> descriptor;

		detector->detect(gray, keypoints, Mat());

		drawKeypoints(frame, keypoints, frame);*/


		threshold(gray, binary, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
		////cv::adaptiveThreshold(gray, binary, 255, CV_ADAPTIVE_THRESH_MEAN_C, CV_THRESH_BINARY_INV, 3, 12);


		vector<vector<Point> > contours;
		vector<Vec4i> hierarchy;

		cv::findContours(binary, contours, hierarchy,
			CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0));



		//for (int i = 0; i >= 0; i = hierarchy[i][0]) {
		//	Scalar color(rand() % 255, rand() % 255, rand() % 255);
		//	cv::drawContours(dst, contours, i, color, CV_FILLED, 8, hierarchy);
		//}
		//

		//if (contours.size() > 0) {
		//	for (int i = 0; i < contours.size(); i++) {
		//		cv::Rect rect = cv::boundingRect(contours[i]);
		//		if (rect.height > 10 && rect.width > 40) {
		//			rectangle(frame, rect, Scalar(0, 255, 0), 3);
		//		}
		//	}
		//}


		imshow("video", frame);
		imshow("binary", binary);
		if (waitKey(20) == 27) break;

	}

	/*Mat src, gray, edge, binary;


	cv::resize(img, src, cv::Size(RESIZE_WIDTH, RESIZE_HEIGHT), 0, 0,
	CV_INTER_NN);
	*/




	//SceneTextDetection detector;

	//detector.Construct();
	//detector.extraction(src);




	//Mat img = imread("C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert.jpg");
	//Mat dst = Mat::zeros(src.rows, src.cols, CV_8UC3);
	//cvtColor(src, gray, CV_RGB2GRAY);



	/*vector<KeyPoint> keypoints;
	Ptr<FastFeatureDetector> detector = new FastFeatureDetector();
	vector<Mat> descriptor;

	detector->detect(gray, keypoints, Mat());
	drawKeypoints(gray, keypoints, gray);*/


	////threshold(gray, binary, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
	//cv::adaptiveThreshold(gray, binary, 255, CV_ADAPTIVE_THRESH_MEAN_C, CV_THRESH_BINARY_INV, 3, 12);

	//vector<vector<Point> > contours;
	//vector<Vec4i> hierarchy;

	//cv::findContours(binary, contours, hierarchy,
	//	CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE, Point(0,0));
	//
	//
	/*
	for (int i = 0; i >= 0; i = hierarchy[i][0]) {
	Scalar color(rand() % 255, rand() % 255, rand() % 255);
	cv::drawContours(dst, contours, i, color, CV_FILLED, 8, hierarchy);
	}
	*/

	/*if (contours.size() > 0) {
	for (int i = 0; i < contours.size(); i++) {
	cv::Rect rect = cv::boundingRect(contours[i]);
	if (rect.height > 10 && rect.width > 40) {
	rectangle(src, rect, Scalar(0, 255, 0), 3);
	}
	}
	}
	*/
	//imgSharpening(img, 1);

	//cv::Canny(gray, edge, 50, 200, 3);



	//imshow("origin", gray);
	//imshow("binary", binary);
	//imshow("edge", edge);
	//imshow("dst", dst);



	//waitKey(0);



	return 0;

}