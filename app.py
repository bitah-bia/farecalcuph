import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
            page_title='Fare Calculator PH',
            page_icon="🚌",
            layout="wide",
            initial_sidebar_state="expanded")
st.title('Welcome to :blue[Fare Calculator PH]!👋')
st.markdown("Our fare calculator website helps you know exactly how much fare to load onto your transit card*, saving you time, money, and hassle. Whether you're planning a trip, commuting, or simply curious about transportation costs from Lucena to Lucban (and vice versa), we've got you covered!")
st.caption("$*$ currently in the Pilot Production Testing phase, as per DOTr")
### st.header('Fare Calculator')

with st.sidebar:
    st.markdown("[![Fare Calcu](https://raw.githubusercontent.com/bitah-bia/farecalcuph/main/LOGO_small.png)](https://www.facebook.com/profile.php?id=100086360007534)")
    st.header("SLSU-BS Acc")
    st.markdown("x")
    st.header("Lucban Genesis TSMPC")
    st.divider()
    st.subheader(":green[How to use?]")
    st.markdown(
        f"""
        **Step 1.**
        Select your fare type.
        
        **Step 2.**
        Select your starting point and destination. Use the provided route map below as guide.

        **Step 3.**
        Click "Calculate my fare" to instantly determine your fare amount.
        """)
    st.divider()
    st.subheader(":green[About]")
    st.markdown("This fare calculator website is an offshoot of the study, _'Attitude and Intention of Commuters on Electronic Fare Payment Systems in Modernized Jeepneys.'_ It is a user-friendly tool that aims to aid the DOTR in its efforts to revolutionalize public transport in the Philippines by increasing the intention of commuters to use electronic fare payment in LGTSMPC.")
    st.divider()
    st.markdown(
        f"""
        Together, we're forging a future where travel is no longer a source of stress but a gateway to limitless possibilities.

        Embrace the power of our fare calculator website, and let it become your trusted companion on every commute.

        Here's to no more fumbling for loose change or second-guessing fare amounts!

        Happy fare-calculating, and safe travels!
                """)
    st.divider()
    st.info(
    f"""
    Was the calculator helpful?
    Send your feedback to:
    farecalculatorph@gmail.com
    
    _by:_ GBM, SLSU BSA Class of 2023
    """
    )
    

### MAIN PAGE

particulars = ["Grand Central Terminal", "Orchids", "Lucena City Diversion","Lic Manukan", "Boundary Gulang2", "United Church", "School Wakas", "Babuyan/Jesus Miracle Crusade", "By Pass Wakas", "Brgy Nangka/Obispo Hospital", "By Pass Baguio/Luis Palad/Ipilan/P. Paterno st. Tayabas", "Donya Carmen", "Mariposa", "Nawawalang Paraiso", "Dapdap", "Lanzonisan", "May it", "Ayos", "Tiawe", "M-Tanaw", "Batis Aramin", "Sindiko", "Tulay Digitel", "Lucban Terminal"]

st.subheader("Select fare type:")
commuter = st.radio(
        "",
        ('Regular','Student/Senior Citizen/Persons with Disability'),
        horizontal=True
        )

st.subheader("Select your starting point and destination:")
if commuter == 'Regular':
    start_clr, end_clr = st.select_slider("",
                                      options=particulars,
                                      value=("Boundary Gulang2","Tiawe"))
    st.markdown("")
    st.image("https://github.com/bitah-bia/farecalcuph/blob/main/Line%20route%20Genesis-Blue.jpg?raw=true")
    st.subheader('You chose:')
    st.write('', start_clr, "**to**", end_clr)
    
    going_to = particulars.index(end_clr)
###    st.write(going_to)
    leaving_from = particulars.index(start_clr)
###    st.write(leaving_from)
    hm = 'Your fare is '
    cur = ' :blue[pesos] 🙌'


    
    if st.button('Calculate my fare'):
        if (int(going_to)-int(leaving_from)) <= 4:
            fare_orig = 14
###            st.write('Your fare is:',fare_orig)
            st.subheader(hm+str(round(fare_orig))+cur)
        elif (int(going_to)-int(leaving_from)) > 4:
            fare_inc = 14+(((int(going_to)-int(leaving_from))-4)*2.20)
###            st.write(round(fare_inc))
            st.subheader(hm+str(round(fare_inc))+cur)

        else:
            st.write("Please select your destination")
else:
    start_clr2, end_clr2 = st.select_slider("",
                                      options=particulars,
                                      value=("Boundary Gulang2","Tiawe"))
    st.markdown("")
    st.image("https://github.com/bitah-bia/farecalcuph/blob/main/Line%20route%20Genesis-Blue.jpg?raw=true")
    st.subheader('You chose:')
    st.write('', start_clr2, "**to**", end_clr2)

    going_to2 = particulars.index(end_clr2)
###    st.write(going_to2)
    leaving_from2 = particulars.index(start_clr2)
###    st.write(leaving_from2)
    hm2 = 'Your fare is '
    cur2 = ' :blue[pesos] 🙌'

    if st.button('Calculate my fare'):
        if (int(going_to2)-int(leaving_from2)) <= 4:
            fare_orig2 = 11.25
            st.subheader(hm2+str(round(fare_orig2))+cur2)
        elif (int(going_to2)-int(leaving_from2)) > 4:
            fare_inc2 = 11.25+(((int(going_to2)-int(leaving_from2))-4)*1.76)
            st.subheader(hm2+str(round(fare_inc2))+cur2)
        else:
            st.write("Please select your destination")



###st.divider()
###st.image("https://www.hino.com.ph/sites/default/files/styles/photo_gallery_380_x_285/public/lucban_genesis_transport_cooperative_7.jpg?itok=-P3FW507")
###st.subheader('Was the calculator helpful?')


### col1, col2, col3 = st.columns(3)
### col1.metric("Temperature", "70 °F", "1.2 °F")
### col2.metric("Wind", "9 mph", "-8%")
### col3.metric("Humidity", "86%", "4%")

