import os
from dotenv import load_dotenv
from story_generator import generate_story
from user_interface import get_user_input, display_story, get_feedback
from story_analyzer import analyze_request

"""
Before submitting the assignment, describe here in a few sentences what you would have built next if you spent 2 more hours on this project:

I would have added the following enhancements:
1. A more sophisticated story arc system with branching narratives based on user choices
2. Voice narration integration using a text-to-speech API
3. A story visualization component that generates simple illustrations for key moments
4. A memory system that recalls user preferences and previously generated stories for personalization
5. Age-appropriate vocabulary filtering based on reading level metrics
"""

def main():
    load_dotenv()
    
    print("🌟 Welcome to the Magical Bedtime Story Generator! 🌟")
    print("I can create wonderful stories for children ages 5-10.\n")
    
    story_request = get_user_input()
    
    analysis = analyze_request(story_request)
    
    story = generate_story(story_request, analysis)
    
    display_story(story)
    
    while True:
        feedback = get_feedback()
        if feedback.lower() in ['exit', 'quit', 'bye', 'no']:
            print("\nThank you for using the Magical Bedtime Story Generator! Sweet dreams! ✨")
            break
        
        analysis = analyze_request(story_request, feedback)
        story = generate_story(story_request, analysis, feedback)
        display_story(story)


if __name__ == "__main__":
    main()