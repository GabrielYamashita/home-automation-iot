
import streamlit as st
from datetime import datetime


class SliderWidget:
    def __init__(self, name, min_value, max_value, default_value, session_key, debug=True):
        self.name = name
        self.label = "Select a Value"

        self.min_value = min_value
        self.max_value = max_value
        self.default_value = default_value

        self.session_key = session_key  # Unique key for the slider

        self.debug = debug

    def render(self):
        # Create and render the slider widget; value is automatically stored by the unique key
        st.markdown(f"### {self.name}")
        slider_value = st.slider(
            self.label, 
            min_value=self.min_value, 
            max_value=self.max_value, 
            value=self.default_value, 
            key=self.session_key,
            format="%d%%"
        )

        # st.write("Slider Value:", slider_value)  
        
        # Print the debug information if debug mode is enabled
        if self.debug:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"[DEBUG] ({current_time}) Slider ({self.session_key}) value: {slider_value}")

        return slider_value



if __name__ == '__main__':
    debug_mode = True
    slider = SliderWidget(
        name="Hall Lamp",
        min_value=0, max_value=100, default_value=75, 
        session_key=f"slider_1", 
        debug=debug_mode
    )

    def main():
        st.title("Slider Button Previw")

        
        # Create instances of the ToggleButton and SliderComponent with the debug flag
        
        # Render the component
        sliderValue = slider.render()  

    main()
