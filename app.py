import streamlit as st
import random

# Initialize session state for scores
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'ai_score' not in st.session_state:
    st.session_state.ai_score = 0
if 'ties' not in st.session_state:
    st.session_state.ties = 0
st.title("🎮 Rock-Paper-Scissors Game with AI")

st.write("### Make your choice:")

# User makes a choice
user_choice = st.selectbox("Choose Rock, Paper, or Scissors:", ("Rock", "Paper", "Scissors"))

# Play button
if st.button("Play"):
    # AI makes a random choice
    ai_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    st.write(f"**You chose:** {user_choice}")
    st.write(f"**AI chose:** {ai_choice}")
    
    # Determine the winner
    if user_choice == ai_choice:
        result = "It's a tie!"
        st.session_state.ties += 1
    elif (user_choice == "Rock" and ai_choice == "Scissors") or \
         (user_choice == "Paper" and ai_choice == "Rock") or \
         (user_choice == "Scissors" and ai_choice == "Paper"):
        result = "🎉 You win!"
        st.session_state.user_score += 1
    else:
        result = "🤖 AI wins!"
        st.session_state.ai_score += 1
    
    st.write(f"### **Result:** {result}")

    # Display scores
    st.write("---")
    st.write("### **Scores**")
    col1, col2, col3 = st.columns(3)
    col1.metric("You", st.session_state.user_score)
    col2.metric("AI", st.session_state.ai_score)
    col3.metric("Ties", st.session_state.ties)

# Reset scores button
if st.button("Reset Scores"):
    st.session_state.user_score = 0
    st.session_state.ai_score = 0
    st.session_state.ties = 0
    st.success("Scores have been reset!")
    

