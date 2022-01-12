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
def X(buf):
    buf[0] = buf[0] + "##            ##  "
    buf[1] = buf[1] + "  ##        ##    "
    buf[2] = buf[2] + "    ##    ##      "
    buf[3] = buf[3] + "     ##  ##       "
    buf[4] = buf[4] + "       ##         "
    buf[5] = buf[5] + "     ## ##        "
    buf[6] = buf[6] + "    ##   ##       "
    buf[7] = buf[7] + "  ##       ##     "
    buf[8] = buf[8] + "##           ##   "    
s = ["", "", "", "", "", "", "", "", ""]
A(s)
X(s)
print(*s, sep = "\n")
