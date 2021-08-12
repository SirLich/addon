import glob

def main():
    for file in glob.glob("BP/features/**"):
        print(file)

main()