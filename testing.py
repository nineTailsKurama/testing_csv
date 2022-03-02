
import csv
import glob

'''
Compare two locations csv files and return a list of the differences.

Params:
    loc1 - location of first csv file 
    loc2 - location of second csv file
'''
def compare_each(loc1, loc2):
    # Open the csv files
    with open(loc1, 'r') as csvfile1:
        with open(loc2, 'r') as csvfile2:
            # Create a csv reader for each file
            reader1 = list(csv.reader(csvfile1))
            reader2 = list(csv.reader(csvfile2))

            reader1 = sorted(reader1[1:], key=lambda row: row[0])
            reader2 = sorted(reader2[1:], key=lambda row: row[0])
            # Create a list to store the differences
            differences = []
            # Iterate through each row of each csv file
            for row1, row2 in zip(reader1, reader2):
                # Compare each row
                if row1 != row2:
                    # Add the difference to the list
                    differences.append((row1, row2))
            # Return the list of differences
            return differences


def main(loc1, loc2):
    # Get the list of csv files
    csv_files_loc1 = sorted(glob.glob(loc1+'*.csv'))
    csv_files_loc2 = sorted(glob.glob(loc2+'*.csv'))
    # Iterate through each csv file
    for i,j in zip(csv_files_loc1, csv_files_loc2):
        # Compare the two csv files
        differences = compare_each(i, j)
        # If there are differences, print them
        if len(differences) > 0:
            print('Differences found in: ' + i + ' and ' + j)
            print(differences)
            for i in differences:
                print(i[0])
                print(i[1])
            print('\n')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Compare two locations csv files and return a list of the differences.')
    parser.add_argument('-l1', help='location of first csv file', type=str , required=True)
    parser.add_argument('-l2', help='location of second csv file', type=str , required=True)
    args = parser.parse_args()
    main(args.l1, args.l2)

