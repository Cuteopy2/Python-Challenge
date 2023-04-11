import os
import csv


def elections_results(input_file, output_file):
    
    # Initialize variables
    total_votes = 0
    candidates = {}

    # Read the input file line by line

    csvpath = os.path.join('Resources', 'election_data.csv') 
    print(csvpath)

    with open (csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader) 
         # Skip header line

        # Iterate through each row in the CSV file
        for row in csvreader:
            # Get the candidate's name from the row
            candidate = row[2]
            # Increment the total votes counter
            total_votes += 1

            # Add the candidate to the candidates dictionary or increment their vote count
            if candidate not in candidates:
                candidates[candidate] = 1
            else:
                candidates[candidate] += 1

    # Find the winner based on popular vote
    winner = max(candidates, key=candidates.get)

    # Print the election results to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # Write the election results to the output file
    with open(output_file, "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")

        # Iterate through the candidates and calculate their vote percentages
        for candidate, votes in candidates.items():
            vote_percentage = (votes / total_votes) * 100
            print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
            file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")

        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")


# Call the elections_results function to execute the script
input_file = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('analysis, Election_Results.tx')
elections_results(input_file, output_file)

