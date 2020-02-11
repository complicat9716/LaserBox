####################################################################################################
# This program generate a Box SVG pattern


def main():
    ####################################################################################################
    # constant limits for later use
    DIM_LIMIT = 2
    THIK_LIMIT = 0.1

    t = 20
    l = 600
    w = 200
    h = 400
    h1 = 100

    ####################################################################################################
    # print the user instruction
    print("Welcome to the Square generator!")
    print(
        "Please follow the instruction to generate a Box shape. :) Have Fun!")
    print("#########################################")
    print("The card borad need to be at least 0.1\" in thickness.")
    print("The Box needs to be at least 2\" in all dimensions.")
    print("#########################################")

    # ####################################################################################################
    # # validate the user input
    # while True:
    #     try:
    #         # get the user input
    #         t = float(input('Enter the thickness of the card borad: '))
    #         l = float(input('Enter the length of the Box: '))
    #         w = float(input('Enter the width of the Box: '))
    #         h = float(input('Enter the height of the Box: '))
    #         h1 = float(input('Enter the front height of the Box: '))
    #     except ValueError:
    #         print(
    #             "Sorry, The parameters seems not right. Please enter valid numbers."
    #         )
    #         continue
    #     else:
    #         if l < DIM_LIMIT or w < DIM_LIMIT or h < DIM_LIMIT or h1 < DIM_LIMIT or t < THIK_LIMIT:
    #             print(
    #                 "One or Both of the numbers was/were too small. Try again."
    #             )
    #             continue
    #         else:
    #             print("Input Successs!")
    #             print("#########################################")
    #             break

    ####################################################################################################
    # write an rectangle
    Boxfile.write(
        "\t<rect x=\"-%f/2\" y=\"-%f/2\" width=\"%f\" height=\"%f\" stroke=\"black\" fill=\"none\"/>\n"
        % (w, h, w, h))

    # draw a lighting pattern
    Boxfile.write(
        "\t<polyline points= \"100,100 150,25 150,75 200,0\" fill=\"none\" stroke=\"black\" />\n"
    )

    # draw the box pattern
    points_List = []
    poly_points = ""

    points_List.append("{},{}".format(w, h))
    points_List.append("{},{}".format(w, h))

    for i in range(len(points_List)):
        if i < len(points_List) - 1:
            poly_points = poly_points + points_List[i] + " "
        else:
            poly_points = poly_points + points_List[i]

    print(poly_points)

    # Boxfile.write("\t<polyline points= \"%s\" fill=\"none\" stroke=\"black\" />\n" %(poly_points))


####################################################################################################
# set the program as main and write file
if __name__ == "__main__":

    with open("LaseBox_0.svg", "w") as Boxfile:

        # write the svg definition
        Boxfile.write(
            "<svg viewBox=\"-500 -500 1000 1000\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"
        )

        # show the boundary
        Boxfile.write(
            "\t<rect x=\"-500\" y=\"-500\" width=\"100%\" height=\"100%\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>\n"
        )

        # main program
        main()

        # close up the file
        Boxfile.write("</svg>")

    print("File generated successfully! Check your root folder :)")