# PROGRAMMING 2022 ASSIGNMENT 5
# Author: Rebecca Hinrichs
# 4 August 2022

# PROGRAMMING STATEMENT:
# The attached file P22-HW5-Input.txt contains a long list of random numbers.
# Write a program that opens the file, reads all numbers from the file, and calculates the following:
# (a) The number of numbers in the file
# (b) The largest and the smallest number
# (c) The sum of all the numbers in the file
# (d) The average of all the numbers in the file
# Write the results to a new file P22-HW5-Output.txt, following the conditions below:
#   - You must write Functions and Lists for parts (a) through (d).
#   - Do not use the built-in functions in Python.


# Main Function Definition
def main():
    numbers = []    # List to store numbers
    
    try:
        # Open the files
        infile = open('P22-HW5-Input.txt', 'r')
        outfile = open('P22-HW5-Output.txt', 'w')
        
        # Process Each Line
        for line in infile:
            numbers.append(int(line))
            
        # Close the input file
        infile.close()
        
        # Output the results
        outfile.writelines('<------- PROGRAMMING 2022 ASSIGNMENT 5: Output Results ------>' + '\n\n')
        outfile.writelines('<----------------- Author: Rebecca Hinrichs ----------------->' + '\n\n')
        outfile.writelines('The quantity of numbers is:  ' + str(num_numbers(numbers)))
        outfile.writelines('\n\n')
        outfile.writelines('The maximum number is:  ' + str(max_min_numbers(numbers)[0]))
        outfile.writelines('\n\n')
        outfile.writelines('The minimum number is:  ' + str(max_min_numbers(numbers)[1]))
        outfile.writelines('\n\n')
        outfile.writelines('The total of the numbers is:  ' + str(sum_numbers(numbers)))
        outfile.writelines('\n\n')
        outfile.writelines('The average of the numbers is:  ' + str(avg_numbers(numbers)))
        outfile.writelines('\n\n')
        
        # Close the output file
        outfile.close()
                
    except IOError:
        print('There was an error reading the file.')
    
    except ValueError:
        print('The file contains non-numeric data.')
        
    except:
        print('Who knows what happened, but I can\'t read that...')           

    
# Function: Part A
def num_numbers(num_list):
    count = 0    # Accumulator len()
    
    for i in num_list:
        count += 1
        
    return count

# Function: Part B
def max_min_numbers(num_list):
    max_min_list = []    # To hold MAX, MIN
    max_num = 0    # Max variable
    min_num = 100    # Min variable
    
    for i in num_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    
    max_min_list.append(max_num)
    max_min_list.append(min_num)
            
    return max_min_list

# Function: Part C
def sum_numbers(num_list):
    total = 0    # Accumulator sum()
    
    for i in num_list:
        total += i
        
    return total

# Function: Part D
def avg_numbers(num_list):
    
    # Average = total value / count of inputs
    return sum_numbers(num_list)/num_numbers(num_list)


# Run Program
main()