import sys
from github_activity import fetch_user_activity, display_activity

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <username>")
        print("Example: python main.py kamranahmedse")
        sys.exit(1)
    
    username = sys.argv[1]
    print(f"Fetching recent activity for user: {username}...")
    
    events = fetch_user_activity(username)
    display_activity(events)

if __name__ == "__main__":
    main()