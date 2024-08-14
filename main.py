import streamlit as st
from supervisor import SupervisorAgent

def main():
    st.title("SummarizeFlow")

    folder_path = st.text_input("Enter the folder path to process:")
    start_processing = st.button("Start Processing")

    if start_processing and folder_path:
        supervisor = SupervisorAgent(folder_path)
        output = supervisor.run()

        st.write("Processing Complete!")
        st.json(output)
        with open("output.json", "w") as f:
            f.write(output)

if __name__ == "__main__":
    main()
