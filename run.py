import csv
import math
import sys
import getopt

def parsepdb():
    ncb_original_file = open("ncbd-original.pdb", "r")  # the ncbd file
    # Make key Value pair of the original file
    new_dict = dict()
    for data in ncb_original_file:
        orignal_data = data.split()
        if len(orignal_data) > 1:
                if orignal_data[2] == input:
                    new_dict[orignal_data[4]] = {
                        "x": float(orignal_data[5]),
                        "y": float(orignal_data[6]),
                        "z": float(orignal_data[7])
                    }
    # print new_dict
    return new_dict
       
def main(input,outputfile):
    residueObject = parsepdb() #parse the pdb file and make a dictionary out of it
    with open(outputfile, 'w+') as csv_output_file:  # Create an output file
        output_writer = csv.writer(csv_output_file, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        with open("merge.txt") as f:  # the source file
            reader = csv.reader(f)
            for line, in reader:
                entries = line.split()
                source = entries[0]
                destination = entries[1]
                source_axis = residueObject[source]
                dest_axis = residueObject[destination]
                print "Source "+source, " ", "Axis:", source_axis
                print "Destination "+destination, " ", "Axis:", dest_axis
                distance = math.sqrt((source_axis["x"]-dest_axis["x"])**2+(
                    source_axis["y"]-dest_axis["y"])**2+(source_axis["z"]-dest_axis["z"])**2)
                print "Distance:", distance  # distance between Source and Destination
                output_writer.writerow([source, destination, distance])
                print "Successfully written to:",outputfile


if __name__ == "__main__":

    # Check Arguments
    if len(sys.argv)<2:
        print 'Usage : run.py -i <inputAtom> -o <outputfile>'
        print 'Example : run.py -i CA -o output.csv'
        sys.exit()
    else:
        argv = sys.argv[1:]
        input = ''
        outputfile = ''
        try:
            opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        except getopt.GetoptError:
            print 'test.py -i <inputAtom> -o <outputfile>'
            print 'Example : run.py -i CA -o output.csv'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'test.py -i <inputAtom> -o <outputfile>'
                print 'Example : run.py -i CA -o output.csv'
                sys.exit()
            elif opt in ("-i", "--iatom"):
                input = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
        print 'Input Atom is "', input
        print 'Output File is "', outputfile

        main(input,outputfile) #the Main function