## For later use
# from LaserBox_Functions import *

####################################################################################################
# This program generate a square SVG pattern


def main():
    ####################################################################################################
    # write the svg definition
    Boxfile.write(
        "<svg viewBox=\"0 0 100 100\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"
    )

    # show the boundary
    Boxfile.write(
        "\t<rect x=\"0\" y=\"0\" width=\"100%\" height=\"100%\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>\n"
    )

    ####################################################################################################
    # print the user instruction
    print("Welcome to the Square generator!")
    print("The square needs to be at least 5\" in all dimensions.")
    print(
        "Please follow the instruction to generate a Box shape. :)  Have Fun!")
    print("#########################################")

    ####################################################################################################
    # validate the user input
    while True:
        try:
            # get the user input
            width = float(input('Enter the width of the Box: '))
            height = float(input('Enter the height of the Box: '))
        except ValueError:
            print("Sorry, I didn't understand that. Please enter a number.")
            continue
        else:
            if width < 5 or height < 5:
                print(
                    "One or Both of the numbers was/were too small. Try again. (The square needs to be at least 5\" in all dimensions.)"
                )
                continue
            else:
                print("Input Successs!")
                break

    ####################################################################################################
    # write an rectangle
    Boxfile.write(
        "\t<rect x=\"calc(50%% - %f/2)\" y=\"calc(50%% - %f/2)\" width=\"%f\" height=\"%f\" stroke=\"black\" stroke-width=\"0.25\" fill=\"none\"/>\n"
        % (width, height, width, height))

    # close up the file
    Boxfile.write("</svg>")

    print("File generated successfully! Check your root folder :)")


if __name__ == "__main__":

    with open("Square.svg", "w") as Boxfile:
        main()
