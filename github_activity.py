import requests
from typing import List, Dict, Any

def fetch_user_activity(username: str) -> List[Dict[str, Any]]:
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            print(f"Error: User '{username}' not found.")
            return []
        elif response.status_code == 403:
            print("Error: Rate limit exceeded. Please try again later.")
            return []
        elif response.status_code != 200:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")
            return []
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Network error - {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


from datetime import datetime
import requests
from typing import List, Dict, Any


try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False

def fetch_user_activity(username: str) -> List[Dict[str, Any]]:
   
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            print(f"Error: User '{username}' not found.")
            return []
        elif response.status_code == 403:
            print("Error: Rate limit exceeded. Please try again later.")
            return []
        elif response.status_code != 200:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")
            return []
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Network error - {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


from datetime import datetime
import requests
from typing import List, Dict, Any

# رنگ برای ترمینال
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False


def fetch_user_activity(username: str) -> List[Dict[str, Any]]:
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            print(f"Error: User '{username}' not found.")
            return []
        elif response.status_code == 403:
            print("Error: Rate limit exceeded. Please try again later.")
            return []
        elif response.status_code != 200:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")
            return []
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Network error - {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


from datetime import datetime
import requests
from typing import List, Dict, Any

# رنگ برای ترمینال
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False


def fetch_user_activity(username: str) -> List[Dict[str, Any]]:
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            print(f"Error: User '{username}' not found.")
            return []
        elif response.status_code == 403:
            print("Error: Rate limit exceeded. Please try again later.")
            return []
        elif response.status_code != 200:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")
            return []
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Network error - {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def display_activity(events: List[Dict[str, Any]]) -> None:
    if not events:
        print("No recent activity found for this user.")
        return
    
    print(f"\nRecent activity for user (showing up to {min(10, len(events))} events):\n")
    
    for event in events[:10]:
        event_type = event.get('type', 'Unknown')
        repo_name = event.get('repo', {}).get('name', 'Unknown repo')
        created_at = event.get('created_at', '')
        
        
        time_str = ""
        if created_at:
            try:
                dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                time_str = f" {Fore.YELLOW}({dt.strftime('%Y-%m-%d %H:%M')}){Style.RESET_ALL}"
            except:
                pass
        
        if event_type == "PushEvent":
            
            print(f"• {Fore.CYAN}Pushed to{Style.RESET_ALL} {repo_name}{time_str}")
        
        elif event_type == "IssuesEvent":
            action = event.get('payload', {}).get('action', 'created').capitalize()
            print(f"• {Fore.GREEN}{action} a new issue{Style.RESET_ALL} in {repo_name}{time_str}")
        
        elif event_type == "WatchEvent":
            print(f"• {Fore.YELLOW}Starred{Style.RESET_ALL} {repo_name}{time_str}")
        
        elif event_type == "ForkEvent":
            print(f"• {Fore.MAGENTA}Forked{Style.RESET_ALL} {repo_name}{time_str}")
        
        elif event_type == "CreateEvent":
            ref_type = event.get('payload', {}).get('ref_type', '')
            print(f"• Created {ref_type} in {repo_name}{time_str}")
        
        else:
            print(f"• {event_type.replace('Event', '')} in {repo_name}{time_str}")