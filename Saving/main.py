
halls = ["geisert", "williams", "wyckoff", "harper", "university"]
   
if __name__ == "__main__":
    my_file = open("halls.txt",'w+')
    my_file.write("\n".join(halls))
    my_file.close()
    
    with open("halls.txt") as file:
        hall_list = file.read().split("\n")
        
    print(hall_list)
