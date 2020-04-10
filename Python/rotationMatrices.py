""" Module contains several rotations 
    and coordinate transformations 
 
    Usage:  import rotationMatrices  
"""
import numpy as np 

def ECEF2LLA(posECEF): 
    """ 
        Transforms an ECEF coordinate system 
        to a LLA coordinate system  

        Input:   ECEF in [m]  
        Returns: LLA in [deg, deg, m]  
    """
    #Constants
    semiMinorEarthRadius =  6356752.3 #[meters]
    semiMajorEarthRadius =  6378137 #[meters]
    eccentricity = np.sqrt(1 - np.square( np.divide(semiMinorEarthRadius, semiMajorEarthRadius) ))
    
    #Empirical model that calculates a position in LLA given a position in ECEF; ref: 
    #http://elfanceswithcode.net/engineeringnotes/geodetic_to_ecef/geodetic_to_ecef.html
    ecc2 = np.square(eccentricity) #eccentricity square 
    #Empirical constants for this model 
    a1 = semiMajorEarthRadius * ecc2 
    a2 = np.square(a1) 
    a3 = 0.5 * a1 * ecc2 
    a4 = 2.5 * a2 
    a5 = a1 + a3 
    a6 = 1 - ecc2 
    radius = np.linalg.norm(posECEF)
    u = a2 / radius 
    v = a3 - (a4 / radius)
    s2 = np.square(posECEF[2]) / np.square(radius) 
    c2 = (np.square(posECEF[0]) + np.square(posECEF[1])) / np.square(radius) 
    #End of empirical constants  
    posLLA = np.zeros(3) 
    posLLA[1] = np.degrees(np.arctan(posECEF[1]/posECEF[0])) #Longitude
    if c2  > 0.3:
        s = ((np.abs(posECEF[2])) / radius) * (1 + c2 * (a1 + u + s2 * v) / radius)
        posLLA[0] = np.arcsin(s) #Latitude 
        c = np.sqrt(1 - np.square(s))
    else:
        c = np.sqrt(c2) * (1 - s2 * (a5 - u - c2 * v) / radius)
        posLLA[0] = np.arccos(c) #Latitude 
        s = np.sqrt(1 - np.square(c)) 
    g = 1 - ecc2 * np.square(s) 
    rg = semiMajorEarthRadius / np.sqrt(g) 
    rf = a6 * rg 
    u = np.sqrt(c2) * radius - (rg * c)# FIX ME  
    v = np.abs(posECEF[2]) - (rf * s) 
    f = (c * u) + (s * v) 
    m = (c * v) - (s * u) 
    p = m / (rf / g + f) 
    posLLA[0] = np.degrees(posLLA[0] + p) #Latitude 
    posLLA[2] = f + (0.5 * m * p)  #Longitude 
    if posECEF[2] < 0:
        posLLA[0] *= -1
    return posLLA #End ECEF2LLA


def LLA2ECEF(posLLA): 
    """ 
        Transforms a LLA coordinate system 
        to a LLA coordinate system  
        
        Input:   LLA in [deg, deg, m] 
        Returns: ECEF in [m]  
    """
    #Constants
    semiMinorEarthRadius =  6356752.3 #[meters]
    semiMajorEarthRadius =  6378137 #[meters]
    eccentricity = np.sqrt(1 - np.square( np.divide(semiMinorEarthRadius, semiMajorEarthRadius) ))
    
    #Lat, Long angles 
    cLat = np.cos(np.deg2rad(posLLA[0])) 
    sLat = np.sin(np.deg2rad(posLLA[0]))
    cLon = np.cos(np.deg2rad(posLLA[1])) 
    sLon = np.sin(np.deg2rad(posLLA[1])) 
    
    radiusOfCurvature = np.divide( semiMajorEarthRadius, np.sqrt(1 - np.square(eccentricity * sLat)) )     
    posECEF = np.zeros(3)
    posECEF[0] = (radiusOfCurvature + posLLA[2]) * cLat * cLon    #x-direction 
    posECEF[1] = (radiusOfCurvature + posLLA[2]) * cLat * sLon    #y-direction
    posECEF[2] = ((1 - np.square(eccentricity)) * radiusOfCurvature + posLLA[2]) * sLat   #z-direction
    return posECEF #End LLA2ECEF 


