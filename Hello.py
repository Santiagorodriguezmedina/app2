import streamlit as st
import pandas as pd

dataset = pd.read_csv("data.csv")

x = dataset.iloc[:,0]
y = dataset.iloc[:,1]
p0 = "pp.png"



# Streamlit app
def main():
    st.sidebar.title("VRS QBR")
    selected_slide = st.sidebar.selectbox("Select Slide:", list(zip(x, y)), format_func=lambda item: item[0])
    if selected_slide:
        slide_name, link = selected_slide
        st.markdown(f"[{slide_name}]({link})")

        for link in range(0,6):
            if slide_name == f"{x[link]}":
                st.image(f"p{link}", use_column_width=True)


if __name__ == "__main__":
    main()
    