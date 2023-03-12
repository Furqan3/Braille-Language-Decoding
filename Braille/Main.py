import cv2 as cv
import numpy as np
import copy as cp
# Braille Key

brkey = {
    (1, 0, 0, 0, 0, 0): 'a',
    (1, 1, 0, 0, 0, 0): 'b',
    (1, 0, 0, 1, 0, 0): 'c',
    (1, 0, 0, 1, 1, 0): 'd',
    (1, 0, 0, 0, 1, 0): 'e',
    (1, 1, 0, 1, 0, 0): 'f',
    (1, 1, 0, 1, 1, 0): 'g',
    (1, 1, 0, 0, 1, 0): 'h',
    (0, 1, 0, 1, 0, 0): 'i',
    (0, 1, 0, 1, 1, 0): 'j',
    (1, 0, 1, 0, 0, 0): 'k',
    (1, 1, 1, 0, 0, 0): 'l',
    (1, 0, 1, 1, 0, 0): 'm',
    (1, 0, 1, 1, 1, 0): 'n',
    (0, 0, 0, 1, 0, 1): 'n',
    (1, 0, 1, 0, 1, 0): 'o',
    (1, 1, 1, 1, 0, 0): 'p',
    (1, 1, 1, 1, 1, 0): 'q',
    (1, 1, 1, 0, 1, 0): 'r',
    (0, 1, 1, 1, 0, 0): 's',
    (0, 1, 1, 1, 1, 0): 't',
    (1, 0, 1, 0, 0, 1): 'u',
    (1, 1, 1, 0, 0, 1): 'v',
    (0, 1, 0, 1, 1, 1): 'w',
    (1, 0, 1, 1, 0, 1): 'x',
    (1, 0, 1, 1, 1, 1): 'y',
    (1, 0, 1, 0, 1, 1): 'z',
    (0, 0, 0, 0, 0, 0): ' ',
}
#Calculating Rows


def calculate_row(label):
    Rows = []
    rows = []
    cell = []
    count = 0
    
    for i in range(label.shape[0]):
        a = label[i,:]
        
        if np.all(a == 0):
            continue
        
        if np.all(label[i-1,:] == 0):
            cell.append(i)
        
        if np.all(label[i+1,:] == 0):
            count += 1
            cell.append(i)
            rows.append(cell)
            cell = []
            
        if count == 3:
            count = 0
            Rows.append(rows)
            rows = []
    return Rows    
# Colume Counting

def count_mycolumn(Image):
        cell=[]
        col=[]
        for i in range(Image.shape[1]):
          if np.all(Image[:,i]==0):
            if np.all(Image[:,i-1]==0):
              continue
            else:
              cell.append(i)
              col.append(cell)
              cell=[]
                    
          else:
           
              if np.all(Image[:,i-1]==0):
                  if len(col)!=0:
                      a=col[-1]
                      b=i-a[1]
                      if (b>30) and (b<60):
                        x=c=a[1]-a[0]
                        cell.append(a[1]+1)
                        cell.append(a[1]+x+1)
                        col.append(cell)
                        cell=[]
                      elif b>120:
                        x=c=a[1]-a[0]
                        cell.append(a[1]+1)
                        cell.append(a[1]+x+1)
                        col.append(cell)
                        cell=[]
                        x=c=a[1]-a[0]
                        cell.append(a[1]+1)
                        cell.append(a[1]+x+1)
                        col.append(cell)
                        cell=[]
                        cell.append(i-1)
                        cell.append(a[1]-1-x)
                        col.append(cell)
                        cell=[]
                      elif (b>80):
                        x=c=a[1]-a[0]
                        cell.append(a[1]+1)
                        cell.append(a[1]+x+1)
                        col.append(cell)
                        cell=[]
                        cell.append(i-1)
                        cell.append(a[1]-1-x)
                        col.append(cell)
                        cell=[]
                  cell.append(i)
        return col  
# Finding Braille Matrix


def Decode_matrix(rows,column,image):
    cell=[]
    decode=[]
    count=0
    for i in rows:
       for j in column:
            for k in i:
                count+=1
                if np.all(image[k[0]:k[1],j[0]:j[1]]==0):
                    cell.append(0)
                else:
                   cell.append(1)
                if count==6:
                    decode.append(cell)
                    count=0
                    cell=[]
    return decode
# Converting To string

def convertingtostr(matrix):
  for i in matrix:
    if np.sum(i)==1:
      print('a',end='')
    else:
      print(brkey[tuple(i)],end='')
def main():
    image = cv.imread('sample.png', 0)
    image=255-image
    _, image = cv.threshold(image, 127, 255, 0)
    
    row=calculate_row(image)
    count=0
    for i in row:
      a=i[0]
      b=i[-1]
      img=cp.copy(image[a[0]-2:b[1]+2,:])
      row2=calculate_row(img)
      col=count_mycolumn(img)
      count+=1
      if count==7:
        None
      decoded=Decode_matrix(row2,col,img)
      convertingtostr(decoded)
      print(' ')

if __name__ == "__main__":
    main()