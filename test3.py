import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img = cv2.imread('Untitled.jpeg')
results = model(img)
results.save()

result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6]=='person']

tmp_img = cv2.imread('Untitled.jpeg')
print(tmp_img.shape)
cropped = tmp_img[int(result[0][1]):int(result[0][3]), int(result[0][0]):int(result[0][2])]
cropped1 = tmp_img[int(result[1][1]):int(result[1][3]), int(result[1][0]):int(result[1][2])]
cropped2 = tmp_img[int(result[2][1]):int(result[2][3]), int(result[2][0]):int(result[2][2])]
cropped3 = tmp_img[int(result[3][1]):int(result[3][3]), int(result[3][0]):int(result[3][2])]
cropped4 = tmp_img[int(result[4][1]):int(result[4][3]), int(result[4][0]):int(result[4][2])]

cv2.imwrite('people1.png', cropped)
cv2.imwrite('people2.png', cropped1)
cv2.imwrite('people3.png', cropped2)
cv2.imwrite('people4.png', cropped3)
cv2.imwrite('people5.png', cropped4)


