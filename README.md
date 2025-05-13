# 🌙 Magical Bedtime Story Generator for Hippocratic AI ✨

Welcome to the **Magical Bedtime Story Generator**, a comprehensive solution that brings storytelling to life for children aged 5–10. This isn't just a simple text generator — it's an interactive, dynamic, and magical storytelling **experience**. ✨📖

---

## 🌟 Key Features

- **🧠 Smart Story Analysis**  
  The system analyzes each story request to determine appropriate themes, characters, story arc, and more — tailoring each story to your input.

- **🔁 Interactive Experience**  
  Generate a story, then give feedback like _"make it funnier"_ or _"add a dragon"_ to see an improved version!

- **📝 Engaging Presentation**  
  Stories are displayed with a typewriter effect, making the reading feel like a magical, animated experience.

- **👶 Age-Appropriate Customization**  
  Vocabulary, tone, and story complexity are automatically adjusted based on the child's age (within the 5–10 range).

- **🧩 Modular Architecture**  
  The project follows clean, maintainable code structure:

  - `main.py`: Core application flow  
  - `story_analyzer.py`: Analyzes requests for themes, characters, tone, and arc  
  - `story_generator.py`: Handles story generation using OpenAI API  
  - `user_interface.py`: Manages user interaction and visual presentation

---

## ⚙️ How It Works

1. Run `main.py` and provide a story request (e.g., "A penguin who wants to become an astronaut").
2. The input is analyzed using OpenAI's API to extract structured storytelling parameters like:
   - Theme  
   - Character types  
   - Story arc  
3. A customized prompt is generated and used to create an age-appropriate bedtime story.
4. The story is displayed using an engaging typewriter-style animation.
5. Optionally, refine the story with feedback — the system intelligently updates it for a better experience.

---

## 🧪 Technical Details

- **📦 Structured JSON Analysis**  
  Uses `response_format={"type": "json_object"}` to receive structured parameters from OpenAI for better prompt engineering.

- **⚠️ Error Handling**  
  Includes fallbacks for JSON parsing failures and ensures a smooth user experience.

- **🔐 Environment Variable Management**  
  API keys are securely stored in a `.env` file and excluded from version control with `.gitignore`.

- **🎨 User Experience Enhancements**  
  Typewriter effect and clean formatting make the reading process more engaging and magical.

- **🎛️ Adaptable Generation Parameters**  
  Automatically adjusts model parameters like `temperature` based on the tone and creative depth of the story.

---

## 🚀 How to Run

1. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   
2. **Set your OpenAI API key:**

   Create a .env file in the root directory with the following content:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   
3. **Run the application:**

   ```bash
   python main.py

4. **Follow the prompts to generate and refine your story!**
