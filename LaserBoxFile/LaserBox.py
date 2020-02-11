####################################################################################################
# This program generate a Box SVG pattern


def main():
    ####################################################################################################
    # constants for later use
    DIM_LIMIT = 2
    THIK_LIMIT = 0.1

    ####################################################################################################
    # print the user instruction
    print("Welcome to the Square generator!")
    print(
        "Please follow the instruction to generate a Box shape. :) Have Fun!")
    print("#########################################")
    print("The card borad need to be at least 0.1\" in thickness.")
    print("The Box needs to be at least 2\" in all dimensions.")
    print("#########################################")

    ####################################################################################################
    # validate the user input
    while True:
        try:
            # get the user input
            thickness = float(input('Enter the thickness of the card borad: '))
            length = float(input('Enter the length of the Box: '))
            width = float(input('Enter the width of the Box: '))
            height = float(input('Enter the height of the Box: '))
        except ValueError:
            print(
                "Sorry, The parameters seems not right. Please enter valid numbers."
            )
            continue
        else:
            if width < DIM_LIMIT or height < DIM_LIMIT or height < DIM_LIMIT or thickness < THIK_LIMIT:
                print(
                    "One or Both of the numbers was/were too small. Try again."
                )
                continue
            else:
                print("Input Successs!")
                print("#########################################")
                break

    ####################################################################################################
    # write an rectangle
    Boxfile.write(
        "\t<rect x=\"calc(50%% - %f/2)\" y=\"calc(50%% - %f/2)\" width=\"%f\" height=\"%f\" stroke=\"black\" fill=\"none\"/>\n"
        % (width, height, width, height))

    # draw the box pattern
    Boxfile.write(
        "<polyline points= \"100,100 150,25 150,75 200,0\" fill=\"none\" stroke=\"black\" />\n"
    )


####################################################################################################
# set the program as main and write file
if __name__ == "__main__":

    with open("LaseBox_0.svg", "w") as Boxfile:

        # write the svg definition
        Boxfile.write(
            "<svg viewBox=\"0 0 1000 1000\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"
        )

        # show the boundary
        Boxfile.write(
            "\t<rect x=\"0\" y=\"0\" width=\"100%\" height=\"100%\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>\n"
        )

        # main program
        main()

        # close up the file
        Boxfile.write("</svg>")

    print("File generated successfully! Check your root folder :)")