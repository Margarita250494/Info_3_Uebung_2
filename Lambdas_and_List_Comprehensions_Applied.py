import os  # Importing the os module for interacting with the file system
import hashlib  # Importing hashlib for creating MD5 hash values of files


class Duplicate_Finder:
    def __init__(self):
        # Initializing the instance variables
        self.hashes = {}  # Dictionary to store the file sizes, hashes and paths
        self.duplicates = []  # List to store the duplicate files found

    def find_duplicates(self, directory):
        # Method to find duplicate files in a given directory
        # os.walk is used to iterate over all files and sub-directories within the given directory
        for root, dirs, files in os.walk(directory):
            # Iterating over all files in the current directory
            for filename in files:
                # Joining the current filename with the current directory path
                file_path = os.path.join(root, filename)
                # Checking if the joined path is a file or not
                if os.path.isfile(file_path):
                    # Getting the size, basename and extension of the current file
                    file_size = os.path.getsize(file_path)
                    file_basename, file_ext = os.path.splitext(filename)
                    # Checking if a file with the same size already exists in the hashes dictionary
                    if file_size in self.hashes:
                        # Checking if the current file has the same hash and extension as the file already in the dictionary
                        if self.hashes[file_size][0] == self.get_md5_hash(file_path) and self.hashes[file_size][
                            1] == file_ext:
                            # If the file is a duplicate, add it to the duplicates list and print a message
                            print(f"{file_basename} is a duplicate of {os.path.basename(self.hashes[file_size][2])}")
                            self.duplicates.append(file_path)
                    else:
                        # If the file size is not in the hashes dictionary, add it with the hash and path information
                        self.hashes[file_size] = (self.get_md5_hash(file_path), file_ext, file_path)

        if len(self.duplicates) <= 0:
            # If no duplicates are found, print a message
            print("No duplicate files found.")
        else:
            # If duplicates are found, print a message and the list of duplicates
            print("Duplicate files found:")
            for filename in self.duplicates:
                print(os.path.basename(filename))

    def get_md5_hash(self, filename):
        # Method to calculate the MD5 hash of a given file
        with open(filename, "rb") as f:
            data = f.read()
            return hashlib.md5(data).hexdigest()


if __name__ == '__main__':
    # Creating an instance of the DuplicateFinder class and calling the find_duplicates method
    duplicate_finder = Duplicate_Finder()
    duplicate_finder.find_duplicates('/Users/margaritaboiko/Desktop/Info_3/Übung_2/Übung_2/Part_3/Files')
