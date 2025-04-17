
import streamlit as st

from Button import ButtonWidget
from Slider import SliderWidget


def main():
    st.title("Home Automation Control Panel")
    
    debug_mode = st.sidebar.checkbox("Enable Debug Mode", value=False)

    toggle = ButtonWidget(
        label="Click to Toggle", 
        state_key="my_toggle_state", 
        button_key="my_toggle_button", 
        debug=debug_mode
    )

    slider = SliderWidget(
        label="Select a Value", 
        min_value=0, max_value=100, default_value=75, 
        session_key="slider1", 
        debug=debug_mode
    )


    with st.container(border=True):
        col1, col2 = st.columns([0.7, 0.3])

        with col1:
            buttonValue = toggle.render()

        with col2:
            st.write("Toggle is", "ON" if buttonValue else "OFF")

    with st.container(border=True):
        col1, col2 = st.columns([0.7, 0.3])

        with col1:
            sliderValue = slider.render() 

        with col2:
            st.write("Slider Value:", sliderValue) 





if __name__ == "__main__":
    main()