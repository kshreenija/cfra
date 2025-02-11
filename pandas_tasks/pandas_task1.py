import csv
# import pandas as pd
csv_file="/home/shreenija/Downloads/archive/StatewiseTestingDetails.csv"
# csv_file=pd.read_csv("/home/shreenija/Downloads/archive/StatewiseTestingDetails.csv")
# df=pd.DataFrame(csv_file)
# unique_states = list(set(df["State"]))
# print(unique_states)


# state_data=list(set())
# with open(csv_file,"r") as file:
#     reader = csv.DictReader(file)
#     headers = reader.fieldnames
#     for row in reader:
#          state_data.append(row["State"])
#         #  state_data=list(set(state_data))
#     # print(list(set(state_data)))
#     statewise_data=[]
#     data=[]
#     for state in state_data:
#         if row["State"]==state:
#             statewise_data.append({state:row})
#         data.append(row)    
#     # print(statewise_data)

# with open("states.csv","w") as file:
#     writer=csv.DictWriter(file,fieldnames=["Date","State","TotalSamples","Negative","Positive"])
#     writer.writeheader()
#     writer.writerows(data)
    

# import pandas as pd
# import os

# # Load the CSV file
# df = pd.read_csv("/home/shreenija/Downloads/archive/StatewiseTestingDetails.csv")

# # Get unique states
# unique_states = list(set(df["State"]))

# # Create a directory to store CSVs
# output_dir = "/home/shreenija/Downloads/archive/statewise_data"
# os.makedirs(output_dir, exist_ok=True)

# # Filter and save each state's data
# for state in unique_states:
#     state_df = df[df["State"] == state ] # Filter data for the state
#     file_name = f"{state}.csv"  # Safe filename
#     state_df.to_csv(file_name, index=False)  # Save without index
#     print(f"Saved: {file_name}")



# import csv

# csv_file = "/home/shreenija/Downloads/archive/StatewiseTestingDetails.csv"

# # Read the CSV file and extract unique states
# state_data = set()
# all_rows = []  # Store all rows for later processing

# with open(csv_file, "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     headers = reader.fieldnames  # Store headers if needed

#     for row in reader:
#         state_data.add(row["State"])  # Collect unique states
#         all_rows.append(row)  # Store all rows

# state_data = list(state_data)  # Convert set to list

# # Create a dictionary to store statewise data
# statewise_data = {state: []or state in state_data}

# for row in all_rows:
#     state = row["State"]
#     statewise_data[state].append(row)

# print(statewise_data)




# import csv
# csv_file = "/home/shreenija/Downloads/archive/StatewiseTestingDetails.csv"
# state_data = set()
# all_rows = [] 
# with open(csv_file, "r") as file:
#     reader = csv.DictReader(file)
#     headers = reader.fieldnames 
#     for row in reader:
#         state_data.add(row["State"])  
#         all_rows.append(row) 
# state_data = list(state_data)
# statewise_data = []
# for state in state_data:
#     for row in all_rows:
#         if row["State"] == state:
#             statewise_data.append(row) 
            
# with open("states.csv", "w") as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(statewise_data) 
# print(f"Saved statewise data to 'states.csv'")




import csv
csv_file = "/home/shreenija/Downloads/archive/StatewiseTestingDetails.csv"

state_data={}
with open(csv_file,"r") as file:
    reader = csv.DictReader(file)
    headers=reader.fieldnames
    for row in reader:
       state= row["State"]
       if state not in state_data:
            



           