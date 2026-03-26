# 🎙️ Voice Assistant

📌 **Internship:** AICTE OIB-SIP – Python Programming Internship  
🏢 **Organization:** Oasis Infobyte  
👩‍💻 **Intern:** Swarali Vishnu Suryawanshi  

---

## 📝 Project Overview

This project is a **Basic Voice Assistant** developed using Python as part of the AICTE OIB-SIP Internship at Oasis Infobyte.

The assistant listens to user voice commands and performs predefined tasks such as responding to greetings, telling the time and date, searching the web, and opening websites.

This project demonstrates the practical implementation of:

- 🎤 Speech Recognition  
- 🔊 Text-to-Speech Conversion  
- ⚙️ Command Processing  
- 🌐 Task Automation  

---

## 🚀 Features

- Responds to greetings (Hello / Hi)  
- Tells current time  
- Tells today’s date  
- Performs Google search  
- Opens YouTube  
- Exit/Stop command  
- Handles basic errors gracefully  
- Adjusts for ambient noise  

---

## 🎯 Objectives

- To understand how voice recognition works  
- To implement text-to-speech responses  
- To build an interactive voice-controlled system  
- To process user commands dynamically  
- To implement basic exception handling  

---

## 🛠️ Technologies Used

- Python 3  
- speech_recognition  
- pyttsx3  
- datetime  
- webbrowser  
- sys  
- time  

---

## ⚙️ Key Concepts Implemented

### 🔹 Speech Recognition
The assistant uses Google Speech Recognition API to convert spoken words into text.

### 🔹 Text-to-Speech (TTS)
The `pyttsx3` library is used to convert text responses into speech output.

### 🔹 Command Handling
Conditional logic is used to match user commands and trigger corresponding actions.

### 🔹 Error Handling
The program handles:
- Unrecognized voice input  
- Internet connectivity issues  
- Empty commands  

---

## 📂 Project Structure

Voice_Assistant/
│
├── voice_assistant.py
├── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Install Python

Check Python version:

python --version


If not installed, download from:  
https://www.python.org/downloads/

---

### 2️⃣ Install Required Libraries

pip install SpeechRecognition pyttsx3 pyaudio


If `pyaudio` gives an error on Windows:

pip install pipwin
pipwin install pyaudio

**
---

### 3️⃣ Run the Application

**
python voice_assistant.py


### ✅ Make sure:
- Microphone is connected  
- Internet connection is active  

---

## 🎤 Supported Voice Commands

| Voice Command | Action Performed |
|---------------|-----------------|
| "hello" / "hi" | Greeting response |
| "time" | Tells current time |
| "date" | Tells today's date |
| "search" | Performs Google search |
| "open youtube" | Opens YouTube |
| "exit" / "stop" | Closes the assistant |

---

## 📸 Project Screenshots

### 🔹 Assistant Starting and Greeting Response

<img width="827" height="312" alt="Screenshot" src="https://github.com/user-attachments/assets/03c844ec-ef2e-4ff3-86bf-908cf4118af8" />

---

### 🔹 Time, Date and Search Command Output

<img width="1134" height="525" alt="Screenshot" src="https://github.com/user-attachments/assets/cda80c51-d162-4c1d-81d7-a4c01fc10b0c" />

---

### 🔹 Open YouTube Execution

<img width="676" height="303" alt="Screenshot" src="https://github.com/user-attachments/assets/f14a699a-8b3a-4982-8273-b896865a314f" />

---

## Testing & Validation
- Verified command recognition accuracy.
- Handled edge cases such as empty commands or noise interruptions.

---

## 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Implementing speech recognition in Python  
- Building real-time voice-interactive systems  
- Integrating multiple Python libraries  
- Writing modular and structured code  
- Handling runtime errors effectively  

---

## 🌱 Future Enhancements

- Add weather updates using API integration  
- Implement email sending functionality  
- Add a GUI interface (Tkinter / PyQt)  
- Integrate NLP for improved understanding  
- Allow custom command personalization  

---

## 📜 Conclusion

The Voice Assistant project successfully demonstrates basic voice interaction and automation using Python. It provides foundational understanding of speech processing and real-time command execution.

This project was completed as part of the **AICTE OIB-SIP Python Programming Internship at Oasis Infobyte**.

---


