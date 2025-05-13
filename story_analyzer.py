import os
import openai
from typing import Dict, Any
import json

def analyze_request(story_request: str, feedback: str = "") -> Dict[str, Any]:
    """
    Analyze the story request to determine appropriate parameters for generation.
    Returns a dictionary with analysis details.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    analysis_prompt = f"""
    Analyze this bedtime story request for children ages 5-10: "{story_request}"
    
    If there's feedback, also consider it: "{feedback if feedback else 'None provided'}"
    
    Provide a JSON response with the following fields:
    1. "theme": The main theme of the requested story
    2. "tone": Most appropriate tone (options: whimsical, educational, adventurous, comforting, magical)
    3. "characters": A list of main characters to include
    4. "story_arc": Recommended story structure (options: hero's journey, problem-solution, discovery, friendship tale)
    5. "creativity_level": How much creative freedom to use (options: low, medium, high)
    6. "age_focus": Which end of the 5-10 age range this seems most appropriate for
    7. "sensory_elements": List of sensory elements to include (sights, sounds, textures)
    8. "vocabulary_level": Difficulty of vocabulary to use (options: simple, moderate, challenging)
    9. "emotional_elements": Key emotions to evoke in the story
    10. "special_considerations": Any special considerations based on the request

    Only respond with valid JSON. Make educated guesses if information is not explicitly provided.
    """
    
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You respond only with valid JSON."},
                {"role": "user", "content": analysis_prompt}
            ],
            stream=False,
            max_tokens=1000,
            temperature=0.1,
            response_format={"type": "json_object"}
        )
        response_text = resp.choices[0].message["content"]  
        return json.loads(response_text)
    except (json.JSONDecodeError, KeyError):
        
        return {
            "theme": "adventure",
            "tone": "comforting",
            "characters": ["protagonist", "friend", "guide"],
            "story_arc": "problem-solution",
            "creativity_level": "medium",
            "age_focus": 7,
            "sensory_elements": ["colors", "sounds", "textures"],
            "vocabulary_level": "moderate",
            "emotional_elements": ["courage", "friendship", "wonder"],
            "special_considerations": "None"
        }