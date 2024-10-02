# Vowel Detector Program

## Description
This is a simple Python program that detects vowels in a word or phrase. The program counts the number of vowels and also provides a breakdown of how many times each vowel appears.

## Features
- Counts both uppercase and lowercase vowels (A, E, I, O, U).
- Provides a summary of vowel counts for the given word or phrase.
- Allows users to check multiple words or phrases in one session.

## How to Run the Program
1. Ensure you have Python installed on your machine.
2. Copy the provided code into a Python script file, e.g., `vowel_detector.py`.
3. Open your terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the command:
   
   ```bash
   
   python vowel_detector.py
   
## Code Explanation

### Input
- The program prompts the user for their name and a word or phrase to check for vowels.

### Process
- A `while True` loop is used to allow multiple inputs.
- The program iterates through each letter in the input word to check if it is a vowel.
- Vowel counts and the presence of each vowel are tracked using individual counters and lists. Each vowel (both uppercase and lowercase) has its own counting mechanism.

### Output
- The program displays:
  - Total number of vowels in the input.
  - The count of each vowel detected.
