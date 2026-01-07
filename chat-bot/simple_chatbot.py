import random
import streamlit as st  # We need to import the Streamlit library

# --- BACKEND LOGIC (The Brain) ---
# This function is exactly the same as before! 
# It doesn't care if the input comes from a terminal or a website.
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    confused_responses = [
        "I'm not sure I understand.",
        "Could you say that in a different way?",
        "That's interesting, tell me more!",
        "I'm still learning English, can you simplify that?"
    ]

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_input:
        return "I am just a computer program, but my code is running perfectly!"
    elif "name" in user_input:
        return "My name is PyBot. Nice to meet you."
    elif "weather" in user_input:
        return "I can't see outside, but I hope it's sunny where you are!"
    elif "python" in user_input:
        return "Python is a great language! It's very beginner-friendly."
    elif "bye" in user_input or "exit" in user_input:
        return "goodbye"
    else:
        return random.choice(confused_responses)

# --- FRONTEND UI (The Face) ---

# 1. Set the title of the web page
st.title("🤖 PyBot: My First AI Assistant")
st.write("Welcome! Type a message below to chat with PyBot.")

# 2. SESSION STATE (The Memory)
# Unlike a 'while' loop in a terminal, web pages "forget" everything 
# every time you click a button. We use 'session_state' to fix that.
if "messages" not in st.session_state:
    # If this is the first time loading the page, create an empty list for chat history
    st.session_state.messages = []

# 3. DISPLAY CHAT HISTORY
# We loop through the 'messages' list and draw them on the screen.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. HANDLE NEW INPUT
# st.chat_input creates the text box at the bottom.
if prompt := st.chat_input("What is up?"):
    
    # A. Display user message immediately
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # B. Save user message to memory (session_state)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # C. Get the bot's response using our function
    response = get_bot_response(prompt)
    
    # D. Display bot response
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # E. Save bot response to memory
    st.session_state.messages.append({"role": "assistant", "content": response})