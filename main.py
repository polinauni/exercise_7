#Exercise 7
#1
def create_file(file_name, names):
    with open('names.txt', 'w') as f:
        names = 'Anna, Polina, Alex, Daniel, Max, Kate, Chris, Jake, Ben, Sky'
        f.write(names)

#for the 5th task

with open('nicknames.txt', 'w') as f:
    nicknames = 'Love, Sad, Angst, Cat, Happy, Lover, Pop, Trick, Doof, Omg'
    f.write(nicknames)



#2
def transform_to_row(input_file, output_file):
    with open(input_file, 'r') as f:
        contents = f.read()

        words = contents.split(',')

    with open(output_file, 'w') as f:
        for word in words:
            f.write(word.strip() + '\n')

transform_to_row("names.txt", "output.txt")

#3
def add_greeting(input_file, output_file):
    with open(input_file, 'r') as f:
        contents = f.read()

        lines = contents.split('\n')

    with open(output_file, 'w') as f:
        for line in lines:
            words = line.split()
            if words:
                words[0] = "Hello " + words[0]
                f.write(' '.join(words) + '\n')
add_greeting("output.txt", "hello_names.txt")

#4
def strip_greeting(input_file, output_file):
    with open(input_file, 'r') as f:
        contents = f.read()

        lines = contents.replace("Hello ", "").split('\n')

    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))

strip_greeting("hello_names.txt", "no_hello.txt")

#5
def combine_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.read().splitlines()
        lines2 = f2.read().splitlines()

    if len(lines1) != len(lines2):
        raise ValueError("Files have different number of lines.")

    combined_lines = [f"{line1} {line2}" for line1, line2 in zip(lines1, lines2)]

    with open(output_file, 'w') as f:
        f.write('\n'.join(combined_lines))





