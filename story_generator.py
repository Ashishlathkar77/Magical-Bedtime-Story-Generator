import os
import openai
import json
from typing import Dict, Any

def call_model(prompt: str, max_tokens=3000, temperature=0.1) -> str:
    """Call the OpenAI API with the given prompt."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=False,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return resp.choices[0].message["content"]  

def call_model_with_json(prompt: str, max_tokens=3000, temperature=0.1) -> Dict[str, Any]:
    """Call the OpenAI API with JSON mode to get structured outputs."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You respond only with valid JSON."},
                {"role": "user", "content": prompt}
            ],
            stream=False,
            max_tokens=max_tokens,
            temperature=temperature,
            response_format={"type": "json_object"}
        )
        response_text = resp.choices[0].message["content"]  
        return json.loads(response_text)
    except json.JSONDecodeError:
        
        return {"error": "Failed to parse JSON response"}

def generate_story(story_request: str, analysis: Dict[str, Any], feedback: str = "") -> str:
    """Generate a bedtime story based on the request and analysis."""

    age_appropriate_tone = analysis["tone"]
    theme = analysis["theme"]
    characters = analysis["characters"]
    story_arc = analysis["story_arc"]
    
    temp = 0.7 if analysis["creativity_level"] == "high" else 0.4
    
    story_prompt = f"""
    You are a master storyteller specializing in creating delightful bedtime stories for children ages 5-10. 
    
    Story Request: "{story_request}"
    
    Based on the analysis:
    - Theme: {theme}
    - Tone: {age_appropriate_tone}
    - Story Arc: {story_arc}
    - Main Characters: {characters}
    
    Writing Guidelines:
    1. Use age-appropriate language, avoiding complex vocabulary but still introducing 2-3 new words with context clues.
    2. Keep paragraphs short (3-4 sentences) and use dialogue to break up text.
    3. Include a gentle moral lesson or positive message without being preachy.
    4. Create a satisfying, hopeful ending that brings closure.
    5. The story should be paced for a 5-7 minute reading time.
    6. Use vivid sensory descriptions that appeal to a child's imagination.
    7. Include moments of gentle humor or surprise.

    ✨✨ IMPORTANT STYLE REQUIREMENT ✨✨
    - Use **relevant emojis generously** throughout the story 🎉🌈✨🧸📚 to make it visually fun and expressive! 🥳
    - Ensure emojis match the context and emotions of the scenes (e.g., 🐶 for dog, 🌧️ for rainy scene, 🏰 for castle, 🌟 for magic).
    - Use emojis in narration, dialogue, and even to emphasize sound effects like *"Boom!" 💥 or "Splash!" 💦*
    - Don't overuse the same emojis; vary them across scenes.
    
    Format the story with a **title**, **clear paragraph breaks**, **engaging dialogue**, and **emojis** throughout.

    Additional feedback to incorporate: {feedback if feedback else "None provided"}
    """
    
    story = call_model(story_prompt, max_tokens=2500, temperature=temp)
    
    return story