import streamlit as st
import math
import scipy
st.title("Weight average of Molecule")
def newStinput(texthere):
    text = st.text_input(texthere, value=1)
    text = float(text)
    return text
'''
<math><msub is="true"><mrow is="true"><mi is="true">M</mi></mrow><mrow is="true"><mi is="true">w</mi></mrow></msub><mrow is="true"><mo is="true">=</mo></mrow><mfrac is="true"><mrow is="true"><munder is="true"><mo is="true">∑</mo><mrow is="true"><mi is="true">i</mi></mrow></munder><mrow is="true"><msub is="true"><mrow is="true"><mi is="true">N</mi></mrow><mrow is="true"><mi is="true">i</mi></mrow></msub><msubsup is="true"><mrow is="true"><mi is="true">M</mi></mrow><mrow is="true"><mi is="true">i</mi></mrow><mrow is="true"><mn is="true">2</mn></mrow></msubsup></mrow></mrow><mrow is="true"><munder is="true"><mo is="true">∑</mo><mrow is="true"><mi is="true">i</mi></mrow></munder><mrow is="true"><msub is="true"><mrow is="true"><mi is="true">N</mi></mrow><mrow is="true"><mi is="true">i</mi></mrow></msub><msub is="true"><mrow is="true"><mi is="true">M</mi></mrow><mrow is="true"><mi is="true">i</mi></mrow></msub></mrow></mrow></mfrac></math>


̅M̅ = Σ
Formula ΣfiMi/Σfi 
'''
# $\frac{ΣfiMi}{Σfi}$
# Where Mi = Mean molecular weight of each molecular range selected
# fi = fractio weight of the material having molecular weights of a selected molecular range
# ### Where f replaces N, so its 
# '''

sum_top = st.number_input("Enter the ΣfiMi", value=1)
sum_bot = st.number_input("Enter the Σfi",value=1)
answer1 = sum_top/sum_bot

st.write("The answer is ", answer1 , "g/mol")


st.subheader("Number average(Mn̅) and Weight average(Mw̅) calculations")

number_average_M = st.number_input("Enter the M̅n/ m̅ where m̅ is the mer molecular weight",value=1)
number_average_m = st.number_input("Enter the m̅",value=1)
number_average_answer = number_average_M/number_average_m

st.write("The answer is ", number_average_answer, 'gram/mol')



st.header("Formula for yield strength")

def NerstEquation(voltage,numberofelectrons,numberofmoles):
    E = voltage + (0.0592/numberofelectrons*math.log10(numberofmoles))
    return E
def getConcentrationNerst(voltage,numberofelectrons,E):
    return 10**((E - voltage)/(0.0592/numberofelectrons))

def enterVoltagesPlease(moletext):
    numberOxidised = st.text_input(moletext,value=1)
    numberOxidised = float(numberOxidised)
    numberOxidisedVoltage = st.text_input("Enter the half cell EMF for the above1",value=1)
    numberOxidisedVoltage = float(numberOxidisedVoltage)
    electronsUsedO = st.text_input("Write the number of electrons used1",value=1)
    electronsUsedO = float(electronsUsedO)
    ans1 = NerstEquation(numberOxidisedVoltage, electronsUsedO, numberOxidised)
    zach = st.radio("Is the reaction reversed?","YN")
    if zach == "Y":
        ans1 = -ans1
        E = newStinput("Write E1")
        E = -E
        st.write("If you are finding the number of moles of substance",getConcentrationNerst(numberOxidisedVoltage, electronsUsedO, E))
    if zach =="N":
        ans1 = ans1
        E = newStinput("Write E3")
        st.write("If you are finding the number of moles of substance",getConcentrationNerst(numberOxidisedVoltage, electronsUsedO, E))
    return ans1

st.header("Nerst equation")
numberOxidised = st.text_input("Enter number of moles of first compound, if it is more negative it oxidises",value=1)
numberOxidised = float(numberOxidised)
numberOxidisedVoltage = st.text_input("Enter the half cell EMF for the above",value=1)
numberOxidisedVoltage = float(numberOxidisedVoltage)
electronsUsedO = st.text_input("Write the number of electrons used",value=1)
electronsUsedO = float(electronsUsedO)
V1 = NerstEquation(numberOxidisedVoltage, electronsUsedO, numberOxidised)
zach = st.radio("Is the reaction reversed?ay","YN")
if zach == "Y":
        V1 = -V1
        E = newStinput("Write E")
        E = -E
        st.write("If you are finding the number of moles of substance",getConcentrationNerst(numberOxidisedVoltage, electronsUsedO, E))
if zach =="N":
        V1 = V1
        E = newStinput("Write E3")
        st.write("If you are finding the number of moles of substance",getConcentrationNerst(numberOxidisedVoltage, electronsUsedO, E))
st.write("The answer is ", V1)
V2 = enterVoltagesPlease("Enter the number of moles of the other substance please(reduced")
st.write(V2)
st.write("Total EMF is", V2+V1)

st.header("Corrosion Rates")


F = 96485.33212
'''

W = weightOfMetalCorroded

I = Current Flow

i = current density(A/cm2)

M = atomic mass of metal

n = number of electrons produced/consumed

F = Faraday;s constant

A = area(cm2)

t = time(s)


'''
def CorrosionRates(I,t,M,n):
    W = I*t*M/n*F
    return st.write("The coorosion rate is",W)
def CorrosionRates2(i,I,t,M,n):
    W = i*A*t*M/n*F
    return st.write("The coorosion rate is",W)

darth = st.radio("Is it in current density or current(N)?","YN")
if darth == "N":
    A = st.text_input("A, current flow", value=1)
    A = float(A)
    t = st.text_input("t, time", value=1)
    t= float(t)
    M = newStinput("Atomic mass of metal g/mol")

    n = newStinput("Number of atoms/produced or consumed")
    CorrosionRates(A, t, M, n)
if darth == "Y":
    i = newStinput("Current density,i ")
    A = st.text_input("A, area,cm2", value=1)
    A = float(A)
    t = st.text_input("t, time", value=1)
    t= float(t)
    M = newStinput("Atomic mass of metal g/mol")

    n = newStinput("Number of atoms/produced or consumed")
    CorrosionRates2(i,A, t, M, n)


st.header("Quantum Mechanics")

st.header("Conductivity and resistivity")
'''
J(current density)= Conductivity*Electric field applied

I = JA

'''

I = newStinput("Enter teh current that is being used, I")
J = newStinput("current density,J")
A1 = newStinput("Cross sectional Area,A")
sigma = newStinput("Conductivity σ [ohm/cm-1]")
ew = newStinput("Electric field applied V/cm")
Volt = newStinput("Voltage applied V")
d = newStinput("distance over which the voltage is applied/cm")
resistivity = newStinput("ρ resistivty [ohm cm]")
number = newStinput("(conduction)electron concetration cm-3")
p = newStinput("(valance hole concentration cm^-3)")
qe = -1.602*10**-19
st.write("qe/charge carried by one electron or hole [C]", qe)
miuh = newStinput("Hole mobility")
miue = newStinput("electron mobility unit is cm^2/Vs")
Resistance = newStinput("resistance")



sigma1 = 1/resistivity
st.write("The conductivity is, please put it into sigma ", sigma1)

st.write('sigma can also be')
sigma2 = qe*number*miue + qe*p*miuh
st.write(sigma2, "if you use the other formula")

try:
    J = sigma*ew
    st.write("J is", J)
except:
    J = sigma*Volt/d
    st.write("J is",J)

st.write("Resistance is such that")

Resistance = resistivity*d/A1
st.write("Resistance is", Resistance)