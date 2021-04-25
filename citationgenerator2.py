import streamlit as st
from sympy import *
from sympy import * 
import json
import numpy as np
st.title('MA1508E Algebric Simplifier')

number_input_1 = st.text_input("Please enter the text that you would wish to simplify",value="x")
truncated_output = simplify(number_input_1)
st.write(truncated_output)
# x = Symbol('x')
# solved = solve(number_input_1,x)
# st.write(solved)
polynomialMatrix = st.text_input("Please enter the polynomial Matrix", value=[1,2,3])
polynomialMatrix = json.loads(polynomialMatrix)
polynomialMatrix = np.poly1d(polynomialMatrix).r
polynomialMatrix = str(polynomialMatrix)
st.write("The roots are ", polynomialMatrix)



st.header("RREF calculator")
writtenStuff = st.text_input("Please enter the matrix", value=[[1,0]])
writtenStuff = json.loads(writtenStuff)
st.write(type(writtenStuff))
M = Matrix(writtenStuff)
M_rref = M.rref()
# st.write(np.array(M_rref)


st.header("Projection Vector Calculator")
projectiona = st.text_input("Please enter the matrix A", value=[[1,0]])
projectionb = st.text_input("Please enter the matrix B", value=[[1,0]])
projectiona = json.loads(projectiona)
projectionb = json.loads(projectionb)
aMatrix = np.array(projectiona)
bMatrix = np.array(projectionb)
aTransposeMatrix = np.array(transpose(aMatrix))
st.subheader("A and A Transpose")
st.write(aMatrix,aTransposeMatrix)

st.subheader("A*ATranpose = ")
AdotAtranspose = np.dot(aTransposeMatrix,aMatrix)
st.write(AdotAtranspose)
AdotAtranspose  =AdotAtranspose.astype(np.float64)
main1 = True
AdotAtransposeLinear = AdotAtranspose
while main1:
    try:
        st.subheader("Inverted A*Atranspose")
        AdotAtransposeLinear = np.array(np.linalg.inv(np.matrix(AdotAtranspose)))
        st.write(AdotAtransposeLinear)
        break
    except:
        st.write("It is singular")
        main1=False
        break

def calc_proj_matrix(A):
    return A*np.linalg.inv(A.T*A)*A.T

def calc_proj(b, A):
    P = calc_proj_matrix(A)
    return P*b.T

st.subheader("Projection Vector P is")
st.write(np.matrix(AdotAtranspose).dtype)
main2 = True
main3 = True
while main2:
    try: 
        answer = projectiona * (np.dot(aTransposeMatrix, bMatrix) / np.dot(aTransposeMatrix, aMatrix))

        st.write(answer)
        break
    except:
        while main3:
            try:
                calc_proj_matrix(aMatrix)
            except:
                st.write("Singular Check")
                main3 = False
        main2 = False
            # aMatrix = aMatrix.astype(np.float64)
            # aTransposeMatrix = aTransposeMatrix.astype(np.float64)
            # otherAnswer = aMatrix*AdotAtransposeLinear*aTransposeMatrix
   

        break
main4 = True
while main4:
    try:
        st.subheader("Main Projection Matrix is")
        st.write(np.array(calc_proj(bMatrix,aMatrix)))
    except:
        st.write("Aint not using this bruh")
        main4 = false


st.header("Simple Orthogonalisation of matracies")
# vectorx = st.text_input("Please enter the matrix 1", value=[3,3,[5,-2,-4,-2,8,-2,-4,-2,5]])
# vectorx = json.loads(vectorx)
vectorx = st.text_input("Please enter the matrix Name", value=[[1,0]])
vectorx = json.loads(vectorx)
st.write(type(vectorx))
M1 = Matrix(writtenStuff)
# matrix1x = np.array(vector1x).astype(np.float64)
# init_printing()
# A = Matrix(vectorx)
p=M1.charpoly().as_expr()
p = factor(p)
st.write(p)




st.header('Orthonormal Basis Calculator')
vector1 = st.text_input("Please enter the matrix 1", value=[[1],[1],[1],[1]])
vector2 = st.text_input("Please enter the matrix 2", value=[[1],[-1],[1],[0]])
vector3 = st.text_input("Please enter the matrix 3", value=[[1], [1], [-1], [-1]])
vector4 = st.text_input("Please enter the matrix 4", value=[[1],[2],[0],[1]])

