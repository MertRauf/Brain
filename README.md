Brain Functions Simulation and Educational Quiz System
Overview
This project is an educational initiative designed to enhance learning in the field of neuroscience and mathematics through interactive applications. It consists of two components:

Brain Functions Simulation (Python): A Tkinter-based application that interfaces with an Arduino to simulate brain functions (vision, hearing, speech, movement, smell) or display educational information about them. It features a fullscreen interface with a brain image, theme support, and an education mode for learning.
Brain Functions Arduino Controller (Arduino): An Arduino sketch that controls LEDs representing different brain regions, responding to commands from the Python application to simulate brain activity through LED blinking sequences.

Additionally, a separate educational game, LoGGame, is included to help students practice logarithm problems interactively. Together, these components aim to provide hands-on learning experiences in neuroscience and mathematics for educational purposes.
Features
Brain Functions Simulation (Python)

Arduino Integration: Connects to an Arduino via a serial port to send commands for brain function simulation.
Education Mode: Displays detailed information about brain functions (vision, hearing, speech, movement, smell) when enabled.
Theme Support: Offers light, dark, and red themes for the UI.
Fullscreen Interface: Displays a sagittal brain image with a control panel for interaction.
Connection Monitoring: Periodically checks Arduino connection status.
Responsive Controls: Supports mouse clicks and Escape key for navigation.

Brain Functions Arduino Controller (Arduino)

LED Control: Uses LEDs to represent brain regions:
Red: Frontal Lobe (Speech)
Green: Occipital Lobe (Vision)
Blue: Temporal Lobe (Hearing)
White: Motor Cortex (Movement) and Olfactory Bulb (Smell)
Yellow: Thalamus


Command Processing: Responds to single-character commands (S, V, H, M, O) from the Python application.
LED Test Sequence: Runs an initial test to verify LED functionality.
Serial Communication: Sends status messages (e.g., "Test Completed") to the Python application.

LoGGame (Python)

Logarithm Quiz: Offers logarithm problems at Easy, Medium, and Hard difficulty levels.
Timed Questions: Players answer within a 30-second time limit.
Hint System: Provides hints to assist with problem-solving (reduces points).
Scoreboard: Tracks and displays the top 10 scores with player names.
Exam Questions: Allows users to upload, view, and delete logarithm-related exam question images.
Sound Effects: Includes audio feedback for correct, incorrect, and timed-out answers (toggleable).
Confetti Animation: Celebrates correct answers with a visual effect.
Fullscreen Support: Adapts to the user’s screen resolution.

Educational Context
This project was developed as part of an educational initiative to engage students in learning about neuroscience and mathematics. The Brain Functions Simulation provides an interactive way to explore brain anatomy and function, either through physical LED simulations or educational content, making it suitable for classroom demonstrations or self-study. The LoGGame targets mathematical proficiency by gamifying logarithm problems, encouraging students to practice and improve their skills in an engaging format. Both components are designed to be accessible, interactive, and aligned with educational goals.
Requirements
Brain Functions Simulation (Python)

Python 3.x
tkinter: For the GUI (included with standard Python installations).
pyserial: For Arduino communication.
Pillow (PIL): For image handling.
Arduino: A compatible Arduino with the provided sketch loaded.
Asset: brain_sagittal.png (sagittal brain image).

Brain Functions Arduino Controller (Arduino)

Arduino IDE: For uploading the sketch.
Arduino Board: Compatible with serial communication (e.g., Arduino Uno).
Hardware:
LEDs (red, green, blue, white, yellow) connected to pins 9, 10, 11, 12, and 8 (or 7 for white LED testing).
Appropriate resistors for LEDs.



LoGGame (Python)

Python 3.x
Pygame: For game rendering and sound.
tkinter: For file dialogs (included with Python).
PyInstaller (optional): For creating standalone executables.
Assets:
Images: background.jpg, button.png, icon.png, logo.png, hint_icon.png
Sounds: correct_answer.wav, wrong_answer.wav, time_up.wav
Font: DJB Chalk It Up.ttf



Installation
Brain Functions Simulation (Python)

Install Python: Ensure Python 3.x is installed.
Install Dependencies:pip install pyserial pillow


Place Asset: Save brain_sagittal.png in the same directory as brain_control_app.py.
Arduino Setup: Upload the Arduino sketch (below) to your Arduino board.
Run the Application:python brain_control_app.py



Brain Functions Arduino Controller (Arduino)

Install Arduino IDE: Download and install the Arduino IDE.
Connect Hardware:
Connect LEDs to pins 9 (red), 10 (green), 11 (blue), 12 (white), and 8 (yellow) with appropriate resistors.
Optionally, use pin 7 for the white LED for testing.


