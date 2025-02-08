import cv2
import imutils
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def get_number_plate(image):
    image = imutils.resize(image, width=500)
    img=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the original image

    # RGB to Gray scale conversion
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Noise removal with iterative bilateral filter(removes noise while preserving edges)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # Find Edges of the grayscale image
    edged = cv2.Canny(gray, 170, 200)

    # Find contours based on Edges
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
    cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] #sort contours based on their area keeping minimum required area as '30' (anything smaller than this will not be considered)
    NumberPlateCnt = None #we currently have no Number plate contour

    # loop over our contours to find the best possible approximate contour of number plate
    count = 0
    for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:  # Select the contour with 4 corners
                NumberPlateCnt = approx #This is our approx Number Plate Contour
                x,y,w,h = cv2.boundingRect(c)
                ROI = img[y:y+h, x:x+w]
                break

    if NumberPlateCnt is not None:
        # Drawing the selected contour on the original image
        cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)

    res=""
    
    #Find bounding box and extract ROI
    # try:
    #     cv2.imshow('image',ROI)
    #     cv2.waitKey(0)
    #     reader = easyocr.Reader(['en'])
    #     result = reader.readtext(image)
    #     for i in result:
    #         res+=i[1]+' '
    #     return res
    # except:
    #     return ""
        
for i in [6]:    
    img=cv2.imread(f"F:\\Nirma\\SEM-7\\Minor\\Minor Project\\Drive\\{i}.jpg")
    img=cv2.flip(img, 1)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    cv2.waitKey(0)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    cv2.imshow('image',gray)
    cv2.waitKey(0)
    edged = cv2.Canny(gray, 170, 200)
    cv2.imshow('image',edged)
    cv2.waitKey(0)
    text = pytesseract.image_to_string(edged, lang = 'eng')
    print(text)