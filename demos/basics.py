# Escape char

# str_1 = ""

# print('i am 6\'2')

# tabby_cat = "\ti\rm tabbled \r in."
# persion_cat = "i'm split \non a line"
# backslash_cat = "i'm \\ a \\ cat"
# print(tabby_cat)
# print(persion_cat)
# print(backslash_cat)

# snapshotdate= "2020-01-05"

# fat_cat = f"""
# i'll do a list:
# {snapshotdate}
# \t* cat food
# \t* fishes
# \t catnip \n\t Grass
# """

# print(fat_cat)


# Asking Questions 

# age = input("lets check the input==")


# from sys import argv
# script, username=argv
# prompt="> "
# print(f"HI {username} i am script {script}")

# print(f"Do you like me {username}")
# like= input(prompt)

# print("where do you live")
# live=input(prompt)

# print("what kind of computer you have")

# computer=input(prompt)

# print(f"HELLO {username} \
# you said said liking {like} about me \
# you live in the {live} \
# and you have {computer}  machine   \
# ")

# from sys import argv 
# scriptname , filename = argv
# txt = open(filename,w)

# print(txt.read())




# from sys import argv

# script, filename = argv

# print(f" We are going to erase {filename}")

# input(">")

# print("Opening the file")

# target = open(filename,'w')

# print("Trucating the file.  Goodbye!")

# target.truncate()

# print("now i am going to ask you three line")

# line1 = input("line 1: ")

# print("i am goint to ask you these line into the file")

# target.write(line1)
# target.close()


# from sys import argv
# from os.path import exists


# script,from_file, to_file = argv 

# print(f"copy files from {from_file} to {to_file}")


# in_file = open(from_file)

# in_data = in_file.read()

# print(f"the input data is {len(in_file)} bytes longs")

# print(f"Does output files exist {exists(to_file)}")

# out_file = open(to_file,'w')
# out_file.write(in_data)

# print("all Done")

# out_file.close
# in_file.close





# 

# def snapshot_assitance(new_msg):
#     return new_msg



# if not (True or False):
#     print("in if")
# else:
#     print("in Else")



#  List Operation 

ten_things = "Apple Oranges Crows Teliphones Light Sugar"

stuff =  ten_things.split(' ')

more_stuff= ["day", "night", "songs", "Frisbee", "Corn", "Banana", "Girls", "Boys"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print(f"adding {next_one}")
    stuff.append(next_one)
    print(f"theres are  {len(stuff)} now")


print(stuff)

# ['Apple', 'Oranges', 'Crows', 'Teliphones', 'Light', 'Sugar', 'Boys', 'Girls', 'Banana', 'Corn']

# Dictionories 


dict_stuff = {"name": "deepak" \
              ,"surname": "tiwari" \
              }

print(dict_stuff["name"])