Upload Sketch:
Open brain_controller.ino in the Arduino IDE.
Upload the sketch to your Arduino board.


Verify Serial Port: Note the port (e.g., COM5 on Windows, /dev/ttyUSB0 on Linux) for use in the Python application.

LoGGame (Python)

Install Python: Ensure Python 3.x is installed.
Install Dependencies:pip install pygame


Place Assets: Save all required assets (listed above) in the same directory as loggame.py.
Run the Game:python loggame.py



Usage
Brain Functions Simulation

Launch: Run brain_control_app.py.
Interface:
Control Panel: Enter the Arduino port (e.g., COM5) and click "Connect".
Function Buttons: Click "Vision", "Hearing", "Speech", "Movement", or "Smell" to:
Send a command to the Arduino (e.g., V for Vision) if education mode is off.
Display educational information if education mode is on.


Settings: Change the theme (Light, Dark, Red).
Education Mode: Toggle to switch between simulation and learning modes.
Exit: Close with the "Exit" button or Escape key.


Arduino Interaction:
The Arduino responds to commands by blinking LEDs corresponding to brain regions.
Connection status is displayed and checked every 5 seconds.



Brain Functions Arduino Controller

Setup: Ensure LEDs are connected and the sketch is uploaded.
Operation:
On startup, the Arduino runs a test sequence, blinking each LED for 0.5 seconds.
It then waits for serial commands (S, V, H, M, O) from the Python application.
For commands S, V, H, or M, the yellow LED (Thalamus) blinks rapidly, followed by the corresponding function LED (red, green, blue, or white).
For O (Smell), only the white LED blinks (no Thalamus involvement).
Serial feedback (e.g., "OK", "Invalid command!") is sent back to the Python application.



LoGGame

Launch: Run loggame.py.
Main Menu:
Start: Select a difficulty (Easy, Medium, Hard) and enter a player name.
Scoreboard: View top 10 scores.
About: Learn about logarithms or access the "Exam Questions" section.
Settings: Toggle sound on/off.


Gameplay:
Answer 5 logarithm questions within 30 seconds each.
Use the hint button or H key for assistance (reduces points).
Correct answers earn 10 points (5 with a hint); incorrect or timed-out answers earn 0.
View score, rank, correct answers, average answer time, and hints used at the end.


Exam Questions:
Upload .png or .jpg images to the questions directory.
Navigate with "Previous"/"Next" buttons or arrow keys.
Delete images with the "Delete Image" button.


Controls:
Mouse: Click buttons or input fields.
Keyboard: Enter to submit, H for hints, Left/Right for image navigation, M to return to the main menu, Escape to quit.



File Structure

Brain Functions Simulation:
brain_control_app.py: Main Python script.
brain_sagittal.png: Brain image file.
brain_controller.ino: Arduino sketch.


LoGGame:
loggame.py: Main game script.
scores.json: Stores high scores (auto-generated).
questions/: Directory for exam question images.
Assets: background.jpg, button.png, icon.png, logo.png, hint_icon.png, correct_answer.wav, wrong_answer.wav, time_up.wav, DJB Chalk It Up.ttf.



Building with PyInstaller (LoGGame)
To create a standalone executable for LoGGame:
pyinstaller --add-data "background.jpg;." --add-data "button.png;." --add-data "icon.png;." --add-data "logo.png;." --add-data "correct_answer.wav;." --add-data "wrong_answer.wav;." --add-data "time_up.wav;." --add-data "hint_icon.png;." --add-data "DJB Chalk It Up.ttf;." --add-data "questions;questions" --icon=icon.png --name LoGGame loggame.py

Note: Adjust --add-data syntax for your OS (; for Windows, : for macOS/Linux).
Notes

Brain Functions Simulation:
Ensure the Arduino is connected and running the provided sketch before launching the Python application.
The brain_sagittal.png file is required for the UI; missing files trigger an error message.
The application assumes a serial baud rate of 9600 and a timeout of 1 second.


Brain Functions Arduino Controller:
LEDs must be connected with appropriate resistors to avoid damage.
The white LED pin can be changed to 7 for testing (update the whiteLed constant).
Serial messages are in English for compatibility with the Python application.


LoGGame:
Missing assets trigger warnings and fallback visuals (e.g., yellow square with a question mark).
Scores are saved to scores.json in the script’s directory.
Logging is enabled at the DEBUG level for troubleshooting.


Educational Use: Both components are designed for classroom or self-study use, providing interactive tools to learn about brain functions and logarithm problem-solving.

License
This project is unlicensed and provided as-is for educational purposes.
Contact
For issues or suggestions, please contact the developer or open an issue on the repository (if applicable).

--

by MertRauf
