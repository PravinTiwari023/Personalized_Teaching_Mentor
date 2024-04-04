# Import necessary libraries
import streamlit as st
import sqlite3
from sqlite3 import Error
import hashlib

# Create SQL connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        st.error(e)
    return conn

# Create a new user in the database
def create_user(conn, user):
    sql = ''' INSERT INTO users(full_name,category,interested_field,email,password)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

# Check user login
def check_user_login(conn, email, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email,password,))
    records = cur.fetchall()
    return len(records) > 0

# Hash password for secure storage
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Main function for the app
def main():
    # Connect to the SQLite database
    conn = create_connection("your_database.db")

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

    st.title('Welcome to Personalized Teaching Mentor App')

    # Sign-in form
    with st.form("Sign_in"):
        st.write("Sign-in")
        full_name = st.text_input("Full Name")
        category = st.selectbox("Are you a student or working professional?", ['Student', 'Working Professional'])
        interested_field = st.text_input("Your Interested Field")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        sign_in_button = st.form_submit_button("Sign in")

        if sign_in_button:
            user = (full_name, category, interested_field, email, hash_password(password))
            create_user(conn, user)
            st.success("You have successfully signed in!")

    # Login form
    with st.form("Login"):
        st.write("Login")
        login_email = st.text_input("Email", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_password")
        login_button = st.form_submit_button("Login")

        if login_button:
            if check_user_login(conn, login_email, hash_password(login_password)):
                st.success("Login successful!")
            else:
                st.error("Invalid email or password.")

if __name__ == "__main__":
    main()