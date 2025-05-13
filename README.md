# Magical Bedtime Story Generator for Hippocratic AI

This project provides a comprehensive and engaging bedtime story generation solution, designed to create tailored and interactive storytelling experiences.

## Key Features

* **Smart Story Analysis:** Intelligently analyzes story requests to determine appropriate themes, characters, story arcs, and more, ensuring highly relevant and personalized stories.
* **Interactive Experience:** Goes beyond simple generation by allowing users to provide feedback and iteratively refine the generated story content.
* **Engaging Presentation:** Presents stories with a captivating typewriter effect, making the reading experience feel magical.
* **Age-Appropriate Customization:** Automatically adjusts vocabulary level, themes, and complexity based on the specified target age within the 5-10 year range.
* **Modular Architecture:** The codebase is well-organized into separate files with clear responsibilities, promoting maintainability and scalability:
    * `main.py`: Contains the core application flow and orchestrates the different modules.
    * `story_analyzer.py`: Handles the analysis of user requests to extract relevant parameters for story generation.
    * `story_generator.py`: Responsible for the actual generation of the bedtime story based on the analyzed parameters.
    * `user_interface.py`: Manages user interaction, input prompts, and the display of the generated stories.

## How It Works

1.  **Initiation:** Upon running `main.py`, the application greets the user and prompts for a bedtime story request.
2.  **Request Analysis:** The user's request is sent to the OpenAI API via the `story_analyzer.py` module. This analysis extracts key information such as desired themes, characters, and the overall story arc. The response is structured in JSON format for easy processing.
3.  **Tailored Prompt Generation:** Based on the analyzed information, `story_analyzer.py` generates a specific and age-appropriate prompt to guide the story generation process.
4.  **Story Generation:** The tailored prompt is then passed to the OpenAI API through the `story_generator.py` module, which handles the actual generation of the bedtime story. Generation parameters like temperature are dynamically adjusted based on the analysis.
5.  **Engaging Display:** The generated story is displayed to the user in an engaging manner using a typewriter effect implemented in `user_interface.py`.
6.  **Interactive Refinement:** The user is then given the opportunity to provide feedback on the generated story. This feedback (e.g., "make it funnier," "add a dragon") can be used to further refine the story through subsequent generation steps.

## Technical Details

* **Structured JSON Analysis:** The `response_format={"type": "json_object"}` parameter is used during the analysis step to ensure structured and easily parsable JSON data is received from the OpenAI API.
* **Robust Error Handling:** The system includes mechanisms to gracefully handle potential JSON parsing failures, ensuring a smoother user experience.
* **Secure API Key Management:** API keys are securely stored as environment variables in a `.env` file. This file is explicitly excluded from version control using `.gitignore`.
* **Enhanced User Experience:** The inclusion of a typewriter effect and thoughtful formatting significantly enhances the user's engagement with the generated stories.
* **Adaptable Generation Parameters:** The system dynamically adjusts OpenAI's generation parameters (e.g., temperature) based on the analysis of the user's request, allowing for more creative or focused story generation as needed.

## How to Run

1.  **Install Dependencies:** Ensure all necessary libraries are installed by running the following command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Application:** Execute the main script:
    ```bash
    python main.py
    ```
3.  **Follow Prompts:** Simply follow the on-screen prompts to input your story request and interact with the generated stories.