Team Name:
SignBridge

Team Members:
- Arnav Yadav
- Rohit Desai
- Kalpak Gugale
- Riya Boladra

Project Name:
SignBridge – Bridging the Communication Gap with Hand Signs

Project Abstract:
SignBridge is a simple real-time hand gesture recognition system that helps non-sign-language users communicate easily with deaf and mute individuals. It uses a webcam to detect basic hand signs and displays the meaning on the screen using text. The goal is to break communication barriers using an easy tool.

Tech Stack:
- Language: Python
- Hand Tracking: MediaPipe
- Webcam & Display: OpenCV
- Code Hosting: GitHub
- Environment: Runs on local laptop

Dataset Used:
- No dataset used in this version.
- Gestures are detected using rule-based logic (no machine learning).
- In the future, a gesture image dataset can be used to train a model.

How It Works:
1. Opens webcam
2. Detects hand using MediaPipe
3. Checks finger positions
4. Matches them to basic gestures (like Hello)
5. Displays result on screen

How to Run:
1. Install dependencies:
   pip install mediapipe opencv-python

2. Run the program:
   python signbridge.py

Press Q to quit the window.

Future Improvements:
- Add more signs like Yes, No, Thank You
- Add text-to-speech (TTS) to speak the recognized signs
- Use machine learning to recognize more complex signs
- Build a mobile or web version

Built For:
College Hackathon – to support disable ones with accessibility of easy communication inclusion using tech.

