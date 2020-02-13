####################################################################################################
# This program generate a Box SVG pattern

def main():
    ####################################################################################################
    # constant limits for later use
    DIM_LIMIT = 5
    THIK_LIMIT = 0.1

    t = 0.3
    l = 6
    w = 4
    h = 3
    h3 = 2
    h2 = 1
    h1 = h - h2

    t = t*100
    l = l*100
    w = w*100
    h = h*100
    h3 = h3*100
    h2 = h2*100
    h1 = h1*100

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
    #         if t < THIK_LIMIT:
    #             t = float(input('Enter the thickness of the card borad: '))

    #         if l < DIM_LIMIT:
    #             l = float(input('Enter the length of the Box: '))

    #         if w < DIM_LIMIT:
    #             w = float(input('Enter the width of the Box: '))

    #         if h < DIM_LIMIT:
    #             h = float(input('Enter the height of the Box: '))

    #         if h3 > l or h3 < DIM_LIMIT:
    #             h3 = float(input('Enter the top chamfer length of the Box: '))

    #         if h2 > h or h2 < DIM_LIMIT:
    #             h2 = float(input('Enter the front chamfer length of the Box: '))

    #         h1 = h - h2

    #     except ValueError:
    #         print("Sorry, The parameters seems not right. Please enter valid numbers.")
    #         continue

    #     else:
    #         if l < DIM_LIMIT or w < DIM_LIMIT or h < DIM_LIMIT or t < THIK_LIMIT or h3 < DIM_LIMIT or h2 < DIM_LIMIT:
    #             print("The following numbers were too small. Try again.")
    #             print("#########################################")
    #             continue
    #         if h2 > h or h3 > l:
    #             print("Chamfer too big. Try again.")
    #             print("#########################################")
    #             continue
    #         else:
    #             print("Input Successs!")
    #             print("#########################################")
    #             break

    ####################################################################################################
    # draw the box pattern
    points_List = []
    poly_points = ""

    points_List.append("{},{}".format(-w / 2 - h, -l / 2 - (w - t)))
    points_List.append("{},{}".format(-w / 2 - t, -l / 2 - (w - t)))
    points_List.append("{},{}".format(-w / 2 - t, -l / 2 - 2*t))
    points_List.append("{},{}".format(-w / 2, -l / 2))
    points_List.append("{},{}".format(-w / 2 - t, -l / 2 - 2*t))
    points_List.append("{},{}".format(-w / 2-t, -l / 2 - 2*t - h))
    points_List.append("{},{}".format(-w / 2, -l / 2 - 2*t - h - 2*t))
    
    points_List.append("{},{}".format(-w / 2, -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(-w / 2 + (1/3)*w, -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(-w / 2 + (1/3)*w, -l / 2 - 2 * t - h - 2 * t - (h - t) - t))
    points_List.append("{},{}".format(1/2*(1/3)*w, -l / 2 - 2 * t - h - 2 * t - (h - t) - t))
    points_List.append("{},{}".format(1/2*(1/3)*w, -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(w/2, -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(w/2, -l / 2 - 2 * t - h - 2 * t))
    points_List.append("{},{}".format(w/2 + t, -l / 2 - 2 * t - h))
    points_List.append("{},{}".format(w/2 + t, -l / 2 - 2 * t))
    
    points_List.append("{},{}".format(w/2, -l / 2 - t))
    points_List.append("{},{}".format(w/2 + t, -l / 2 - 2 * t))
    points_List.append("{},{}".format(w/2 + t, -l / 2 - t - (w-t)))
    points_List.append("{},{}".format(w/2 + h, -l / 2 - t - (w-t)))
    points_List.append("{},{}".format(w/2 + h, l/2 - h3))
    points_List.append("{},{}".format(w/2 + h - h2, l/2 + t))
    points_List.append("{},{}".format(w/2 + h - h2, l/2 + t + (w-t)))
    points_List.append("{},{}".format(w/2 + t, l/2 + t + (w-t)))
    points_List.append("{},{}".format(w/2 + t, l/2 + 2*t))
    points_List.append("{},{}".format(w/2, l/2 + t))
    points_List.append("{},{}".format(w/2 + t, l/2 + 2*t))
    points_List.append("{},{}".format(w/2 + t, l/2 + 2*t + h1))
    points_List.append("{},{}".format(w/2, l/2 + 2*t + h1 + 2*t))

    points_List.append("{},{}".format(w/2, l/2 + 2*t + h1 + 2*t + (h1-t)))
    points_List.append("{},{}".format((1/3*w)/2, l/2 + 2*t + h1 + 2*t + (h1-t)))
    points_List.append("{},{}".format((1/3*w)/2, l/2 + 2*t + h1 + 2*t + (h1-t) + t))
    points_List.append("{},{}".format(-(1/3*w)/2, l/2 + 2*t + h1 + 2*t + (h1-t) + t))
    points_List.append("{},{}".format(-(1/3*w)/2, l/2 + 2*t + h1 + 2*t + (h1-t)))
    points_List.append("{},{}".format(-w/2, l/2 + 2*t + h1 + 2*t + (h1-t)))
    points_List.append("{},{}".format(-w/2, l/2 + 2*t + h1 + 2*t))
    points_List.append("{},{}".format(-w/2-t, l/2 + 2*t + h1))
    points_List.append("{},{}".format(-w/2-t, l/2 + 2*t))
    points_List.append("{},{}".format(-w/2, l/2))
    points_List.append("{},{}".format(-w/2-t, l/2 + 2*t))

    points_List.append("{},{}".format(-w/2 - t, l/2 + (w-t)))
    points_List.append("{},{}".format(-w/2 - h1, l/2 + (w-t)))
    points_List.append("{},{}".format(-w/2 - h1, l/2))
    points_List.append("{},{}".format(-w/2 - h, l/2 - h3))
    points_List.append("{},{}".format(-w / 2 - h, -l / 2 - (w - t)))


    for i in range(len(points_List)):
        if i < len(points_List) - 1:
            poly_points = poly_points + points_List[i] + " "
        else:
            poly_points = poly_points + points_List[i]

    Boxfile.write("\t<polyline points= \"%s\" fill=\"none\" stroke=\"black\"/>\n" %(poly_points))


    ####################################################################################################
    # draw dash lines
    dash_list = []

    dash_list.append((-w/2, -l/2 - 2*t - h - 2*t, w/2, -l/2 - 2*t - h - 2*t))
    dash_list.append((-w/2, -l/2 - 2*t - h, w/2, -l/2 - 2*t - h))
    dash_list.append((-w/2, -l/2 - 2*t, w/2, -l/2 - 2*t))

    dash_list.append((-w/2, l/2 + 2*t + h1 + 2*t, w/2, l/2 + 2*t + h1 + 2*t))
    dash_list.append((-w/2, l/2 + 2*t + h1, w/2, l/2 + 2*t + h1))
    dash_list.append((-w/2, l/2 + 2*t, w/2, l/2 + 2*t))

    dash_list.append((-w/2, -l/2, -w/2 - h, -l/2))
    dash_list.append((-w/2, l/2, -w/2 - h1, l/2))

    dash_list.append((w/2, -l/2 - t, w/2 + h, -l/2 - t))
    dash_list.append((w/2, l/2 + t, w/2 + h1, l/2 + t))

    dash_list.append((-w/2, -l/2, -w/2, l/2))
    dash_list.append((w/2, -l/2 - t, w/2, l/2 + t))

    for dashline_loc in dash_list:
        Boxfile.write("\t<line x1=\"%s\" y1=\"%s\" x2=\"%s\" y2=\"%s\" stroke=\"black\" stroke-dasharray=\"11\"/>\n" % (dashline_loc))


    ####################################################################################################
    # draw the lockers
    Boxfile.write("\t<rect x=\"%f\" y=\"%f\" width=\"%f\" height=\"%f\" stroke=\"black\" fill=\"none\"/>\n" % (-(1/3*w)/2, -l/2, w/3, t))
    Boxfile.write("\t<rect x=\"%f\" y=\"%f\" width=\"%f\" height=\"%f\" stroke=\"black\" fill=\"none\"/>\n" % (-(1/3*w)/2, l/2 - t, w/3, t))


    ####################################################################################################
    # draw the text
    UserText = "Digital Manufacturing"
    Text_size = t
    Text_loc = -l/2-3*Text_size
    Boxfile.write("\t<text x=\"0\" y=\"%f\" transform=\"rotate(180, 0, 0)\"   style=\"fill: none; stroke: black;  font-size: %fpx;\" text-anchor=\"middle\">%s</text>\n" % (Text_loc, Text_size, UserText))

    # # User defined text
    # UserText_flag = input("Do you want to custome some text on the top of the box? (y/n): ")

    # if UserText_flag == 'y' or UserText_flag == 'Y':
    #     UserText = input("Please type your custom text: ")
    #     Text_loc_top = l/2 + 2*t + h + 2*t + 50
    #     Boxfile.write("\t<text x=\"0\" y=\"%f\" transform=\"rotate(180, 0, 0)\"   style=\"fill: none; stroke: black;  font-size: %fpx;\" text-anchor=\"middle\">%s</text>\n" % (Text_loc_top, Text_size, UserText))
    # else:
    #     pass

    # # User defined text
    # UserText_flag = input("Do you want to custome some text on the front of the box? (y/n): ")

    # if UserText_flag == 'y' or UserText_flag == 'Y':
    #     UserText = input("Please type your custom text: ")
    #     Text_loc_front = -l/2 - h1 + 10
    #     Boxfile.write("\t<text x=\"0\" y=\"%f\" transform=\"rotate(180, 0, 0)\"   style=\"fill: none; stroke: black;  font-size: %fpx;\" text-anchor=\"middle\">%s</text>\n" % (Text_loc_front, Text_size, UserText))
    # else:
    #     pass


    ####################################################################################################
    # draw the logo
    if w > h1:
        logo_size = 1/2*h1
    else:
        logo_size = 1/2*w
    
    logo_xloc = -1/2*logo_size
    logo_yloc = Text_loc - logo_size - Text_size

    url = "logo.svg"
    Boxfile.write("\t<image href=\"%s\" x=\"%f\" y=\"%f\" transform=\"rotate(180 0 0)\" height=\"%f\" width=\"%F\"/>\n" % (url, logo_xloc, logo_yloc, logo_size, logo_size))


    ####################################################################################################
    # draw the fractal pattern
    drawCircle(w/2+h/2+t, -h/3, h/4)

    ####################################################################################################
    # how to draw the curves



# fractal function
def drawCircle(x, y, d):

    Boxfile.write("\t<circle cx=\"%f\" cy=\"%f\" r=\"%f\" stroke=\"black\" text-anchor=\"middle\" fill=\"none\"/>\n" %(x, y, d))

    if d > 15:
        drawCircle(x-d, y, d/2)
        drawCircle(x, y-d, d/2)
        drawCircle(x, y+d, d/2)



####################################################################################################
# set the program as main and write file
if __name__ == "__main__":

    with open("LaserBox.svg", "w") as Boxfile:

        # write the svg definition
        Boxfile.write("<svg viewBox=\"-1000 -1000 2000 2000\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

        # # show the boundary
        # Boxfile.write("\t<rect x=\"-500\" y=\"-500\" width=\"100%\" height=\"100%\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>\n")

        # main program
        main()

        # close up the file
        Boxfile.write("</svg>")

    print("File generated successfully! Check your root folder :)")