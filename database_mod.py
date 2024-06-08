import re, os, random, string
import pandas as pd

# Define the path to save CSV file
data_file_add = 'data_base.csv'

# Define the path to save CSV file using os.getcwd() to get the current working directory
data_file_path = os.path.join(os.getcwd(), 'data_base.csv')

# Function to save email data to CSV
def save_email_data(df):
    df.to_csv(data_file_path, index=False)

# Function to load email data from CSV
def load_data_base():
    if os.path.exists(data_file_add):
        return pd.read_csv(data_file_add)
    else:
        return pd.DataFrame(columns=['ch_user_id', 'tel_user_name', 'tel_user_id', 'email_id', 'date'])

# Check if the email is already registered
def is_email(input_str):
    # Regular expression pattern for email validation
    email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    # Using re.match to check if the input string matches the email pattern
    if re.match(email_pattern, input_str):
        return True
    else:
        return False

def gen_uniq_channel_id(existing_ids):
    """
    Generate a unique 10-digit channel ID.
    :param existing_ids: A set of existing channel IDs
    :return: A unique 10-digit channel ID
    """
    while True:
        # Generate a random 10-digit ID
        channel_id = ''.join(random.choices(string.digits, k=10))
        # Check if this ID is unique
        if channel_id not in existing_ids:
            return channel_id