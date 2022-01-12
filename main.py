def A(buf):
    buf[0] = buf[0] + "        #         "
    buf[1] = buf[1] + "       # #        "
    buf[2] = buf[2] + "      #   #       "
    buf[3] = buf[3] + "     #     #      "
    buf[4] = buf[4] + "    #       #     "
    buf[5] = buf[5] + "   #         #    "
    buf[6] = buf[6] + "  #############   "
    buf[7] = buf[7] + " #             #  "
    buf[8] = buf[8] + "#               # "

def S(buf):
    buf[0] = buf[0] + "      ############"
    buf[1] = buf[1] + "    ##            "
    buf[2] = buf[2] + "   ##             "
    buf[3] = buf[3] + "    ##            "
    buf[4] = buf[4] + "    ##########    "
    buf[5] = buf[5] + "             ##   "
    buf[6] = buf[6] + "              ##  "
    buf[7] = buf[7] + "            ##    "
    buf[8] = buf[8] + "#############     "
    
def R(buf):
    buf[0] = buf[0] + "##########        "
    buf[1] = buf[1] + "##       ##       "
    buf[2] = buf[2] + "##        ##      "
    buf[3] = buf[3] + "##        ##      "
    buf[4] = buf[4] + "###########       "
    buf[5] = buf[5] + "##        ##      "
    buf[6] = buf[6] + "##         ##     "
    buf[7] = buf[7] + "##          ##    "
    buf[8] = buf[8] + "##           ##   "

def I(buf):
    buf[0] = buf[0] + "        #         "
    buf[1] = buf[1] + "        #         "
    buf[2] = buf[2] + "        #         "
    buf[3] = buf[3] + "        #         "
    buf[4] = buf[4] + "        #         "
    buf[5] = buf[5] + "        #         "
    buf[6] = buf[6] + "        #         "
    buf[7] = buf[7] + "        #         "
    buf[8] = buf[8] + "        #         "

def B(buf):
    buf[0] = buf[0] + "    ########      "
    buf[1] = buf[1] + "    #       #     "
    buf[2] = buf[2] + "    #        #    "
    buf[3] = buf[3] + "    #       #     "
    buf[4] = buf[4] + "    #######       "
    buf[5] = buf[5] + "    #       #     "
    buf[6] = buf[6] + "    #        #    "
    buf[7] = buf[7] + "    #       #     "
    buf[8] = buf[8] + "    ########      "

def J(buf):
    buf[0] = buf[0] + "        #         "
    buf[1] = buf[1] + "        #         "
    buf[2] = buf[2] + "        #         "
    buf[3] = buf[3] + "        #         "
    buf[4] = buf[4] + "        #         "
    buf[5] = buf[5] + "        #         "
    buf[6] = buf[6] + "        #         "
    buf[7] = buf[7] + "  #     #         "
    buf[8] = buf[8] + "  # # # #         "

def K(buf):
    buf[0] = buf[0] + "   #            # "
    buf[1] = buf[1] + "   #          #   "
    buf[2] = buf[2] + "   #        #     "
    buf[3] = buf[3] + "   #      #       "
    buf[4] = buf[4] + "   # # # #        "
    buf[5] = buf[5] + "   #       #      "
    buf[6] = buf[6] + "   #         #    "
    buf[7] = buf[7] + "   #           #  "
    buf[8] = buf[8] + "   #             #"


def K(buf):
    buf[0] = buf[0] + "   #              "
    buf[1] = buf[1] + "   #              "
    buf[2] = buf[2] + "   #              "
    buf[3] = buf[3] + "   #              "
    buf[4] = buf[4] + "   #              "
    buf[5] = buf[5] + "   #              "
    buf[6] = buf[6] + "   #              "
    buf[7] = buf[7] + "   #              "
    buf[8] = buf[8] + "   # # # # #      "

s = ["", "", "", "", "", "", "", "", ""]
A(s)
B(s)
I(s)
J(s)
K(s)
R(s)
S(s)
print(*s, sep = "\n")
