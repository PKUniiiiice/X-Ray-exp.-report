import numpy as np

hkl = np.mat([[1,0,0],
              [0,0,2],
              [1,0,1],
              [1,0,2],
              [1,1,0],
              [1,0,3],
              [2,0,0],
              [1,1,2],
              [2,0,1],
              [0,0,4],
              [2,0,2],
              [1,0,4],
              [2,0,3]])

dbtheta = np.array([31.77369,34.43401,36.25530,47.55143,56.59651,62.85849,66.37830,67.95403,69.07955,72.57889,76.95818,81.37841,89.60493])

alpha = np.array(np.square(hkl[:,0]) + np.multiply(hkl[:,0],hkl[:,1]) + np.square(hkl[:,1])).flatten()
gamma = np.array(np.square(hkl[:,2])).flatten()
delta = 10 * np.square(np.sin(np.radians(dbtheta)))

coef = np.zeros((3,3))

coef[0,0] = np.dot(alpha,alpha)
coef[0,1] = np.dot(alpha,delta)
coef[0,2] = np.dot(alpha,gamma)
coef[1,1] = np.dot(delta,delta)
coef[1,2] = np.dot(gamma,delta)
coef[2,2] = np.dot(gamma,gamma)

coef = coef + np.triu(coef,k=1).T

b = np.zeros((3,1))

b[0]=np.dot(alpha,np.square(np.sin(np.radians(0.5*dbtheta))))
b[1]=np.dot(delta,np.square(np.sin(np.radians(0.5*dbtheta))))
b[2]=np.dot(gamma,np.square(np.sin(np.radians(0.5*dbtheta))))

solve = np.linalg.solve(coef,b)

a = np.sqrt(1.5406**2/(solve[0]*3))
c = np.sqrt(1.5406**2/(solve[2]*4))

print('解:\n{0} \n\n a:\n{1} \n\n c:\n{2}'.format(solve,a,c))