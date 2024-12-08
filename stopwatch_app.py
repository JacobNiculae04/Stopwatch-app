import streamlit as st  # Import the Streamlit library for creating the web app
import time             # Import the time library to track elapsed time

# Set up the Streamlit app with a title
st.title("🕒 Stopwatch Timer App")

# Initialize state variables in Streamlit's session state to maintain state across interactions
if "start_time" not in st.session_state:
    st.session_state.start_time = None  # Stores the starting time when the stopwatch is started
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0   # Stores the total elapsed time in seconds
if "running" not in st.session_state:
    st.session_state.running = False    # Indicates if the stopwatch is currently running

# Function to start the stopwatch
def start_stopwatch():
    if not st.session_state.running:
        # Record the current time minus any previously elapsed time (to allow resuming)
        st.session_state.start_time = time.time() - st.session_state.elapsed_time
        st.session_state.running = True  # Set the stopwatch to running state

# Function to stop the stopwatch
def stop_stopwatch():
    if st.session_state.running:
        # Calculate and store the elapsed time up to this point
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        st.session_state.running = False  # Set the stopwatch to stopped state

# Function to reset the stopwatch
def reset_stopwatch():
    st.session_state.start_time = None      # Clear the start time
    st.session_state.elapsed_time = 0       # Reset the elapsed time to zero
    st.session_state.running = False        # Set the stopwatch to stopped state

# Create three columns for Start, Stop, and Reset buttons
col1, col2, col3 = st.columns(3)

# Place the Start button in the first column
with col1:
    if st.button("Start"):
        start_stopwatch()

# Place the Stop button in the second column
with col2:
    if st.button("Stop"):
        stop_stopwatch()

# Place the Reset button in the third column
with col3:
    if st.button("Reset"):
        reset_stopwatch()

# Placeholder to display the elapsed time
timer_placeholder = st.empty()  # Create an empty placeholder for the timer display

# Update the elapsed time if the stopwatch is currently running
while st.session_state.running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time  # Calculate elapsed time
    timer_placeholder.write(f"### Elapsed Time: {st.session_state.elapsed_time:.2f} seconds")  # Update display
    time.sleep(0.1)  # Sleep for a short duration to update the timer every 0.1 seconds

# Display the formatted elapsed time with two decimal places when the stopwatch is stopped
timer_placeholder.write(f"### Elapsed Time: {st.session_state.elapsed_time:.2f} seconds")