vector1 = json.loads(vector1)
vector2 = json.loads(vector2)
vector3 = json.loads(vector3)
vector4 = json.loads(vector4)
matrix1 = np.array(vector1).astype(np.float64)
matrix2 = np.array(vector2).astype(np.float64)
matrix3 = np.array(vector3).astype(np.float64)
matrix4 = np.array(vector4).astype(np.float64)




st.write("V1 = ",matrix1)
matrixDotProduct0 = np.dot(matrix1.T,matrix1)

st.write("V1.T * V1 = ", matrixDotProduct0)


# MATRIX V2
matrix1T = np.array(transpose(matrix1))

def solveMe(v1,u1):
    v1T = np.array(transpose(v1)).astype(np.float64)
    matrixDotProduct1 = np.dot(v1T,v1)
    matrixDotProductTop = np.dot(transpose(v1),u1)
    fractionMain = matrixDotProductTop / matrixDotProduct1
    return fractionMain

def solveMeFinalAnswer(fraction,matrix):
    return fraction*matrix



matrixDotProduct1 = np.dot(matrix1T,matrix1)
matrixDotProductTop = np.dot(transpose(matrix1),matrix2)
st.write("V1.T * V1 = ", matrixDotProduct1)
st.write("Top Fractions = ",matrixDotProductTop)
st.write("Bottom Fraction/Matrix", matrixDotProduct1)

# v2 = (matrix2 - (matrix1.T * matrix1)*matrix2*(np.linalg.inv(matrix1.T*matrix1)*matrix1))
# st.write(v2)
st.write("V1 = ",matrix2)

fractionMain = matrixDotProductTop / matrixDotProduct1
st.header("Fraction * V1 ")
st.write(fractionMain*matrix1)
st.header("V2 = ")
v2 = matrix2 - (fractionMain*matrix1)
st.write(v2)



###### MATRIX V3 ######

st.header("V3 here")
firstFraction  = solveMe(matrix1,matrix3)
firstMatrix = solveMeFinalAnswer(firstFraction,matrix1)
st.write("First fraction", firstFraction)
st.write("First Matrix is ",firstMatrix)
secondFraction = solveMe(v2,matrix3)
secondMatrix = solveMeFinalAnswer(secondFraction,v2)
st.write("Second fraction", secondFraction)
st.write("Second Matrix is ",secondMatrix)
v3 = matrix3 - firstMatrix-secondMatrix
st.write("The answer is " , v3)
# v2dotproducted = np.dot(transpose(v2),v2)
# v3 = matrix3 - ((np.dot(matrix3,transpose(matrix1))/matrixDotProduct1 )* matrix1 ) - ((np.dot(transpose(v2),matrix3)/v2dotproducted)*v2)
# st.header("V3 = ")
# st.write(v3)

#### V4###

st.header("V4 here")
firstFraction  = solveMe(matrix1,matrix4)
firstMatrix = solveMeFinalAnswer(firstFraction,matrix1)
st.write("First fraction", firstFraction)
st.write("First Matrix is ",firstMatrix)
secondFraction = solveMe(v2,matrix4)
secondMatrix = solveMeFinalAnswer(secondFraction,v2)
st.write("Second fraction", secondFraction)
st.write("Second Matrix is ",secondMatrix)
thirdFraction = solveMe(v3,matrix4)
thirdMatrix = solveMeFinalAnswer(thirdFraction,v3)
st.write("Third fraction", thirdFraction)
st.write("Third Matrix is ",thirdMatrix)
v4 = matrix4 - firstMatrix-secondMatrix - thirdMatrix
st.write("The answer is " , v4)

# matrix2T = np.array(transpose(matrix1)).astype(np.float64)
# matrixDotProduct1 = np.dot(matrix1T,matrix1)
# matrixDotProductTop = np.dot(transpose(matrix1),matrix2)

# st.subheader("Projection Matrix P is")
# projMat = np.dot(aMatrix,answer)
# st.write(projMat)


