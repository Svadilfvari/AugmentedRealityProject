import numpy as np

# First we require the mean values of u_i and v_i (aka x and y of each point)
def Normalize(points_source,points_target):#Now we normalize the data
    scaleFactorNormalizationTargetPoints,averageTargetX,averageTargetY=ComputeScalarNormalization(points_target)
    normalizationMatrix_TargetPoints_T=BuildNormalizationMatrix(scaleFactorNormalizationTargetPoints,averageTargetX,averageTargetY)
    
    scaleFactorNormalizationSourcePoints,averageSourceX,averageSourceY=ComputeScalarNormalization(points_source)
    normalizationMatrix_SourcePoints_T=BuildNormalizationMatrix(scaleFactorNormalizationSourcePoints,averageSourceX,averageSourceY)
    
    
    # After having the averages and the Scale Factor related to the Normalization we will build 
    
    NormalizedPoints_target=MultiplyMatrixArray(normalizationMatrix_TargetPoints_T,points_target)
    
    NormalizedPoints_source=MultiplyMatrixArray(normalizationMatrix_SourcePoints_T,points_source)
    return NormalizedPoints_source,NormalizedPoints_target,normalizationMatrix_SourcePoints_T,normalizationMatrix_TargetPoints_T
def ComputeArrayOfAverageOfEachCoordinate(pointsArray):
    return np.average(pointsArray, axis=0)


def ComputeScalarNormalization(pointsArray):
    n=len(pointsArray)
    
    arrayOfAverageOfEachCoordinate=ComputeArrayOfAverageOfEachCoordinate(pointsArray)
    
    averageX=arrayOfAverageOfEachCoordinate[0]
    averageY=arrayOfAverageOfEachCoordinate[1]
   
    arrayofXcoordinates=np.take(pointsArray,0,axis=1)
    arrayofYcoordinates=np.take(pointsArray,1,axis=1)
    
    # The below two lines will provide us with generators
    arrayFirstElementLeastSquare=((arrayofXcoordinates[i]-averageX)**2 for i in range(n-1))
    arraySecondElementLeastSquare=((arrayofYcoordinates[i]-averageY)**2 for i in range(n-1))
    
    
    #The below two lines will convert the generators to npArrays by making them a List first
    arrayFirstElementLeastSquare = np.array(list(arrayFirstElementLeastSquare))
    arraySecondElementLeastSquare = np.array(list(arraySecondElementLeastSquare))
    
    # The above was done so that we can apply :
    arrayAdditionRootElement=np.sqrt(np.add(arrayFirstElementLeastSquare, arraySecondElementLeastSquare)) 
    
    sumDenominator=sum(arrayAdditionRootElement)
    
    ScaleFactorNormalizationArrayPoints= 2**(1/2)*n/(sumDenominator)
    return ScaleFactorNormalizationArrayPoints,averageX,averageY
    


# After having the averages and the Scale Factor related to the Normalization we will build 
def BuildNormalizationMatrix(ScaleFactorNormalizationArrayPoints,averageX,averageY):
    
    NormalizationMatrix_T= np.array([
        [1,0,-averageX],
        [0,1, -averageY],
        [0,0, 1/ScaleFactorNormalizationArrayPoints]
     ])
        
    return ScaleFactorNormalizationArrayPoints*NormalizationMatrix_T

def MultiplyMatrixArray(matrix,arrayPoints):
    resultingArray=(np.matmul(matrix,arrayPoints[i]) for i in range(len(arrayPoints)))
    return  np.array(list(resultingArray))
    