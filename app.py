import streamlit as st

def main():
    st.title('test')
    st.text('test ma più piccolo')

    tizio = st.slider('qualcosa', 0, 100, 0)

    st.write('il numero è', tizio)

if __name__ == "__main__":
    main()