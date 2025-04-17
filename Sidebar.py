

import time
import streamlit as st
from streamlit_option_menu import option_menu

class Sidebar():
    def __init__(self, title, components, debug=False):
        self.title = title
        self.components = components

        self.debug = debug

    def render(self):
        # Create a sidebar with a title
        
        with st.sidebar:
            with st.container(border=True):
                col1, col2 = st.columns([0.7, 0.3], vertical_alignment="center")
                col1.title(self.title)
                col2.title(":balloon")

            # selected = option_menu("Main Menu", ["Home", 'Settings'], 
            #     icons=['house', 'gear'], menu_icon="cast", default_index=1)
            # selected

            # Add Space:
            st.container(height=250, border=False)

            # Add a checkbox to toggle debug mode
            debug_mode = st.sidebar.checkbox("Enable Debug Mode", value=self.debug)


if __name__ == "__main__":
    def main():
        st.title("Sidebar Example")

        sidebar = Sidebar(
            title="My Home",
            components=["Component 1", "Component 2", "Component 3"],
            debug=True
        )
        sidebar.render()

        # st.title("Sidebar")


        # st.container(height=250, border=False)
        # add_selectbox = st.sidebar.selectbox(
        #     "How would you like to be contacted?",
        #     ("Email", "Home phone", "Mobile phone")
        # )

        # # Using "with" notation
        # with st.sidebar:
        #     add_radio = st.radio(
        #         "Choose a shipping method",
        #         ("Standard (5-15 days)", "Express (2-5 days)")
        #     )


        # debug_mode = st.sidebar.checkbox("Enable Debug Mode", value=False)
    
    main()