import streamlit as st

# Define the questions and answers based on the uploaded document
questions = {
    1: {"question": "What is the value that appears most frequently in a data set?", "answer": "mode"},
    2: {"question": "What is the distance around a circle called?", "answer": "circumference"},
    3: {"question": "Who discovered Zero?", "answer": "aryabhatta"},
    4: {"question": "What is the binary value of the decimal number '15'?", "answer": "1111"},
    5: {"question": "What is the extension of a Python file?", "answer": ".py"},
    6: {"question": "What is the study of data collection, analysis, interpretation, and presentation called?", "answer": "statistics"},
    7: {"question": "What is the result of an experiment called?", "answer": "outcome"},
    8: {"question": "What do you call the distance of a number from zero on a number line?", "answer": "absolute"},
    9: {"question": "What is the name of the method used to find the area under a curve in calculus?", "answer": "integration"},
    10: {"question": "A line intersecting a circle in two points is called a?", "answer": "secant"},
    11: {"question": "What is the measure of data spread called that calculates the average squared deviation from the mean?", "answer": "variance"},
    12: {"question": "What is the term for a graph showing the frequency distribution of a dataset?", "answer": "histogram"},
    13: {"question": "Which operator is used in SQL to select values within a range?", "answer": "between"},
    14: {"question": "Which protocol is used to transfer files between devices over a TCP/IP connection?", "answer": "file transfer protocol"},
    15: {"question": "If a database table has duplicate rows, which SQL clause can be used to remove duplicates in the result set?", "answer": "distinct"},
    16: {"question": "“I am the keeper of your digital treasures, Photos, music, and files in great measures. Portable or fixed, I’m always in use, Without me, your data you’d lose. What am I?”", "answer": "storage device"},
}

# Session state for tracking question progress
if 'current_question' not in st.session_state:
    st.session_state.current_question = 1  # Start with question 1

# Function to display a question and get an answer
def display_question(q_num):
    st.write(f"Question {q_num}: {questions[q_num]['question']}")
    
    # Display answer input field
    answer = st.text_input(f"Answer for Question {q_num}:", key=f"input_{q_num}")
    
    # Submit button
    submitted = st.button("Submit Answer", key=f"submit_{q_num}")
    
    # Check the answer either when "Enter" is pressed or "Submit" button is clicked
    if answer and (submitted or st.session_state.get(f"submitted_{q_num}", False)):
        if answer.lower() == questions[q_num]['answer']:
            st.success("Correct answer! Proceeding to the next question.")
            st.session_state.current_question += 1  # Automatically move to the next question
            st.session_state[f"submitted_{q_num}"] = False  # Reset submitted state for the next question
        else:
            st.error("Incorrect answer. Try again!")
        # Mark that the submit button has been pressed to handle "Enter" presses
        st.session_state[f"submitted_{q_num}"] = True

# Display each question sequentially based on the current question number
st.title("Treasure Hunt Event")

if st.session_state.current_question <= len(questions):
    display_question(st.session_state.current_question)
else:
    st.balloons()  # Show a celebration effect
    st.success("Congratulations! You've answered all questions correctly.")
    st.write("Now, go in search of your treasure!")
