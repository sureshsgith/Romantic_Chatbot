import streamlit as st
import openai

# Initialize OpenAI GPT-3.5
openai.api_key = "sk-POyh72"+"mWbhIMJ8Q"+"ATu63T3BlbkF"+"JYyk2492ZR"+"qgPSEuG4FaK"

def get_bot_response(prompt):
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()

def main():
    # Set page configuration
    st.set_page_config(page_title="Romantic Chatbot", page_icon="❤️")

    # Custom styles (for backgrounds and overall look)
    st.markdown("""
    <style>
        body {
            color: #ff8c8c;
            background-color: #ffe4e1;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Romantic Chatbot")
    st.write("Embark on a romantic conversation tailored just for you.")
    
    # Gender and Mood Selection
    gender = st.sidebar.radio("Your Gender:", ["Male", "Female"])
    mood = st.sidebar.radio("Choose the Chatbot's Mood:", ["Flirty", "Shy", "Sweet", "Passionate"])

    # Dynamic Backgrounds logic remains unchanged ...

    # Check if 'messages' exists in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Type your message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Crafting the prompt based on mood
        full_prompt = f"A romantic conversation where the chatbot is in a {mood} mood. User: {prompt} Chatbot:"
        ai_response = get_bot_response(full_prompt)

        # Display bot's response
        with st.chat_message("assistant"):
            st.write(ai_response)

        st.session_state.messages.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    main()
