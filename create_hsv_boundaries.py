import cv2
import numpy as np

'''
	# GREEN HSV VALUES (10:45, 40:255, 10:255), (65:255, 255, 255)
	# RED HSV VALUES (0, 30:255, 0:230), (0:45, 255, 255)
'''

def donothing(e):
	pass

def main():

	bars_window = np.zeros((40, 512, 3), dtype=np.uint8)
	cv2.namedWindow('bars_image')

	# tackbars for HSV value lower and upper.
	# lower
	cv2.createTrackbar('HLower', 'bars_image', 0, 255, donothing)
	cv2.createTrackbar('SLower', 'bars_image', 0, 255, donothing)
	cv2.createTrackbar('VLower', 'bars_image', 0, 255, donothing)

	# upper
	cv2.createTrackbar('HUpper', 'bars_image', 0, 255, donothing)
	cv2.createTrackbar('SUpper', 'bars_image', 0, 255, donothing)
	cv2.createTrackbar('VUpper', 'bars_image', 0, 255, donothing)

	while True:

		frame = cv2.imread('land.jpg')
		frame = cv2.resize(frame, (300, 300))

		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		'''
			Getting the current positions of the trackbars
			and with it create the mask boundries hsv_lower and hsv_upper
		'''

		cv2.imshow('bars_image', bars_window)

		# lower values
		hl = int(cv2.getTrackbarPos('HLower', 'bars_image'))
		sl = int(cv2.getTrackbarPos('SLower', 'bars_image'))
		vl = int(cv2.getTrackbarPos('VLower', 'bars_image'))

		# upper values
		hu = int(cv2.getTrackbarPos('HUpper', 'bars_image'))
		su = int(cv2.getTrackbarPos('SUpper', 'bars_image'))
		vu = int(cv2.getTrackbarPos('VUpper', 'bars_image'))

		# create lower and uppder boundires
		lower_red = np.array([hl, sl, vl],  dtype=np.uint8)
		upper_red = np.array([hu, vu, su], dtype=np.uint8)

		mask = cv2.inRange(hsv_frame, lower_red, upper_red)

		res = cv2.bitwise_and(frame, frame, mask=mask)

		cv2.imshow('frame', frame)
		cv2.imshow('res', res)

		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

if __name__ == '__main__':
	main()
