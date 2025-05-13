import time
import sys
import re
from typing import List, Dict, Any

def get_user_input() -> str:
    """Get the initial story request from the user."""
    print("What kind of bedtime story would you like to hear today? 📚")
    print("(For example: 'A story about a brave turtle who's afraid of water')")
    return input("> ")

def display_story(story: str) -> None:
    """Display the generated story with a typewriter effect and formatting."""
    
    lines = story.strip().split('\n')
    
    if lines and (lines[0].isupper() or lines[0].startswith('# ') or len(lines[0]) < 50):
        title = lines[0].replace('# ', '').strip()
        content = '\n'.join(lines[1:]).strip()
        
        print("\n" + "=" * 50)
        print(f"📖  {title.upper()}  📖")
        print("=" * 50 + "\n")
        
        _typewriter_effect(content)
    else:
        _typewriter_effect(story)
    
    print("\n" + "=" * 50 + "\n")

def _typewriter_effect(text: str, speed: float = 0.01) -> None:
    """Helper function to create a typewriter effect when displaying text."""

    paragraphs = text.split('\n')
    
    for paragraph in paragraphs:
        if paragraph.strip():
            
            is_dialogue = paragraph.strip().startswith('"') or paragraph.strip().startswith('-')
            
            if is_dialogue:
                print("  ", end="")
            
            for char in paragraph:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
            
            print("\n")
            time.sleep(0.3)  

def get_feedback() -> str:
    """Get feedback or requests for story modifications from the user."""
    print("\nAny changes you'd like to make?")
    print("(You can ask for changes like 'make it funnier' or 'add a dragon')")
    print("(Or type 'exit' to quit)")
    return input("> ")

def format_analysis_for_display(analysis: Dict[str, Any]) -> List[str]:
    """Format the analysis results for display."""
    formatted = []
    
    formatted.append(f"🎭 Theme: {analysis['theme'].capitalize()}")
    formatted.append(f"✨ Tone: {analysis['tone'].capitalize()}")
    formatted.append(f"👥 Characters: {', '.join(analysis['characters'])}")
    formatted.append(f"📈 Story Arc: {analysis['story_arc'].capitalize()}")
    
    formatted.append(f"👶 Age Focus: Around {analysis['age_focus']} years old")
    
    return formatted