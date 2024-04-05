# Import necessary libraries
import streamlit as st
import sqlite3
from sqlite3 import Error
import hashlib
from email_varification import send_email
from crewai import Crew
from Tasks import ProjectTasks
from Agents import ProjectAgents
from dotenv import load_dotenv
load_dotenv()


# Function to create SQL connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        st.error(e)
    return conn


# Function to create a new user in the database
def create_user(conn, user):
    sql = ''' INSERT INTO users(full_name,category,interested_field,email,password)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid


# Function to check user login
def check_user_login(conn, email, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password,))
    records = cur.fetchall()
    return len(records) > 0


# Hash password for secure storage
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Define the homepage content
def homepage():
    tasks = ProjectTasks()
    agent = ProjectAgents()

    st.title("Hi I am your project assistant LLM")
    st.write("Congratulations, you're logged in.")
    project_scope=st.text_area("Write project scope:")
    project_objective=st.text_area("Write project objective:")
    available_resources=st.multiselect("Choose a resources", ["Project Manager", "Project Researcher", "Document Writer", "Front-end Developer", "Back-end Developer", "Data Scientist", "Project Tester"])
    technology_stack=st.multiselect("Choose a technology stacks", ["Python Flask, SQLite3", "Python Data Science", "HTML, CSS, JavaScript", "Python unittest"])

    if st.button("Crew KickOff!!"):
        ProjectManager = agent.ProjectManager()
        ProjectResearcher = agent.ProjectResearcher()
        FrontEndDeveloper = agent.FrontEndDeveloper()
        BackEndDeveloper = agent.BackEndDeveloper()
        DataScientest = agent.DataScientist()
        SoftwareTester = agent.SoftwareTester()
        DocumentWriter = agent.DocumentWriter()

        Planning = tasks.Planning(ProjectManager, project_scope, project_objective, available_resources, technology_stack)
        Research = tasks.Research(ProjectResearcher, project_scope, project_objective, available_resources, technology_stack)
        Coding = tasks.Coding(FrontEndDeveloper, project_scope, project_objective, available_resources, technology_stack)
        Testing = tasks.Testing(SoftwareTester, project_scope, technology_stack, available_resources)

        Planning.context = [Research, Coding, Testing]
        Coding.context = [Research, Testing]

        crew = Crew(
            agent=[
                ProjectManager,
                ProjectResearcher,
                FrontEndDeveloper,
                BackEndDeveloper,
                DataScientest,
                SoftwareTester,
                DocumentWriter
            ],
            tasks=[
                Planning,
                Research,
                Coding,
                Testing
            ]
        )
        result = crew.kickoff()

        st.markdown(result)

    # Logout Button in Sidebar
    if st.sidebar.button('Logout'):
        st.session_state['logged_in'] = False
        st.experimental_rerun()  # This will rerun the app and reflect the updated login state

# Main function for the app
def main():
    # Connect to the SQLite database
    conn = create_connection("your_database.db")

    # Ensure the users table exists
    with conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            category TEXT NOT NULL,
            interested_field TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        """)

    # Using session state to manage login status
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # Navigation
    if st.session_state['logged_in']:
        homepage()
    else:
        page = st.sidebar.selectbox("Choose a page", ["Login", "Register"])
        if page == "Register":
            st.title("Register Page")
            full_name = st.text_input("Full Name")
            category = st.selectbox("Are you a student or working professional?", ['Student', 'Working Professional'])
            interested_field = st.text_input("Your Interested Field")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Register"):
                hashed_password = hash_password(password)
                user = (full_name, category, interested_field, email, hashed_password)
                create_user(conn, user)
                st.success("You have successfully registered!")
                # Send welcome email
                subject = "Welcome to the Personalized Teaching Mentor App!"
                body = f"Dear {full_name},\n\nWelcome aboard! As a {category}, your interest in {interested_field} is about to take a new leap. Let's make the learning journey exciting together.\n\nBest,\nThe Team"
                send_email(email, subject, body)
        elif page == "Login":
            st.title("Login Page")
            login_email = st.text_input("Email", key="login_email")
            login_password = st.text_input("Password", type="password", key="login_password")
            if st.button("Login"):
                hashed_password = hash_password(login_password)
                if check_user_login(conn, login_email, hashed_password):
                    st.session_state['logged_in'] = True
                    st.experimental_rerun()
                else:
                    st.error("Invalid email or password.")


if __name__ == "__main__":
    main()