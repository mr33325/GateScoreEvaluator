import pandas as pd
import re
import os
import sys
import webbrowser

exam_year= input("Enter The GATE Examination Year: ")

# Get the current working directory and set the file path
current_directory = os.getcwd()
current_directory =current_directory.replace('\\', '/')
base_path= 'Archive/'+ exam_year +'/'
answer_sheet= base_path + 'answer_sheet_' + exam_year +'.xlsx'
answer_key= base_path + 'answer_key_' + exam_year +'.xlsx'
report_path= base_path + 'Test_Report_' + exam_year +'.html'

# Load the answer sheet and answer key
answer_sheet_df = pd.read_excel(answer_sheet, usecols=['Q. No.', 'Answer'])
answer_key_df = pd.read_excel(answer_key, usecols=['Q. No.', 'Question Type', 'Key', 'Mark'])

# Merge the answer sheet and answer key on question number
merged_df = pd.merge(answer_sheet_df, answer_key_df, on='Q. No.')
merged_df['Colour']=None 
correct= []
wrong= []
not_attempted= []

# Function to calculate marks based on the given rules
def calculate_marks(row):
    if row['Question Type'] == 'MCQ':
        if row['Key'] == 'MTA':
            correct.append(row['Q. No.'])
            return row['Mark']
        elif pd.isnull(row['Answer']):
            not_attempted.append(row['Q. No.'])
            return 0
        elif row['Answer'] == row['Key']:
            correct.append(row['Q. No.'])
            return row['Mark']
        else:
            row['Colour']='R'
            wrong.append(row['Q. No.'])
            return -1 / 3 if row['Mark'] == 1 else -2 / 3
    elif row['Question Type'] == 'MSQ':
        if pd.isnull(row['Answer']):
            not_attempted.append(row['Q. No.'])
            return 0
        
        given_answer_list = row['Answer'].split(', ')  # Assuming answers are separated by ', ' in the answer sheet
        key_list = row['Key'].split(', ')  # Assuming keys are separated by ', ' in the answer key
        
        if len(given_answer_list)==len(key_list) and all(answer in key_list for answer in given_answer_list):
            correct.append(row['Q. No.'])
            return row['Mark']
        else:
            row['Colour']='R'
            wrong.append(row['Q. No.'])
            return 0
    elif row['Question Type'] == 'NAT':
        if pd.isnull(row['Answer']):
            not_attempted.append(row['Q. No.'])
            return 0
        
        if "OR" in row['Key']:
            range_ans = list(set(float(value) for value in re.split(r'\s+to\s+|\s+OR\s+', row['Key'])))
            answer = float(row['Answer'])
            
            if answer in range_ans:
                correct.append(row['Q. No.'])
                return row['Mark']
            else:
                row['Colour']='R'
                wrong.append(row['Q. No.'])
                return 0

        else:
            range_start, range_end = map(float, row['Key'].split(' to '))
            answer = float(row['Answer'])
            
            if range_start <= answer <= range_end:
                correct.append(row['Q. No.'])
                return row['Mark']
            else:
                row['Colour']='R'
                wrong.append(row['Q. No.'])
                return 0


# Apply the calculate_marks function to each row and calculate total marks
merged_df['Obtained Marks'] = merged_df.apply(calculate_marks, axis=1)

# Calculate total marks
total_marks = merged_df['Obtained Marks'].sum()

# Print the total marks
print('Total Marks Obtained: '+ str(total_marks) + '/100')
merged_df = merged_df[['Q. No.', 'Answer', 'Key', 'Question Type', 'Mark', 'Obtained Marks', 'Colour']]
for i in correct:
    merged_df.loc[i-1, 'Colour']= 'G'
for i in wrong:
    merged_df.loc[i-1, 'Colour']= 'R'
for i in not_attempted:
    merged_df.loc[i-1, 'Colour']= 'Y'
    
#merged_df.to_excel("MarksData.xlsx")
#merged_df.to_json('MarksData.json')


###--------------------------------------- HTML Rendering---------------------------------------------------------- ###
correct_questions= correct
wrong_questions= wrong
not_attempted_questions= not_attempted
# Calculate additional statistics
total_questions = len(correct_questions) + len(wrong_questions) + len(not_attempted_questions)
questions_attempted = len(correct_questions) + len(wrong_questions)  # Corrected this line
percentage_correct = (len(correct_questions) / questions_attempted) * 100 if questions_attempted > 0 else 0
percentage_wrong = (len(wrong_questions) / questions_attempted) * 100 if questions_attempted > 0 else 0
percentage_not_attempted = (len(not_attempted_questions) / total_questions) * 100

# Create HTML content (transposed table with additional statistics)
with open("index.html", "r") as html_file:
    html_content = html_file.read()

# Format question lists for HTML display
correct_str = ", ".join(map(str, correct_questions))
wrong_str = ", ".join(map(str, wrong_questions))
not_attempted_str = ", ".join(map(str, not_attempted_questions))

table= merged_df.to_html(index=False)
table= table.replace('<table border="1" class="dataframe">', '<table id="myTable" class="table table-bordered table-sm">')
table= table.replace('<tr style="text-align: right;">', '<tr>')

# Load Js script file
with open("script.js", "r") as js_file:
    table_js = js_file.read()

# Populate HTML content with formatted question numbers and statistics
html_content = html_content.format(exam_year, total_marks, correct_str, wrong_str, not_attempted_str,
                                   total_questions, questions_attempted,
                                   len(correct_questions), percentage_correct, 
                                   len(wrong_questions), percentage_wrong,
                                   len(not_attempted_questions), percentage_not_attempted, table, table_js)

# Write the HTML content to a file
with open(report_path, "w") as html_file:
    html_file.write(html_content)

report_path = current_directory + '/' + report_path
print("HTML page created at: ", report_path)
webbrowser.open(report_path)

### ---------------------------- Add the topics to the report that need special attention ----------------------------------------###

checkpoint = input("Do you want to add the topics that need thorough understanding? Press 1 if Yes or 0 if No")

if(checkpoint == '1'):
    badge=''
    spans=''
    while(1):
        badge= input("Enter the key point or Enter 0 to exit: ")
        if(badge=='0'):
            break
        spans= spans + '<span class="badge bg-primary">' + badge + '</span> '
        
    html_content= html_content.replace('#null#', spans + '#null#')
    with open(report_path, "w") as html_file:
        html_file.write(html_content)
    webbrowser.open(report_path)
else:
    sys.exit(0)
