####################################################################################################
# This program generate a Box SVG pattern


def main():
    ####################################################################################################
    # constant limits (at least 1 inch in diameters and 0.00001 in thickness)
    DIM_LIMIT = 1
    THIK_LIMIT = 0.00001

    t = 0
    l = 0
    w = 0
    h = 0
    h3 = 0
    h2 = 0

    Thickness_measure = 3.0

    ####################################################################################################
    # print the user instruction
    print("Welcome to the Box generator!")
    print(
        "Please follow the instruction to generate a Box shape. :) Have Fun!")
    print("#########################################")
    print("The cardborad need to be at least >= 0\" in thickness.")
    print("The Box needs to be at least 1\" in all dimensions.")
    print("#########################################")

    ####################################################################################################
    # validate the user input
    while True:
        try:
            # get the user input
            if t < THIK_LIMIT:
                t = float(input('Enter the thickness of the cardborad (in): '))

            if t >= 3:
                thick_flag = input(
                    "Are you sure you have a cardborad with a thickness of %f in? (y/n)"
                    % t)

                if thick_flag == "y" or thick_flag == "Y":
                    pass
                else:
                    t = 0
                    continue

            if l < DIM_LIMIT:
                l = float(input('Enter the length of the Box (in): '))

            if w < DIM_LIMIT:
                w = float(input('Enter the width of the Box (in): '))

            if h < DIM_LIMIT:
                h = float(input('Enter the height of the Box (in): '))

        except ValueError:
            print(
                "Sorry, The parameters seems not right. Please enter valid numbers."
            )
            continue

        else:

            if l < DIM_LIMIT or w < DIM_LIMIT or h < DIM_LIMIT or t < THIK_LIMIT:
                print("#########################################")
                print("The following numbers were too small. Try again.")

                continue

            else:
                print("\nInput Successs!")
                print("#########################################")

                break

    slanted = input("\nDo you want to do a slanted box? (y/n): ")

    if slanted == "y" or slanted == "Y":

        # validate the chamfer parameters
        while True:

            try:

                if h3 > l or h3 <= 0:
                    h3 = float(
                        input(
                            'Enter the top chamfer length of the Box (in): '))

                if h2 > h or h2 <= 0:
                    h2 = float(
                        input(
                            'Enter the front chamfer length of the Box (in): ')
                    )

            except ValueError:
                print(
                    "Sorry, The parameters seems not right. Please enter valid numbers."
                )
                continue

            else:
                if h3 < 0 or h2 < 0:
                    print("#########################################")
                    print("The following numbers were too small. Try again.")

                    continue

                if h2 > h or h3 > l:
                    print("#########################################")
                    print("Chamfer too big. Try again.")

                    continue

                else:
                    print("\nInput Successs!")
                    print("#########################################")

                    break

    else:

        print("\nInput Successs!")
        print("#########################################")
        h3 = 0
        h2 = 0
        print()

    # record the thickness and scale the display pattern
    Thickness_measure = t

    t = t * 100
    l = l * 100
    w = w * 100
    h = h * 100
    h3 = h3 * 100
    h2 = h2 * 100
    h1 = h - h2

    thickness_to_pattern_r = t / (w + 2 * h)
    print("Adjust the width of the whole pattern to %f in on laser cutter" %
          (Thickness_measure / thickness_to_pattern_r))
    print("Adjust the width of the whole pattern to %f mm on laser cutter\n" %
          ((Thickness_measure / thickness_to_pattern_r) * 25.4))

    ####################################################################################################
    # draw the box pattern
    points_List = []
    poly_points = ""

    points_List.append("{},{}".format(-w / 2 - h, -l / 2 - (w - t)))
    points_List.append("{},{}".format(-w / 2 - t, -l / 2 - (w - t)))
    points_List.append("{},{}".format(-w / 2 - t, -l / 2 - 2 * t))
    points_List.append("{},{}".format(-w / 2, -l / 2))
    points_List.append("{},{}".format(-w / 2 - t, -l / 2 - 2 * t))
    points_List.append("{},{}".format(-w / 2 - t, -l / 2 - 2 * t - h))
    points_List.append("{},{}".format(-w / 2, -l / 2 - 2 * t - h - 2 * t))
    points_List.append("{},{}".format(-w / 2,
                                      -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(-w / 2 + (1 / 3) * w,
                                      -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(-w / 2 + (1 / 3) * w, -l / 2 - 2 * t -
                                      h - 2 * t - (h - t) - t))
    points_List.append("{},{}".format(1 / 2 * (1 / 3) * w, -l / 2 - 2 * t - h -
                                      2 * t - (h - t) - t))
    points_List.append("{},{}".format(1 / 2 * (1 / 3) * w,
                                      -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(w / 2,
                                      -l / 2 - 2 * t - h - 2 * t - (h - t)))
    points_List.append("{},{}".format(w / 2, -l / 2 - 2 * t - h - 2 * t))
    points_List.append("{},{}".format(w / 2 + t, -l / 2 - 2 * t - h))
    points_List.append("{},{}".format(w / 2 + t, -l / 2 - 2 * t))
    points_List.append("{},{}".format(w / 2, -l / 2 - t))
    points_List.append("{},{}".format(w / 2 + t, -l / 2 - 2 * t))
    points_List.append("{},{}".format(w / 2 + t, -l / 2 - t - (w - t)))
    points_List.append("{},{}".format(w / 2 + h, -l / 2 - t - (w - t)))
    points_List.append("{},{}".format(w / 2 + h, l / 2 - h3))
    points_List.append("{},{}".format(w / 2 + h - h2, l / 2 + t))
    points_List.append("{},{}".format(w / 2 + h - h2, l / 2 + t + (w - t)))
    points_List.append("{},{}".format(w / 2 + t, l / 2 + t + (w - t)))
    points_List.append("{},{}".format(w / 2 + t, l / 2 + 2 * t))
    points_List.append("{},{}".format(w / 2, l / 2 + t))
    points_List.append("{},{}".format(w / 2 + t, l / 2 + 2 * t))
    points_List.append("{},{}".format(w / 2 + t, l / 2 + 2 * t + h1))
    points_List.append("{},{}".format(w / 2, l / 2 + 2 * t + h1 + 2 * t))
    points_List.append("{},{}".format(w / 2,
                                      l / 2 + 2 * t + h1 + 2 * t + (h1 - t)))
    points_List.append("{},{}".format((1 / 3 * w) / 2,
                                      l / 2 + 2 * t + h1 + 2 * t + (h1 - t)))
    points_List.append("{},{}".format(
        (1 / 3 * w) / 2, l / 2 + 2 * t + h1 + 2 * t + (h1 - t) + t))
    points_List.append("{},{}".format(
        -(1 / 3 * w) / 2, l / 2 + 2 * t + h1 + 2 * t + (h1 - t) + t))
    points_List.append("{},{}".format(-(1 / 3 * w) / 2,
                                      l / 2 + 2 * t + h1 + 2 * t + (h1 - t)))
    points_List.append("{},{}".format(-w / 2,
                                      l / 2 + 2 * t + h1 + 2 * t + (h1 - t)))
    points_List.append("{},{}".format(-w / 2, l / 2 + 2 * t + h1 + 2 * t))
    points_List.append("{},{}".format(-w / 2 - t, l / 2 + 2 * t + h1))
    points_List.append("{},{}".format(-w / 2 - t, l / 2 + 2 * t))
    points_List.append("{},{}".format(-w / 2, l / 2))
    points_List.append("{},{}".format(-w / 2 - t, l / 2 + 2 * t))
    points_List.append("{},{}".format(-w / 2 - t, l / 2 + (w - t)))
    points_List.append("{},{}".format(-w / 2 - h1, l / 2 + (w - t)))
    points_List.append("{},{}".format(-w / 2 - h1, l / 2))
    points_List.append("{},{}".format(-w / 2 - h, l / 2 - h3))
    points_List.append("{},{}".format(-w / 2 - h, -l / 2 - (w - t)))

    for i in range(len(points_List)):
        if i < len(points_List) - 1:
            poly_points = poly_points + points_List[i] + " "
        else:
            poly_points = poly_points + points_List[i]

    Boxfile.write(
        "\t<polyline points= \"%s\" fill=\"none\" stroke=\"black\"/>\n" %
        (poly_points))

    ####################################################################################################
    # draw dash lines
    dash_list = []

    dash_list.append((-w / 2, -l / 2 - 2 * t - h - 2 * t, w / 2,
                      -l / 2 - 2 * t - h - 2 * t))
    dash_list.append((-w / 2, -l / 2 - 2 * t - h, w / 2, -l / 2 - 2 * t - h))
    dash_list.append((-w / 2, -l / 2 - 2 * t, w / 2, -l / 2 - 2 * t))

    dash_list.append((-w / 2, l / 2 + 2 * t + h1 + 2 * t, w / 2,
                      l / 2 + 2 * t + h1 + 2 * t))
    dash_list.append((-w / 2, l / 2 + 2 * t + h1, w / 2, l / 2 + 2 * t + h1))
    dash_list.append((-w / 2, l / 2 + 2 * t, w / 2, l / 2 + 2 * t))

    dash_list.append((-w / 2, -l / 2, -w / 2 - h, -l / 2))
    dash_list.append((-w / 2, l / 2, -w / 2 - h1, l / 2))

    dash_list.append((w / 2, -l / 2 - t, w / 2 + h, -l / 2 - t))
    dash_list.append((w / 2, l / 2 + t, w / 2 + h1, l / 2 + t))

    dash_list.append((-w / 2, -l / 2, -w / 2, l / 2))
    dash_list.append((w / 2, -l / 2 - t, w / 2, l / 2 + t))

    for dashline_loc in dash_list:
        Boxfile.write(
            "\t<line x1=\"%s\" y1=\"%s\" x2=\"%s\" y2=\"%s\" stroke=\"black\" stroke-dasharray=\"11\"/>\n"
            % (dashline_loc))

    ####################################################################################################
    # draw the lockers
    Boxfile.write(
        "\t<rect x=\"%f\" y=\"%f\" width=\"%f\" height=\"%f\" stroke=\"black\" fill=\"none\"/>\n"
        % (-(1 / 3 * w) / 2, -l / 2, w / 3, t))
    Boxfile.write(
        "\t<rect x=\"%f\" y=\"%f\" width=\"%f\" height=\"%f\" stroke=\"black\" fill=\"none\"/>\n"
        % (-(1 / 3 * w) / 2, l / 2 - t, w / 3, t))

    ####################################################################################################
    # draw the text
    UserText = "Digital Manufacturing"
    Text_size = 2 * t
    Text_loc = -l / 2 - 2 * Text_size
    Boxfile.write(
        "\t<text x=\"0\" y=\"%f\" transform=\"rotate(180, 0, 0)\"   style=\"fill: none; stroke: black;  font-size: %fpx;\" text-anchor=\"middle\">%s</text>\n"
        % (Text_loc, Text_size, UserText))

    # User defined text
    UserText_flag = input(
        "Do you want to custom some text on the top of the box? (y/n): ")

    if UserText_flag == 'y' or UserText_flag == 'Y':
        # UserText = input("Please type your custom text: ")
        UserText = ("Yachao Liu (yl4269)")
        Text_loc_top = l / 2 + 2 * t + h + 2 * t + 50
        Boxfile.write(
            "\t<text x=\"0\" y=\"%f\" transform=\"rotate(180, 0, 0)\"   style=\"fill: none; stroke: black;  font-size: %fpx;\" text-anchor=\"middle\">%s</text>\n"
            % (Text_loc_top, Text_size, UserText))
    else:
        pass

    # User defined text
    UserText_flag = input(
        "Do you want to custom some text on the front of the box? (y/n): ")

    if UserText_flag == 'y' or UserText_flag == 'Y':
        # UserText = input("Please type your custom text: ")
        UserText = ("Chong Liu (cl3896)")
        Text_loc_front = -l / 2 - h1 - 2 * t + Text_size + 10
        Boxfile.write(
            "\t<text x=\"0\" y=\"%f\" transform=\"rotate(180, 0, 0)\"   style=\"fill: none; stroke: black;  font-size: %fpx;\" text-anchor=\"middle\">%s</text>\n"
            % (Text_loc_front, Text_size, UserText))
    else:
        pass

    ####################################################################################################
    # draw the logo
    if w > h1:
        logo_size = 1 / 2.0 * h1
    else:
        logo_size = 1 / 2.0 * w

    logo_yloc = Text_loc - 2 * t

    with open("logo.svg", "r") as Logofile:

        Boxfile.write(
            "\t<g transform=\"translate(%f %f) rotate(180 0 0) scale(%f, %f)\" fill=\"#000000\" stroke=\"none\">\n"
            % (1 / 2.0 * logo_size, -logo_yloc, logo_size * 0.00008,
               -logo_size * 0.00008))

        copy_flag = False

        for line in Logofile:

            if line[:5] == "<path":
                copy_flag = True

            if line[:4] == "</g>":
                copy_flag = False

            if copy_flag == True:
                Boxfile.write("\t\t" + line)

        Boxfile.write("\t</g>\n")

    ####################################################################################################
    # draw the fractal pattern
    drawCircle(w / 2 + h / 2 + t, -h / 5, h / 4, "r")
    drawCircle(-(w / 2 + h / 2 + t), -h / 5, h / 4, "l")

    # ####################################################################################################
    # draw the fractal tree branch

    Tree_flag = input(
        "Do you want to promise to save more trees by sign a tree at the buttom of your box? (y/n): "
    )

    if Tree_flag == "y" or Tree_flag == "Y":
        root_loc = 0
        root_len = 80

        Boxfile.write(
            "\t<g id=\"branch\"> <line x1=\"0\" y1=\"%f\" x2=\"0\" y2=\"%f\" stroke=\"black\"/> </g>\n"
            % (root_loc, root_loc - root_len))

        Boxfile.write("\t<g id=\"%f\"><use xlink:href=\"#branch\"/></g>\n" % 0)

        for i in range(1, 5):

            Boxfile.write(
                "\t<g id=\"%f\"> <use xlink:href=\"#%f\" transform=\"translate(0, -80) rotate(-35) scale(.7)\"/> <use xlink:href=\"#%f\" transform=\"translate(0, -40) rotate(+35) scale(.7)\"/> <use xlink:href=\"#branch\"/></g>\n"
                % (i, i - 1, i - 1))


# fractal function
def drawCircle(x, y, d, f):

    Boxfile.write(
        "\t<circle cx=\"%f\" cy=\"%f\" r=\"%f\" stroke=\"black\" fill=\"none\"/>\n"
        % (x, y, d))

    if d > 15 and f == "r":
        drawCircle(x - d, y, d / 2, "r")
        drawCircle(x, y - d, d / 2, "r")
        drawCircle(x, y + d, d / 2, "r")

    elif d > 15 and f == "l":
        drawCircle(x + d, y, d / 2, "l")
        drawCircle(x, y - d, d / 2, "l")
        drawCircle(x, y + d, d / 2, "l")


####################################################################################################
# set the program as main and write file
if __name__ == "__main__":

    with open("LaserBox1.svg", "w") as Boxfile:

        # write the svg definition
        Boxfile.write(
            "<svg viewBox=\"-1000 -1000 2000 2000\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"
        )

        # # show the boundary
        # Boxfile.write("\t<rect x=\"-500\" y=\"-500\" width=\"100%\" height=\"100%\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>\n")

        # main program
        main()

        # close up the file
        Boxfile.write("</svg>")

    print("#########################################")
    print("\nFile generated successfully! Check your root folder :)")
