####################################################################################################
# This program generate a Box SVG pattern


def main():
    ####################################################################################################
    # constant limits for later use
    DIM_LIMIT = 2
    THIK_LIMIT = 0.1

    t = 1*4
    l = 90*4
    w = 30*4
    h = 35*4
    h3 = 30*4
    h2 = 20*4
    h1 = h - h2

    # ####################################################################################################
    # # print the user instruction
    # print("Welcome to the Square generator!")
    # print("Please follow the instruction to generate a Box shape. :) Have Fun!")
    # print("#########################################")
    # print("The card borad need to be at least 0.1\" in thickness.")
    # print("The Box needs to be at least 2\" in all dimensions.")
    # print("#########################################")

    # ####################################################################################################
    # # validate the user input
    # while True:
    #     try:
    #         # get the user input
    #         t = float(input('Enter the thickness of the card borad: '))
    #         l = float(input('Enter the length of the Box: '))
    #         w = float(input('Enter the width of the Box: '))
    #         h = float(input('Enter the height of the Box: '))
    #         h3 = float(input('Enter the front height of the Box: '))
    #     except ValueError:
    #         print(
    #             "Sorry, The parameters seems not right. Please enter valid numbers."
    #         )
    #         continue
    #     else:
    #         if l < DIM_LIMIT or w < DIM_LIMIT or h < DIM_LIMIT or h3 < DIM_LIMIT or t < THIK_LIMIT:
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
    # Boxfile.write("\t<rect x=\"-%f/2\" y=\"-%f/2\" width=\"%f\" height=\"%f\" stroke=\"black\" fill=\"none\"/>\n" % (w, h, w, h))

    # # draw a lighting pattern
    # Boxfile.write("\t<polyline points= \"100,100 150,25 150,75 200,0\" fill=\"none\" stroke=\"black\" />\n")

    # draw the box pattern
    points_List = []
    poly_points = ""

    points_List.append("{},{}".format(-w / 2 - h, -l / 2 - (w - t)))
    points_List.append("{},{}".format(-w / 2, -l / 2 - (w - t)))
    points_List.append("{},{}".format(-w / 2, -l / 2))
    points_List.append("{},{}".format(-w / 2, -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(-w / 2 + (1/3)*w, -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(-w / 2 + (1/3)*w, -l / 2 - 2 * t - h - 2 * t - (h - t) - t))
    points_List.append("{},{}".format(1/2*(1/3)*w, -l / 2 - 2 * t - h - 2 * t - (h - t) - t))
    points_List.append("{},{}".format(1/2*(1/3)*w, -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(w/2, -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(w/2, -l / 2 - t))
    points_List.append("{},{}".format(w/2, -l / 2 - t - (w-t)))
    points_List.append("{},{}".format(w/2 + h, -l / 2 - t - (w-t)))
    points_List.append("{},{}".format(w/2 + h, l/2 - h3))
    points_List.append("{},{}".format(w/2 + h - h2, l/2 + t))
    points_List.append("{},{}".format(w/2 + h - h2, l/2 + t + (w-t)))
    points_List.append("{},{}".format(w/2, l/2 + t + (w-t)))
    points_List.append("{},{}".format(w/2, l/2 + t))
    points_List.append("{},{}".format(w/2, l/2 + 2*t + h1 + 2*t + (h-t)))
    points_List.append("{},{}".format((1/3*w)/2, l/2 + 2*t + h1 + 2*t + (h-t)))
    points_List.append("{},{}".format((1/3*w)/2, l/2 + 2*t + h1 + 2*t + (h-t) + t))
    points_List.append("{},{}".format(-(1/3*w)/2, l/2 + 2*t + h1 + 2*t + (h-t) + t))
    points_List.append("{},{}".format(-(1/3*w)/2, l/2 + 2*t + h1 + 2*t + (h-t)))
    points_List.append("{},{}".format(-w/2, l/2 + 2*t + h1 + 2*t + (h-t)))
    points_List.append("{},{}".format(-w/2, l/2))
    points_List.append("{},{}".format(-w/2, l/2 + (w-t)))
    points_List.append("{},{}".format(-w/2 - h1, l/2 + (w-t)))
    points_List.append("{},{}".format(-w/2 - h1, l/2))
    points_List.append("{},{}".format(-w/2 - h, l/2 - h3))
    points_List.append("{},{}".format(-w / 2 - h, -l / 2 - (w - t)))


    for i in range(len(points_List)):
        if i < len(points_List) - 1:
            poly_points = poly_points + points_List[i] + " "
        else:
            poly_points = poly_points + points_List[i]

    print(poly_points)

    Boxfile.write("\t<polyline points= \"%s\" fill=\"none\" stroke=\"black\" />\n" %(poly_points))

    Boxfile.write("\t<line x1=\"0\" y1=\"3\" x2=\"30\" y2=\"3\" stroke=\"black\" stroke-dasharray=\"4\" />\n")



####################################################################################################
# set the program as main and write file
if __name__ == "__main__":

    with open("LaseBox_0.svg", "w") as Boxfile:

        # write the svg definition
        Boxfile.write("<svg viewBox=\"-500 -500 1000 1000\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

        # show the boundary
        Boxfile.write("\t<rect x=\"-500\" y=\"-500\" width=\"100%\" height=\"100%\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>\n")

        # main program
        main()

        # close up the file
        Boxfile.write("</svg>")

    print("File generated successfully! Check your root folder :)")