from Normalization import *

def find_homography(points_source, points_target):
    A  = construct_A(points_source, points_target)#construct our A matrix using the function 
    u, s, vh = np.linalg.svd(A, full_matrices=True)#compute the svd 
    
    # Solution to H is the last column of V, or last row of V transpose
    homography = vh[-1].reshape((3,3)) # the reshape method gives a new shape to an array without changing its data
                                       #In this case the last column(vh[-1] represents the element before the first one)
                                       #matrix vh[-1] is reshaped as 3*3 matrix while originally being a vector
                                       #with a length of 9
    
    return homography/homography[2,2]#normalize H

def construct_A(points_source, points_target):
    assert points_source.shape == points_target.shape, "Shape does not match" #verify that the sizes are the same (3D)
    num_points = points_source.shape[0] #Extract the number of points from the points source matrix
                                        #in this case : shape[0]= length of the matrix => the number of points
    matrices = [] 
    for i in range(num_points):
        partial_A = construct_A_partial(points_source[i], points_target[i]) #Construct a "portion" of the A matrix (which
                                                                            #means that it constructs the A matrix for 
                                                                            #one point)
        matrices.append(partial_A) # we add the resulting matrix to the emmpty matrix
    return np.concatenate(matrices, axis=0)

def construct_A_partial(point_source, point_target):
    x, y, z = point_source[0], point_source[1], 1
    x_t, y_t, z_t = point_target[0], point_target[1], 1
    #A_partial represents the A matrix for one point 
    # Even after changing the hereafter line nothing has changed 
    A_partial = np.array([
        [0, 0, 0, -z_t*x, -z_t*y, -z_t*z, y_t*x, y_t*y, y_t*z],
        [z_t*x, z_t*y, z_t*z, 0, 0, 0, -x_t*x, -x_t*y, -x_t*z]
    ])
    return A_partial

def Denormalize(normalized_Homography,normalizationMatrix_SourcePoints_T,normalizationMatrix_TargetPoints_T):
    Reversed_Tsource=np.linalg.inv(normalizationMatrix_SourcePoints_T)
    reversed_Tsource_mult_NormHomography=np.matmul(Reversed_Tsource,normalized_Homography)
    H=np.matmul(reversed_Tsource_mult_NormHomography,normalizationMatrix_TargetPoints_T)
    return H

def BuildKMatrix():
    # Building the K matrix
    #From the calibration of the camera we've done using matlab we found that 
    #all length units are in mm 
    Focal_length_X = 3146.7211
    Focal_length_Y =3150.2599
    Principal_point_X=1960.7933
    Principal_point_Y=1503.0496
    
    K=np.zeros((3,3))
    K[0][0]=Focal_length_X
    K[1][1]=Focal_length_Y
    K[0][2]=Principal_point_X
    K[1][2]=Principal_point_Y
    K[2][2]=1
    
    return K

def BuildProjectionMatrix(H,K):
    #reverse the K matrix to get the results of K^-1*H
    reverse_K = np.linalg.inv(K)
    
    
    
    homography_mult_Reverse_K=np.matmul(reverse_K,H)
    
    R1_tilde=np.array(homography_mult_Reverse_K[:,0]) #The first column
    R2_tilde=np.array(homography_mult_Reverse_K[:,1]) #The second column
    Trans_tilde=np.array(homography_mult_Reverse_K[:,2]) #The third column
    
    #promoting the arrays from row to column ones
    R1_tilde = R1_tilde[:, np.newaxis]
    R2_tilde = R2_tilde[:, np.newaxis]
    Trans_tilde = Trans_tilde[:, np.newaxis]
    
    firstColumnRotationaMatrix=R1_tilde#which is in reality a times R1_tilde representing R1
    secondColumnRotationaMatrix=R2_tilde#which is in reality a times R2_tilde representing R2
    #set the third parameter axis=0 which tells cross that the vectors are defined along the first axis, rather than the last axis
    thirdColumnRotationaMatrix=np.cross(R1_tilde,R2_tilde,axis=0)#which is in reality (a^2 times R1_tilde cross R2_tilde) representing R3
    
    
    rotationalMatrixTilde=np.concatenate([firstColumnRotationaMatrix,secondColumnRotationaMatrix,thirdColumnRotationaMatrix], axis=1)  
    
    
    
    firstSolutionScaleFactor= np.linalg.det(rotationalMatrixTilde)**(-1/4)
    
    secondSolutionScaleFactor=-firstSolutionScaleFactor
    fourthColumnProjectionMatrix=firstSolutionScaleFactor*(Trans_tilde)
    
    rotationalMatrixProjection=firstSolutionScaleFactor*rotationalMatrixTilde
    rotationalMatrixProjection[:,2]*=firstSolutionScaleFactor
    
    projectionMatrixFirstSolution=np.hstack((rotationalMatrixProjection,fourthColumnProjectionMatrix) )
    #Since the determinent is negative the first solution is the correct one
    if np.linalg.det(rotationalMatrixProjection)>0:
        projectionMatrixFirstSolution=1*projectionMatrixFirstSolution
    else:
        projectionMatrixFirstSolution=-1*projectionMatrixFirstSolution
    
    
    
    #append the last row representing the 0 0 0 1
    homogenousLine=np.array([0,0,0,1])
    
    projectionMatrixFirstSolution=np.vstack([projectionMatrixFirstSolution,homogenousLine])
    return projectionMatrixFirstSolution
    
    

    