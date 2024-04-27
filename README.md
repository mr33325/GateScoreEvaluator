
# GATE Exam Report Generator

This Python script generates a comprehensive report for the GATE (Graduate Aptitude Test in Engineering) exam based on the answer sheet and answer key provided by the user. The report includes various statistics such as total marks obtained, questions attempted, correct answers, wrong answers, not attempted questions, and percentages.

## Features

- Loads the answer sheet and answer key provided by the user.
- Calculates marks for each question based on the provided answer key.
- Generates an HTML report with detailed statistics and a color-coded table highlighting correct, wrong, and not attempted questions.
- Allows users to add special topics that need thorough understanding to the report.

## Prerequisites

- Python 3.x
- pandas library
- webbrowser module

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/gate-exam-report.git
   cd gate-exam-report
   ```

2. **Install Dependencies:**
   ```bash
   pip install pandas
   ```

3. **Run the Script:**
   ```bash
   python gate_exam_report.py
   ```

4. **Follow the Instructions:**
   - Enter the GATE examination year when prompted.
   - Provide the answer sheet and answer key in Excel format as per the script's instructions. You can look at the sample excel sheet in the project. put the answer sheet in answer key in the archive/<Exam_Year> folder. So that the program can pick it from there.
   - Once the script completes execution, a web browser will open automatically displaying the generated report.

5. **Adding Special Topics (Optional):**
   - At the end of the script execution, you will be prompted to add special topics that need thorough understanding.
   - Enter each topic one by one and press `0` when you're done.
   - These topics will be added to the report for reference.

## File Structure

- `gate_exam_report.py`: Main Python script that generates the report.
- `index.html`: HTML template for the report.
- `script.js`: JavaScript code for table sorting.
- `Archive/`: Directory containing GATE exam data for different years.
- `README.md`: Documentation file.

## Example Output

![GATE Exam Report](report_screenshot.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
