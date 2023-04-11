
# importing the module
import os
import csv
def pybank_analysis(input_file, output_file):
    

    # Initialize variables
	
    total_months = 0
    net_total_profit_losses = 0
    changes = []
    previous_profit_losses = None
    max_increase = [None, float('-inf')]
    max_decrease = [None, float('inf')]

    # Read the input file line by line
    with open(input_file) as file:
        next(file)  # Skip header line
        for line in file:
            # Split each line into date and profit/losses
            date, profit_losses = line.strip().split(',')
            profit_losses = int(profit_losses)

            # Increment the total months counter
            total_months += 1
            # Add profit_losses to net_total_profit_losses
            net_total_profit_losses += profit_losses

            # Calculate the changes in profit/losses
            if previous_profit_losses is not None:
                change = profit_losses - previous_profit_losses
                changes.append(change)

                # Update the greatest increase in profits
                if change > max_increase[1]:
                    max_increase = [date, change]

                # Update the greatest decrease in profits
                if change < max_decrease[1]:
                    max_decrease = [date, change]

            # Set the previous_profit_losses for the next iteration
            previous_profit_losses = profit_losses

    # Calculate the average of the changes
    average_changes = sum(changes) / len(changes)

    # Print the analysis to the terminal
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_profit_losses}")
    print(f"Average Change: ${average_changes:.2f}")
    print(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
    print(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")

    # Write the analysis results to the output file
    with open(output_file, "w") as file:
        file.write("Financial Analysis\n")
        file.write("------------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${net_total_profit_losses}\n")
        file.write(f"Average Change: ${average_changes:.2f}\n")
        file.write(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n")
        file.write(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n")

# Call the pybank_analysis function to execute the script
input_file = "budget_data.csv"
output_file = "financial_analysis.txt"
pybank_analysis(input_file, output_file)
# importing the module
import os
import csv

def pybank_analysis(input_file, output_file):
    

    # Initialize variables
	
    total_months = 0
    net_total_profit_losses = 0
    changes = []
    previous_profit_losses = None
    max_increase = [None, float('-inf')]
    max_decrease = [None, float('inf')]

 
    csvpath = os.path.join('Resources','budget_data.csv') 
    print(csvpath)

    # Read the input file line by line
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        next(csvreader)  
        
        # Skip header line
        for line in csvreader:
            
            # Split each line into date and profit/losses
            date = line[0]
            profit_losses = line[1]
            profit_losses = int(profit_losses)

            # Increment the total months counter
            total_months += 1

            # Add profit_losses to net_total_profit_losses
            net_total_profit_losses += profit_losses

            # Calculate the changes in profit/losses
            if previous_profit_losses is not None:
                change = profit_losses - previous_profit_losses
                changes.append(change)

                # Update the greatest increase in profits
                if change > max_increase[1]:
                    max_increase = [date, change]

                # Update the greatest decrease in profits
                if change < max_decrease[1]:
                    max_decrease = [date, change]

            # Set the previous_profit_losses for the next iteration
            previous_profit_losses = profit_losses

    # Calculate the average of the changes
    average_changes = sum(changes) / len(changes)

    # Print the analysis to the terminal
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_profit_losses}")
    print(f"Average Change: ${average_changes:.2f}")
    print(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
    print(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")

    output_file = os.path.join(r'analysis','financial_analysis.txt')
    # Write the analysis results to the output file
    with open(output_file, "w") as file:
        file.write("Financial Analysis\n")
        file.write("------------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${net_total_profit_losses}\n")
        file.write(f"Average Change: ${average_changes:.2f}\n")
        file.write(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n")
        file.write(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n")

# Call the pybank_analysis function to execute the script

input_file = os.path.join('Resources','budget_data.csv')
output_file = os.path.join('analysis','financial_analysis.txt')
pybank_analysis(input_file, output_file)