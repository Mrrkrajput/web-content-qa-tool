Hello! I’m AI engineer, and this is my Web Content Q&A Tool for the AI role assessment. Here’s how to run and use it on your system—simple and effective, just like my approach to AI!

---

How to Run It Locally
---------------------

1. **Get the Code**
   - If it’s on GitHub, open your terminal and type:
     ```
     git clone https://github.com/your-username/web-content-qa-tool.git
     cd web-content-qa-tool
     ```
     (Replace "your-username" with the GitHub ID hosting it.)
   - Or download `app.py` and `index.html`, put them in a folder like `web-content-qa-tool`, and navigate there:
     ```
     cd path-to-your-folder/web-content-qa-tool
     ```

2. **Install the Libraries**
   - In the terminal, run this to set up everything:
     ```
     pip install flask requests beautifulsoup4 trafilatura transformers torch
     ```

3. **Start the Tool**
   - Type this to launch it:
     ```
     python app.py
     ```
   - It’ll run at `http://localhost:5000`.

4. **Open in Browser**
   - Go to `http://localhost:5000` in your browser—ready to roll!

---

How to Use It
-------------

1. **Add Web Content**
   - In the "Enter URLs" box, enter URLs one per line, like:
     ```
     https://en.wikipedia.org/wiki/Python_(programming_language)
     ```
   - Click "Ingest Content" to load the data.

2. **Ask Your Question**
   - In "Ask a question," type something like:
     ```
     What is Python in simple terms?
     ```
   - Hit "Ask Question"—the answer pops up below, maybe "a powerful programming language for coding."

3. **Keep Exploring**
   - Add more URLs or ask more questions—whatever you want to test!

This is my take on an AI-powered Q&A tool—hope you like it for the assessment!
