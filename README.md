# Cold Email Generator

## Overview

The Cold Email Generator is an AI-powered application designed to streamline the process of creating cold emails. By leveraging advanced language models and a robust tech stack, it enables users to generate, manage, and optimize personalized email content with ease. The application integrates seamlessly with tools like Streamlit for an interactive user interface, ChromaDB for efficient tech stack querying, and Llama3 for generating high-quality text.

Additionally, the Cold Email Generator supports customization and adaptability, allowing users to tailor email templates to specific industries or audiences. This makes it an ideal solution for professionals looking to enhance their outreach efforts while saving time and effort.

## 📸 Screenshot

![Screenshot 1](images/img1.png)
![Screenshot 2](images/img2.png)

## 🚀 Features
- Extracts job details from the provided text or URL.
- Generates a professional cold email using **LangChain**.
- Displays the generated email in a user-friendly, formatted layout.
- Offers customization options for the email before finalizing it.
- Provides an option to download the generated email with a single click for easy access and sharing.
- Leverages **Groq Cloud** for optimized LLM processing and personalization.

## Tech Stack

The Cold Email Generator is built using a modern and efficient tech stack to ensure high performance and seamless functionality:

- **Python**: Serves as the core programming language, enabling robust and scalable application development.
- **Streamlit**: Powers the interactive user interface, making it easy to manage and generate cold emails.
- **ChromaDB**: Acts as a specialized database for storing and querying tech stack links, ensuring relevant and efficient data retrieval.
- **Groq API**: Provides advanced AI capabilities for optimized language model processing and personalization.
- **Llama3**: A cutting-edge AI model used for generating high-quality, context-aware email content.
- **LangChain**: A versatile framework that integrates with Llama3 and other tools to streamline and enhance interactions with language models.

This combination of tools and technologies ensures that the Cold Email Generator delivers a user-friendly and powerful experience for creating personalized email content.


## Setup

### Prerequisites

1. **Python**: Ensure that Python is installed on your system.
2. **Anaconda**: Install Anaconda to manage Python environments and packages.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Faisalece18/LLM-Project-Cold-Email-Generator.git
   cd Cold-email-generator
   ```

2. **Navigate to the Project Directory**

    ```bash
    cd LLM-Project-Cold-Email-Generator
    ```

3. **Create and Activate a Conda Environment**

    ```bash
    conda create --name GenAiProject python=3.8
    conda activate GenAiProject
    ```

4. **Install Required Packages**

    Install the necessary libraries using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, you can install packages individually using conda or pip.

5. **Set Up Environment Variables**

    Create a `.env` file in the root of the project directory with the following content:

    ```plaintext
    groq_api_key=your_groq_api_key_here
    ```

    Replace `your_groq_api_key_here` with your actual GROQ API key. The API key is necessary for the project to access the GROQ services.

## Usage

1. **Run the Application**

    To start the application, run the following command:

    ```bash
    streamlit run Final_Project\main.py
    ```

    Make sure to have Streamlit installed in your environment.

2. **Access the Application**

    Open a web browser and navigate to `http://localhost:8501` to interact with the Cold Email Generator.

## Project Structure

- **`app.py`**: The main application script that runs the Cold Email Generator.
- **`requirements.txt`**: A file listing the Python dependencies required for the project.
- **`.env`**: Environment file where sensitive information such as API keys are stored.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please feel free to submit a pull request or open an issue.

## Contact

For any questions or feedback, please contact the repository owner via GitHub.

---

**Note**: Ensure you have set up your `.env` file correctly with a valid GROQ API key before running the application.
