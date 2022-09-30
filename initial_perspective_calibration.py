#https://docs.opencv.org/3.3.0/dc/dbb/tutorial_py_calibration.html

import numpy as np
import cv2
import glob
# import camera_realworldxyz

# cameraXYZ=camera_realworldxyz.camera_realtimeXYZ()

calculatefromCam=True

imgdir="/home/pi/Desktop/Captures/"

writeValues=True





#test camera calibration against all points, calculating XYZ

#load camera calibration
savedir="camera_data/"
cam_mtx=np.load(savedir+'cam_mtx.npy')
dist=np.load(savedir+'dist.npy')
newcam_mtx=np.load(savedir+'newcam_mtx.npy')
roi=np.load(savedir+'roi.npy')


#load center points from New Camera matrix
cx=newcam_mtx[0,2]
cy=newcam_mtx[1,2]
fx=newcam_mtx[0,0]
print("cx: "+str(cx)+",cy "+str(cy)+",fx "+str(fx))


#MANUALLY INPUT YOUR MEASURED POINTS HERE
#ENTER (X,Y,d*)
#d* is the distance from your point to the camera lens. (d* = Z for the camera center)
#we will calculate Z in the next steps after extracting the new_cam matrix


#world center + 8 world points

total_points_used=9

X_center=1.71
Y_center=3.125
Z_center=40
# worldPoints=np.array([[X_center,Y_center,Z_center],
#                        [2.5,2.5,35.18],
#                        [0,2.5,35.09],
#                        [-2.5,2.5,35.18],
#                        [2.5,0,35.09],
#                        [-2.5,0,35.09],
#                        [2.5,-2.5,35.18],
#                        [0,-2.5,35.09],
#                        [-2.5,-2.5,35.18]], dtype=np.float32)

# worldPoints=np.array([[X_center,Y_center,Z_center],
#                        [-5,5,87.46],
#                        [0,5,83.81],
#                        [5,5,87.46],
#                        [-5,0,83.81],
#                        [5,0,83.81],
#                        [-5,-5,87.46],
#                        [0,-5,83.81],
#                        [5,-5,87.46]], dtype=np.float32)

# worldPoints=np.array([[X_center,Y_center,Z_center],
#                        [-5,-5,87.46],
#                        [-5,0,83.81],
#                        [-5,5,87.46],
#                        [0,-5,83.81],
#                        [0,5,83.81],
#                        [5,-5,87.46],
#                        [5,0,83.81],
#                        [5,5,87.46]], dtype=np.float32)

# worldPoints=np.array([[X_center,Y_center,Z_center],
#                        [7.2,7,41.24],
#                        [7.2,0,40.64],
#                        [7.2,-7,41.24],
#                        [0,7,40.61],
#                        [0,-7,40.61],
#                        [-7.2,7,41.24],
#                        [-7.2,0,40.64],
#                        [-7.2,-7,41.24]], dtype=np.float32)

worldPoints=np.array([[X_center,Y_center,Z_center],
                       [5.2,5,40.64],
                       [5.2,0,40.34],
                       [5.2,-5,40.64],
                       [0,5,40.31],
                       [0,-5,40.31],
                       [-5.2,5,40.64],
                       [-5.2,0,40.34],
                       [-5.2,-5,40.64]], dtype=np.float32)


#MANUALLY INPUT THE DETECTED IMAGE COORDINATES HERE

#[u,v] center + 9 Image points
# imagePoints=np.array([[cx,cy],
#                        [332.7,332.6],
#                        [479.5,332.6],
#                        [626.3,332.6],
#                        [332.7,479.4],
#                        [626.3,479.4],
#                        [332.7,626.3],
#                        [479.5,626.3],
#                        [626.3,626.3]], dtype=np.float32)

# imagePoints=np.array([[cx,cy],
#                        [716,296],
#                        [959,296],
#                        [1202,296],
#                        [716,539],
#                        [1202,539],
#                        [716,782],
#                        [959,782],
#                        [1202,782]], dtype=np.float32)

imagePoints=np.array([[cx,cy],
                       [1125,359],
                       [1126,529],
                       [1128,698],
                       [949,362],
                       [953,701],
                       [775,364],
                       [777,533],
                       [778,702]], dtype=np.float32)


#FOR REAL WORLD POINTS, CALCULATE Z from d*

for i in range(1,total_points_used):
    #start from 1, given for center Z=d*
    #to center of camera
    wX=worldPoints[i,0]-X_center
    wY=worldPoints[i,1]-Y_center
    wd=worldPoints[i,2]

    d1=np.sqrt(np.square(wX)+np.square(wY))
    wZ=np.sqrt(np.square(wd)-np.square(d1))
    worldPoints[i,2]=wZ

print(worldPoints)


#print(ret)
print("Camera Matrix")
print(cam_mtx)
print("Distortion Coeff")
print(dist)

