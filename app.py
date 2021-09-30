import streamlit as st

Vt = 0.025
def eqparallelDivision(r1,r2):
    newNumber = (1/r1)+(1/r2)
    return newNumber**-1

# Create a page dropdown 
page = st.selectbox("Choose your page", ["NPN BJT", "PNP BJT", "Page 3"]) 
if page == "NPN BJT":
    st.header("Hello there welcome to 2027")


    st.markdown("""

    # NPN BJT \n
    The formula is as follows\n # For NPN BJT, collector i<sub>c</sub> current moves into the collector and through the base.

    The figure below is how it looks like in a figure.

    The conditions which have to be true for a forward active mode are as follows: 

    V<sub>BE</sub>>0 - emitter base junction/ forward bias 
    V<sub>BC</sub>>0 - base collector junction/ reverse bias 
    ![](https://www.electronics-tutorials.ws/wp-content/uploads/2013/09/tran5.gif?fit=499%2C248)


    """,unsafe_allow_html = True)

    npnVBE = st.number_input("""Enter V_be""", value= 0.0)
    npnVBC = st.number_input("""Enter V_bc""", value= 0.0)

    def trueornote(npnvbe, npnvbc):
        if(npnvbe > 0 and npnvbc<0):
            return "It is forward active"
        else:
            return "It is not forward active"
    st.write(trueornote(npnVBE,npnVBC))

    st.markdown("""If the question asks you to get the value of the current gain, early voltage and saturation current of a BJT, please fill the items up as follows:


![](https://i.ibb.co/92GBsf3/Screenshot-2021-09-29-at-11-47-21-PM.png)
![](https://i.ibb.co/pzTBnLy/Screenshot-2021-09-29-at-11-59-11-PM.png)
    """, unsafe_allow_html=True)

    

    # smallchangeinvbe = st.number_input("""Enter small change in Vbe""", value= 0.0)
    st.write("Remeber to change the units into the respective ones")
    def forwardActiveModeCalculator():
        gmnpn = st.number_input("""Enter small change in Vbe/gm""", value= 0.0)
        ic = Vt*gmnpn
        ib = st.number_input("""Enter ib""", value= 1.0)
        beta = ic/ib
        return "Answer is "+ str(beta)
    st.write(forwardActiveModeCalculator())
    def earlyAcalculator():
        r0 = st.number_input("""Enter small change in Vce/r0""", value= 1.0,step=1e-6,
    format="%.5f")
        ic = st.number_input("""Enter ic(from above)""", value= 1.0,step=1e-6,
    format="%.5f")
        answer = ic/r0
        return answer
    answerReturned = earlyAcalculator()
    def isAnswerValid(a):
        if(a<90):
            return "Please try to redo the question"
        else:
            return "The answer seems to be correct"
    st.write("Answer is "+ str(answerReturned))
    st.write(isAnswerValid(answerReturned))
    st.write("The ending to this is Point P is not within the forward active region, but at the verge of saturation, hence the small signal ac ic and vce will be distorted, and the amplifier will no longer work properly.")
    st.write("Lol")

elif page == "PNP BJT":
    st.write("Hello there")
    st.markdown("""
![](https://i.stack.imgur.com/k29On.png)


# Basically what you do for PNP is the same as """)
    st.write("Voltage Divider Principlé")
    rOne = st.number_input("""Enter r1(from above)""", value= 1.0,step=1e-6,
    format="%.5f")
    st.write("Test")
    rTwo = st.number_input("""Enter r2(from above)""", value= 1.0,step=1e-6,
    format="%.5f")
    vDD = st.number_input("""Enter vDR""", value= 1.0,step=1e-6,
    format="%.5f")
    rE = st.number_input("""Enter re""", value= 1.0,step=1e-6,
    format="%.5f")
    rC = st.number_input("""Enter rC""", value= 1.0,step=1e-6,
    format="%.5f")
    st.write("Hello wrold")
    def voltageDividerPrinciple(vDD,r1,r2,rE,rC):
        st.write("Assuming fair split of currents")
        voltageFounded = eqparallelDivision(r1,r2) * vDD
        st.write(voltageFounded)
        vb = st.number_input("""Enter vb""", value= 1.0,step=1e-6,
    format="%.5f")
        return voltageFounded     
    voltageDividerPrinciple(vDD,rOne,rTwo,rE,rC)
        


elif page == "Page 3":
    st.write("Hello there")


### ASSETS ARE ALL CONSTANTS