def ECEF2NED(posECEF, refLLA): 
    """ 
        Transforms an ECEF coordinate system 
        to a NED coordinate system  

        Input:   ECEF [m] and LLA [deg, deg, m] 
        Returns: NED in [m, m, m]  
    """
    #Check if a reference frame for the NED is given, if not assume LLA as the ref frame 
    refPosECEF = LLA2ECEF(refLLA)  #Assumes that my reference is at the LLA provided  
    cLat = np.cos(np.deg2rad(refLLA[0])) 
    sLat = np.sin(np.deg2rad(refLLA[0]))
    cLon = np.cos(np.deg2rad(refLLA[1])) 
    sLon = np.sin(np.deg2rad(refLLA[1]))    
    losECEF = posECEF - refPosECEF  #Line of Sight Vector
    rotECEF2NED = np.array([ [-sLat*cLon, -sLat*sLon, cLat], [-sLon, cLon, 0], [-cLat*cLon, -cLat*sLon, -sLat] ])  
    posNED = np.dot(rotECEF2NED, losECEF) 
    return posNED  #End ECEF2NED  


def rollMatrix(rollAngleDeg):  
    """ 
        Creates a roll rotation matrix  

        Input:   roll angle in [deg]  
        Returns: roll rotation matrix [ ] 
    """
    rollAngRad = np.asarray(np.radians(rollAngleDeg))
    R = np.zeros((3,3)) 
    R[0,0] = 1
    R[1,1] = np.cos(rollAngRad) 
    R[1,2] = -np.sin(rollAngRad) 
    R[2,1] = np.sin(rollAngRad) 
    R[2,2] = np.cos(rollAngRad)
    return R #End rollMatrix


def pitchMatrix(pitchAngleDeg): 
    """ 
        Creates a pith rotation matrix  

        Input:   pith angle in [deg]  
        Returns: pitch rotation matrix [ ] 
    """
    pitchAngRad = np.asarray(np.radians(pitchAngleDeg)) 
    P = np.zeros((3,3))
    P[0,0] = np.cos(pitchAngRad) 
    P[0,2] = np.sin(pitchAngRad) 
    P[1,1] = 1 
    P[2,0] = -np.sin(pitchAngRad) 
    P[2,2] = np.cos(pitchAngRad) 
    return P #End pitchMatrix


def yawMatrix(yawAngleDeg): 
    """ 
        Creates a yaw rotation matrix  

        Input:   yaw angle in [deg]  
        Returns: yaw rotation matrix [ ] 
    """
    yawAngRad = np.asarray(np.radians(yawAngleDeg)) 
    Y = np.zeros((3,3)) 
    Y[0,0] = np.cos(yawAngRad) 
    Y[0,1] = -np.sin(yawAngRad) 
    Y[1,0] = np.sin(yawAngRad) 
    Y[1,1] = np.cos(yawAngRad) 
    Y[2,2] = 1
    return Y #End yawMatrix


def cartesianUV(inpVector): #Calculates the Cartesian unit inpVector
    """ 
        Calculates the cartesian unit vector 

        Input:   a 3d vector [x, y, z] 
        Returns: cartesian unit vector      
    """
    cartessianUV = np.divide(inpVector, np.linalg.norm(inpVector)) 
    return cartessianUV #End cartesianUV 


def cylindricalUV(inpVector): #Calculates the cylindrical unit inpVector
    """ 
        Calculates the cylindrical unit vector 

        Input:   a 3d vector [x, y, z] 
        Returns: cylindrical unit vectors [radial, azimuthal, elevation]        
    """
    cylindricalUV = np.zeros((3,3))
    #Radial Unit inpVector
    cylindricalUV[0,0] = np.cos(np.radians(inpVector[1])) 
    cylindricalUV[0,1] = np.sin(np.radians(inpVector[1])) 
    #Azimuthal Unit inpVector 
    cylindricalUV[1,0] = -np.sin(np.radians(inpVector[1])) 
    cylindricalUV[1,1] = np.cos(np.radians(inpVector[1]))
    #Elevation Unit inpVector 
    cylindricalUV[2,2] = 1 
    return cylindricalUV #End cylindricalUV


