Brain Functions Simulation
Overview
This project is an educational initiative designed to enhance learning in the field of neuroscience through an interactive application and hardware interface. It consists of two components:

Brain Functions Simulation (Python): A Tkinter-based application that interfaces with an Arduino to simulate brain functions (vision, hearing, speech, movement, smell) or display educational information about them. It features a fullscreen interface with a brain image, theme support, and an education mode for learning.
Brain Functions Arduino Controller (Arduino): An Arduino sketch that controls LEDs representing different brain regions, responding to commands from the Python application to simulate brain activity through LED blinking sequences.

These components are designed to provide hands-on learning experiences for students studying neuroscience, making complex brain functions accessible through visual simulations and educational content.
Features
Brain Functions Simulation (Python)

Arduino Integration: Connects to an Arduino via a serial port to send commands for brain function simulation.
Education Mode: Displays detailed information about brain functions (vision, hearing, speech, movement, smell) when enabled.
Theme Support: Offers light, dark, and red themes for the UI.
Fullscreen Interface: Displays a sagittal brain image with a control panel for interaction.
Connection Monitoring: Periodically checks Arduino connection status.
Responsive Controls: Supports mouse clicks and the Escape key for navigation.

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

Educational Context
This project was developed as part of an educational initiative to engage students in learning about neuroscience. The Brain Functions Simulation provides an interactive platform to explore brain anatomy and function, either through physical LED simulations controlled by an Arduino or through educational content displayed in education mode. It is suitable for classroom demonstrations, self-study, or educational workshops, offering a tangible way to understand how different brain regions contribute to functions like vision, hearing, speech, movement, and smell.
Requirements
Brain Functions Simulation (Python)

Python 3.x
tkinter: For the graphical user interface (included with standard Python installations).
pyserial: For Arduino communication.
Pillow (PIL): For image handling.
Arduino: A compatible Arduino board with the provided sketch loaded.
Asset: brain_sagittal.png (sagittal brain image).

Brain Functions Arduino Controller (Arduino)

Arduino IDE: For uploading the sketch.
Arduino Board: Compatible with serial communication (e.g., Arduino Uno).
Hardware:
LEDs (red, green, blue, white, yellow) connected to pins 9, 10, 11, 12, and 8 (or 7 for white LED testing).
Appropriate resistors for LEDs.



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
Optionally, use pin 7 for the white LED for testing (update the whiteLed constant).


Upload Sketch:
Open brain_controller.ino in the Arduino IDE.
Upload the sketch to your Arduino board.


Verify Serial Port: Note the port (e.g., COM5 on Windows, /dev/ttyUSB0 on Linux) for use in the Python application.

Usage
Brain Functions Simulation

Launch: Run brain_control_app.py.
Interface:
Control Panel (left side):
Arduino Port: Enter the serial port (default: COM5) and click "Connect".
Function Buttons: Click "Vision", "Hearing", "Speech", "Movement", or "Smell" to:
Send a command to the Arduino (e.g., V for Vision) if education mode is off.
Display educational information if education mode is on.


Settings: Change the theme (Light, Dark, Red).
Education Mode: Toggle to switch between simulation and learning modes.
Exit: Close the application with the "Exit" button or Escape key.


Canvas: Displays the brain image (brain_sagittal.png).


Controls:
Mouse: Click buttons or input fields.
Keyboard: Escape to exit the application.


Arduino Interaction:
The Arduino responds to commands by blinking LEDs corresponding to brain regions.
Connection status is displayed and checked every 5 seconds.



Brain Functions Arduino Controller

Setup: Ensure LEDs are connected and the sketch is uploaded.
Operation:
On startup, the Arduino runs a test sequence, blinking each LED for 0.5 seconds.
It then waits for serial commands (S, V, H, M, O) from the Python application.
For commands S, V, H, or M, the yellow LED (Thalamus) blinks rapidly (10 times at 50ms intervals), followed by the corresponding function LED (red, green, blue, or white) blinking 5 times at 100ms intervals.
For O (Smell), only the white LED blinks (no Thalamus involvement).
Serial feedback (e.g., "OK", "Invalid command!") is sent back to the Python application.



File Structure

brain_control_app.py: Main Python script for the Brain Functions Simulation.
brain_sagittal.png: Required brain image file.
brain_controller.ino: Arduino sketch for controlling LEDs.

Notes

Brain Functions Simulation:
Ensure the Arduino is connected and running the provided sketch before launching the Python application.
The brain_sagittal.png file is required for the UI; missing files trigger an error message.
The application assumes a serial baud rate of 9600 and a timeout of 1 second.


Brain Functions Arduino Controller:
LEDs must be connected with appropriate resistors to avoid damage.
The white LED pin can be changed to 7 for testing (update the whiteLed constant).
Serial messages are in English for compatibility with the Python application.


Educational Use: The project is designed for classroom or self-study use, providing an interactive tool to learn about brain functions through simulations and educational content.

License
This project is unlicensed and provided as-is for educational purposes.
Contact
For issues or suggestions, please contact the developer or open an issue on the repository (if applicable).

--

by MertRauf
