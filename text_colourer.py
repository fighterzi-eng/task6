#g is green,r is red,y is yellow


def colouring(colour,letter):
    match colour:
        case "r":
            x="\033[31m"+letter+"\033[0m"
            return x



        case "y":
            x="\033[33m"+letter+"\033[0m"
            return x


        case "g":
            x="\033[32m"+letter+"\033[0m"
            return x
