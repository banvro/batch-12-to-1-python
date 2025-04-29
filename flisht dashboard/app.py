import streamlit as st
from mydb import mydb
import plotly.graph_objects as go

# pip install streamlit

st.sidebar.title("Flights Analysis")

# python -m streamlit run app.py

choice = st.sidebar.selectbox("Menu", ["Select One", "Check Flight", "Analysis"])

db = mydb()

if choice == "Check Flight":
    st.title("Check Flights")

    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox("Source", db.get_cities())
    
    with col2:
        destination = st.selectbox("Destination", db.get_destination_ceties())

    if st.button("Check Flights"):
        
        all_flights = db.get_flights_data(source, destination)

        st.dataframe(all_flights)


elif choice == "Analysis":
    st.title("Flight Analysis")

    air_nme, flt_cunt = db.airlines_flights()

    fig = go.Figure(
       go.Pie(labels = air_nme, values = flt_cunt)
        )
    
    st.header("Airllines Count")
    st.plotly_chart(fig)


    airoport, ct = db.buzest_airport()

    new_fig = go.Figure(
        go.Bar(
            x = airoport,
            y = ct
        )
    )

    st.header("Buizest Airpots")
    st.plotly_chart(new_fig)



else:
    pass