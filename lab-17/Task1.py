import pandas as pd
import numpy as np

#  Create a sample employee dataset
data = {
    'employee_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Anita', 'Rahul', 'Suresh', 'Divya', 'Neha', 'Ravi', 'Meena'],
    'salary': [55000, 62000, None, 58000, None, 60000, 75000],
    'department': ['HR', 'human resources', 'hr', 'Sales & Marketing', 'Finance', None, 'Human Resources'],
    'job_role': ['Manager', 'Executive', 'HR Officer', 'Sales Rep', 'Accountant', 'Clerk', 'Recruiter'],
    'joining_date': ['2020-01-15', None, '2019-03-10', '2021-07-22', '2020-12-05', '2018-09-14', None]
}


df = pd.DataFrame(data)


print("Sample Employee Dataset (Raw):\n")
print(df)


df.to_csv('employee_data.csv', index=False)
print("\n Dataset saved as 'employee_data.csv'")