def sphericalUV(inpVector): #Calculates the spherical unit inpVector 
    """ 
        Calculates the spherical unit vector 

        Input:   a 3d vector [x, y, z] 
        Returns: spherical unit vectors [radial, azimuthal, elevation]        
    """
    sphericalUV = np.zeros((3,3))
    #Radial Unit inpVector
    sphericalUV[0,0] = np.cos(np.radians(inpVector[1])) * np.sin(np.radians(inpVector[2]))
    sphericalUV[0,1] = np.sin(np.radians(inpVector[1])) * np.sin(np.radians(inpVector[2]))
    sphericalUV[0,2] = np.cos(np.radians(inpVector[2])) 
    #Azimuthal Unit inpVector 
    sphericalUV[1,0] = -np.sin(np.radians(inpVector[1]))
    sphericalUV[1,1] = np.cos(np.radians(inpVector[1]))
    #Elevation Unit inpVector 
    sphericalUV[2,0] = np.cos(np.radians(inpVector[1])) * np.cos(np.radians(inpVector[2]))
    sphericalUV[2,1] = np.sin(np.radians(inpVector[1])) * np.sin(np.radians(inpVector[2]))
    sphericalUV[2,2] = -np.sin(np.radians(inpVector[2])) 
    return sphericalUV #End sphericalUV


def cartesian2Spherical(inpVector):
    """ 
        Converts a cartesian vector to a spherical vector  

        Input:   a 3d cartesian  [x, y, z] 
        Returns: a 3d spherical vector [radial, azimuthal, elevation] 
    """
    sphericalVec = np.zeros(3) 
    sphericalVec[0] = np.linalg.norm(inpVector)                           #radius 
    sphericalVec[1] = np.degrees(np.arctan(inpVector[1] / inpVector[0]))    #azimuthal angle 
    sphericalVec[2] = np.degrees(np.arccos(inpVector[2] / sphericalVec[0])) #elevation angle
    return sphericalVec #End cartersian2Spherical 


def cartesian2Cylindrical(inpVector):
    """ 
        Converts a cartesian vector to a cylindrical vector  

        Input:   a 3d cartesian  [x, y, z] 
        Returns: a 3d cylindrical  vector [radial, azimuthal, elevation] 
    """
    cylindricalVec = np.zeros(3) 
    cylindricalVec[0] = np.sqrt(np.square(inpVector[0]) + np.square(inpVector[1])) #radius 
    cylindricalVec[1] = np.degrees(np.arctan(inpVector[1] / inpVector[0]))           #azimuthal angle
    cylindricalVec[2] = inpVector[2]                                               #elevation 
    return cylindricalVec #End cartesian2Cylindrical


def cylindrical2Cartesian(inpVector):
    """ 
        Converts a cylindrical vector to a cartesian vector  

        Input:   a 3d cylindrical  vector [radial, azimuthal, elevation] 
        Returns: a 3d cartesian vector [x, y, z] 
    """
    cartesianVec = np.zeros(3) 
    cartesianVec[0] = inpVector[1] * np.cos(np.radians(inpVector[1]))   #x-direction
    cartesianVec[1] = inpVector[1] * np.sin(np.radians(inpVector[1]))   #y-direction
    cartesianVec[2] = inpVector[2]                                      #z-direction 
    return cartesianVec #End cylindrical2Cartesian 


def spherical2Cartesian(inpVector):
    """ 
        Converts a spherical vector to a cartesian vector  

        Input:   a 3d spherical vector [radial, azimuthal, elevation] 
        Returns: a 3d cartesian vector [x, y, z] 
    """
    cartesianVec = np.zeros(3) 
    cartesianVec[0] = inpVector[0] * np.cos(np.radians(inpVector[1])) * np.sin(np.radians(inpVector[2])) #x-direction
    cartesianVec[1] = inpVector[0] * np.sin(np.radians(inpVector[1])) * np.sin(np.radians(inpVector[2])) #y-direction
    cartesianVec[2] = inpVector[0] * np.cos(np.radians(inpVector[2]))                                    #z-direction
    return cartesianVec #End spherical2Cartesian

