
import streamlit as st

class SliderWidget:
    def __init__(self, label, min_value, max_value, default_value, session_key, debug=False):
        self.label = label

        self.min_value = min_value
        self.max_value = max_value
        self.default_value = default_value

        self.session_key = session_key

        self.debug = debug

    def render(self):
        # Create and render the slider widget; value is automatically stored by the unique key
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
            print(f"[DEBUG] Slider value: {slider_value}")

        return slider_value



if __name__ == '__main__':
    def main():
        st.title("Slider Button Previw")

        debug_mode = True
        
        # Create instances of the ToggleButton and SliderComponent with the debug flag
        slider = SliderWidget(
            label="Select a Value", 
            min_value=0, max_value=100, default_value=75, 
            session_key="slider1", 
            debug=debug_mode
        )
        
        # Render the component
        sliderValue = slider.render()  
    
    main()
