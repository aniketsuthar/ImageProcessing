import cv2

img = cv2.imread("galaxy.jpg", 0)
resize_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
cv2.imshow("Galaxy", resize_img)
cv2.imwrite("galaxy_resized_latest.jpg", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(type(img))
print(img)
print("Image Shape ", img.shape)
print("Img Dimension: ", img.ndim)

# cv2.resize(img, "g.jpg", 0.5, 0.5, interpolation=True)
# resized_image = cv2.resize("galaxy.jpg", int(img.shape[1] / 2), int(img.shape[0] / 2))
# print(resized_image)
