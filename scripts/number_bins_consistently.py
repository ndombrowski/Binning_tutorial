import os
import sys

def usage():
    print("Usage: number_bins_consistently.py directory_name")
    print("This script will rename all .fna files in the specified directory to have a consistent numbering format (e.g. NIOZ118_mb_b001.fna).")
    print("Beware that the script was designed with the following name in mind: NIOZ118_mb_b1.fna ")
if len(sys.argv) != 2:
    usage()
    sys.exit(1)

directory = sys.argv[1]

if not os.path.isdir(directory):
    print("Error: %s is not a directory" % directory)
    usage()
    sys.exit(1)

for filename in os.listdir(directory):
    if filename.endswith(".fna"):
        parts = filename.split("_")
        num_parts = parts[-1].split(".")
        num = num_parts[0]
        num_prefix = ""
        num_suffix = ""
        if num[0].isalpha():
            num_prefix = num[0]
            num = num[1:]
        if len(num_parts) > 1:
            num_suffix = "." + num_parts[1]
        new_num = num.zfill(3)
        new_name = "_".join(parts[:-1]) + "_" + num_prefix + new_num + num_suffix + ".fna"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

