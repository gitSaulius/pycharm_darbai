# employees.csv
#   * Apskaičiuoti vidurkį, sumą, minimumą, maksimumą ir kitus statistinius rodiklius stulpeliuose arba grupėse
#      naudojant mean(), sum(), min(), max() ir kitas funkcijas.
#   * Grupuoti duomenis pagal tam tikrą stulpelį ir atlikti agregavimo operacijas, pvz., apskaičiuoti bendrą sumą ar
#     vidurkį kiekvienai grupės naudojant groupby() funkciją.
#   * Atlikti reikiamus duomenų valymo veiksmus, pvz., pašalinti dublikatus, užpildyti trūkstamas reikšmes arba
#     pašalinti netinkamas reikšmes.
#   * Sukurti naujus stulpelius, atlikdami skaičiavimus ar manipuliacijas su esamais stulpeliais, pvz., pridėti, sudėti
#     arba suskaidyti reikšmes.
#   * Redaguoti duomenų tipus, pvz., konvertuoti skaičių tipo stulpelius į datų tipo stulpelius arba atvirkščiai.
#   * Atlikti duomenų filtravimą, rūšiavimą ir sujungimą pagal sąlygas arba stulpelius.
#   * Vizualizuoti duomenis naudojant įvairias diagramas ir grafikus

# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('employees.csv')
# print(df.head(5))

# average_salary = df['SALARY'].mean()
# print(f"Average salary: {average_salary}")

# min_salary = df['SALARY'].min()
# print(f"Minimum salary: {min_salary}")

# max_salary = df['SALARY'].max()
# print(f"Maximum salary: {max_salary}")

# total_salary = df['SALARY'].sum()
# print(f"Total salary: {total_salary}")

# arba
# stats = df.agg({'SALARY': ['sum', 'mean', 'min', 'max', 'size']})
# print(stats)

# increased_salary = df['SALARY'] * 1.10
# print(increased_salary)

# department_salary = df.groupby('DEPARTMENT_ID').agg({'SALARY': ['mean']})
# print(department_salary)

# job_salary_avg = df.groupby('JOB_ID').agg({'SALARY': ['mean']})
# print(job_salary_avg)
# arba
# job_salary_avg2 = df.groupby('JOB_ID')['SALARY'].mean()
# print(job_salary_avg2)

# name_salary_avg = df.groupby('LAST_NAME').agg({'SALARY': ['mean']})
# print(name_salary_avg)
#  arba
# name_salary_avg2 = df.groupby('LAST_NAME')['SALARY'].mean()
# print(name_salary_avg2)

# drop_duplicates = df['FIRST_NAME'].drop_duplicates()
# print(drop_duplicates)

# df['NEW_SALARY'] = df['SALARY'] * 1.10
# print(df.head())

# df['DEPARTMENT_ID'] = pd.to_datetime(df['DEPARTMENT_ID'])
# print(df['DEPARTMENT_ID'].dtypes)

# nesigauna - reikia prideti datos formata (format='%d-%m-%Y)
# df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'])
# print(df['HIRE_DATE'].dtypes)

# filtered_salary = df[df['SALARY'] >= 10000][['FIRST_NAME', 'LAST_NAME', 'JOB_ID', 'DEPARTMENT_ID', 'SALARY']]
# print(filtered_salary)

# filtered_manager = df[df['MANAGER_ID'] == '100'][['FIRST_NAME', 'LAST_NAME', 'JOB_ID', 'DEPARTMENT_ID', 'SALARY']]
# print(filtered_manager)

# filtered_department = df[df['DEPARTMENT_ID'] == 100][['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'JOB_ID', 'HIRE_DATE']]
# print(filtered_department)

# job_salary_avg2.plot(kind='bar', figsize=(14, 12))
# plt.title('Atlyginimu suvestine pagal pareigas')
# plt.xlabel('Pareigos')
# plt.ylabel('Atlyginimas')
# plt.show()

# department_salary.plot(kind='bar', figsize=(14, 12))
# plt.title('Atlyginimu suvestine pagal departamenta')
# plt.xlabel('Departamentas')
# plt.ylabel('Atlyginimas')
# plt.show()

# department_salary.plot(kind='pie', subplots=True, figsize=(8, 4))
# plt.title('Atlyginimu suvestine pagal departamenta')
# plt.show()

