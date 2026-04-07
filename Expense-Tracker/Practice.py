import csv
def main():
    # We will use a dictionary to keep track of total spending in each category.
    # A dictionary in Python holds key-value pairs, like: {"food": 50.0, "traveling": 20.0}
    category_totals = {}
    
    # Store the grand total of everything spent
    total_spent = 0.0
    
    print("Welcome to the Expense Tracker!")
    print("Reading expenses.csv...\n")
    
    # Open the file. The 'r' means we are just reading it, not writing.
    try:
        with open('expenses.csv', 'r') as file:
            # reader helps us go through the file line by line
            reader = csv.reader(file)
            
            # We want to skip the first line because it's just headers (Date, Description, etc.)
            next(reader) 
            
            # Loop through each row in the CSV file
            for row in reader:
                # The data is organized like this in our file: [Date, Description, Category, Amount]
                # So category is at position 2, and amount is at position 3.
                category = row[1]
                
                # The amount is read as text right now, so we turn it into a decimal number (float)
                amount = float(row[2])
                
                # Add it to our grand total
                total_spent = total_spent + amount
                
                # Check if we have seen this category before
                if category in category_totals:
                    # If yes, add the amount to what we already have for this category
                    category_totals[category] = category_totals[category] + amount
                else:
                    # If this is a new category, start it off with this amount
                    category_totals[category] = amount

        # Now that we've read everything, let's print our results nicely
        print("------- Spending Summary -------")
        
        # Loop over our dictionary and print each category and its total
        for cat, total in category_totals.items():
            # The .2f formats the number so it looks like real money (2 decimal places)
            print(f"- {cat.capitalize()}: Rs. {total:.2f}")
            
        print("--------------------------------")
        print(f"Grand Total Spent: Rs. {total_spent:.2f}")

    except FileNotFoundError:
        print("Error: Could not find 'expenses.csv'. Make sure the file exists in the same folder.")

# This is a standard way in Python to say "run the main function when the script starts"
if __name__ == "__main__":
    main()
