import sys
import cv2
import os
import numpy as np

def random_nr(size, seed=None):
    seed or np.random.seed(seed=seed)
    return np.random.randint(0,2,size,dtype=np.uint8)



def main():
    for p in os.listdir("input/"):
        inp = cv2.imread("input/"+p,cv2.IMREAD_COLOR)
        rdp = random_nr(inp.shape,0)
        cv2.imwrite("output/p_"+p,rdp)
        rdp = rdp*(255-inp)+inp*(1-rdp)
        #cv2.imshow("inp",inp)
        cv2.imwrite("output/d_"+p,rdp)
        #cv2.imshow("rdp",rdp)
        #cv2.waitKey(0)

if __name__ == "__main__":
    main()