print("Region of Interest")
print(roi)
print("New Camera Matrix")
print(newcam_mtx)
inverse_newcam_mtx = np.linalg.inv(newcam_mtx)
print("Inverse New Camera Matrix")
print(inverse_newcam_mtx)
if writeValues==True: np.save(savedir+'inverse_newcam_mtx.npy', inverse_newcam_mtx)

print(">==> Calibration Loaded")


print("solvePNP")
ret, rvec1, tvec1=cv2.solvePnP(worldPoints,imagePoints,newcam_mtx,dist)

print("pnp rvec1 - Rotation")
print(rvec1)
if writeValues==True: np.save(savedir+'rvec1.npy', rvec1)

print("pnp tvec1 - Translation")
print(tvec1)
if writeValues==True: np.save(savedir+'tvec1.npy', tvec1)

print("R - rodrigues vecs")
R_mtx, jac=cv2.Rodrigues(rvec1)
print(R_mtx)
if writeValues==True: np.save(savedir+'R_mtx.npy', R_mtx)

print("R|t - Extrinsic Matrix")
Rt=np.column_stack((R_mtx,tvec1))
print(Rt)
if writeValues==True: np.save(savedir+'Rt.npy', Rt)

print("newCamMtx*R|t - Projection Matrix")
P_mtx=newcam_mtx.dot(Rt)
print(P_mtx)
if writeValues==True: np.save(savedir+'P_mtx.npy', P_mtx)

#[XYZ1]



#LETS CHECK THE ACCURACY HERE


s_arr=np.array([0], dtype=np.float32)
s_describe=np.array([0,0,0,0,0,0,0,0,0,0],dtype=np.float32)


def calculate_XYZ(u,v):
                                      
    #Solve: From Image Pixels, find World Points

    uv_1=np.array([[u,v,1]], dtype=np.float32)
    uv_1=uv_1.T
    # suv_1=scalingfactor*uv_1
    suv_1=s_arr[0]*uv_1
    xyz_c=inverse_newcam_mtx.dot(suv_1)
    xyz_c=xyz_c-tvec1
    XYZ=inverse_R_mtx.dot(xyz_c)

    return XYZ

for i in range(0,total_points_used):
    print("=======POINT # " + str(i) +" =========================")
    
    print("Forward: From World Points, Find Image Pixel")
    XYZ1=np.array([[worldPoints[i,0],worldPoints[i,1],worldPoints[i,2],1]], dtype=np.float32)
    XYZ1=XYZ1.T
    print("{{-- XYZ1")
    print(XYZ1)
    suv1=P_mtx.dot(XYZ1)
    print("//-- suv1")
    print(suv1)
    s=suv1[2,0]    
    uv1=suv1/s
    print(">==> uv1 - Image Points")
    print(uv1)
    print(">==> s - Scaling Factor")
    print(s)
    s_arr=np.array([s/total_points_used+s_arr[0]], dtype=np.float32)
    print(s_arr)
    s_describe[i]=s
    if writeValues==True: np.save(savedir+'s_arr.npy', s_arr)

    print("Solve: From Image Pixels, find World Points")

    uv_1=np.array([[imagePoints[i,0],imagePoints[i,1],1]], dtype=np.float32)
    uv_1=uv_1.T
    print(">==> uv1")
    print(uv_1)
    suv_1=s*uv_1
    print("//-- suv1")
    print(suv_1)

    print("get camera coordinates, multiply by inverse Camera Matrix, subtract tvec1")
    xyz_c=inverse_newcam_mtx.dot(suv_1)
    xyz_c=xyz_c-tvec1
    print("      xyz_c")
    inverse_R_mtx = np.linalg.inv(R_mtx)
    XYZ=inverse_R_mtx.dot(xyz_c)
    print("{{-- XYZ")
    print(XYZ)


    # if calculatefromCam==True:
    #     cXYZ=cameraXYZ.calculate_XYZ(imagePoints[i,0],imagePoints[i,1])
    #     print("camXYZ")
    #     print(cXYZ)
    if calculatefromCam==True:
        cXYZ=calculate_XYZ(imagePoints[i,0],imagePoints[i,1])
        print("camXYZ")
        print(cXYZ)


s_mean, s_std = np.mean(s_describe), np.std(s_describe)

print(">>>>>>>>>>>>>>>>>>>>> S RESULTS")
print("Mean: "+ str(s_mean))
#print("Average: " + str(s_arr[0]))
print("Std: " + str(s_std))

print(">>>>>> S Error by Point")

for i in range(0,total_points_used):
    print("Point "+str(i))
    print("S: " +str(s_describe[i])+" Mean: " +str(s_mean) + " Error: " + str(s_describe[i]-s_mean))



ansTest1 = calculate_XYZ(1127,613)
ansTest2 = calculate_XYZ(687,449)
ansTest3 = calculate_XYZ(831,349)
print(ansTest1)
print(ansTest2)
print(ansTest3)