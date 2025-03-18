import os

def create_env_file():
    """
    Creates a .env file with placeholders for TOKEN and OWNER_ID.
    """
    env_content = """
TOKEN=
OWNER_ID=
"""
    with open('.env', 'w') as env_file:
        env_file.write(env_content)
    print("✅ .env file created successfully.")

def create_user_memories_folder():
    """
    Creates a folder called user_memories if it doesn't already exist.
    """
    if not os.path.exists('user_memories'):
        os.makedirs('user_memories')
        print("✅ user_memories folder created successfully.")
    else:
        print("✅ user_memories folder already exists.")


def main():
    create_env_file()
    create_user_memories_folder()
    print("Setup complete!")


if __name__ == "__main__":
    main()
