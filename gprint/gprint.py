# __main__.py
from random import choice

class rgb_string_not_valid(Exception):
    pass

PURE_RED_DARK_4             = ["51","0","0"]
PURE_RED_DARK_3             = ["102","0","0"]
PURE_RED_DARK_2             = ["153","0","0"]
PURE_RED_DARK_1             = ["204","0","0"]
PURE_RED                    = ["255","0","0"]
PURE_RED_LIGHT_1            = ["51","51","51"]
PURE_RED_LIGHT_2            = ["51","102","102"]
PURE_RED_LIGHT_3            = ["51","153","153"]
PURE_RED_LIGHT_4            = ["51","204","204"]

ORANGE_DARK_4               = ["51","25","0"]
ORANGE_DARK_3               = ["102","51","0"]
ORANGE_DARK_2               = ["153","76","0"]
ORANGE_DARK_1               = ["204","102","0"]
ORANGE                      = ["255","128","0"]
ORANGE_LIGHT_1              = ["255","153","51"]
ORANGE_LIGHT_2              = ["255","178","102"]
ORANGE_LIGHT_3              = ["255","204","153"]
ORANGE_LIGHT_4              = ["255","229","204"]

PURE_GREEN                  = ["0","255","0"]
PURE_BLUE                   = ["0","0","255"]

NONE                        = ["255","255","255"]
MAROON                      = ["128","0","0"]
DARK_RED                    = ["139","0","0"]
BROWN                       = ["165","42","42"]
FIREBRICK                   = ["178","34","34"]
CRIMSON                     = ["220","20","60"]
RED                         = ["255","0","0"]
TOMATO                      = ["255","99","71"]
CORAL                       = ["255","127","80"]
INDIAN_RED                  = ["205","92","92"]
LIGHT_CORAL                 = ["240","128","128"]
DARK_SALMON                 = ["233","150","122"]
SALMON                      = ["250","128","114"]
LIGHT_SALMON                = ["255","160","122"]
ORANGE_RED                  = ["255","69","0"]
DARK_ORANGE                 = ["255","140","0"]
ORANGE                      = ["255","165","0"]
GOLD                        = ["255","215","0"]
DARK_GOLDEN_ROD             = ["184","134","11"]
GOLDEN_ROD                  = ["218","165","32"]
PALE_GOLDEN_ROD             = ["238","232","170"]
DARK_KHAKI                  = ["189","183","107"]
KHAKI                       = ["240","230","140"]
OLIVE                       = ["128","128","0"]
YELLOW                      = ["255","255","0"]
YELLOW_GREEN                = ["154","205","50"]
DARK_OLIVE_GREEN            = ["85","107","47"]
OLIVE_DRAB                  = ["107","142","35"]
LAWN_GREEN                  = ["124","252","0"]
CHART_REUSE                 = ["127","255","0"]
GREEN_YELLOW                = ["173","255","47"]
DARK_GREEN                  = ["0","100","0"]
GREEN                       = ["0","128","0"]
FOREST_GREEN                = ["34","139","34"]
LIME                        = ["0","255","0"]
LIME_GREEN                  = ["50","205","50"]
LIGHT_GREEN                 = ["144","238","144"]
PALE_GREEN                  = ["152","251","152"]
DARK_SEA_GREEN              = ["143","188","143"]
MEDIUM_SPRING_GREEN         = ["0","250","154"]
SPRING_GREEN                = ["0","255","127"]
SEA_GREEN                   = ["46","139","87"]
MEDIUM_AQUA_MARINE          = ["102","205","170"]
MEDIUM_SEA_GREEN            = ["60","179","113"]
LIGHT_SEA_GREEN             = ["32","178","170"]
DARK_SLATE_GRAY             = ["47","79","79"]
TEAL                        = ["0","128","128"]
DARK_CYAN                   = ["0","139","139"]
AQUA                        = ["0","255","255"]
CYAN                        = ["0","255","255"]
LIGHT_CYAN                  = ["224","255","255"]
DARK_TURQUOISE              = ["0","206","209"]
TURQUOISE                   = ["64","224","208"]
MEDIUM_TURQUOISE            = ["72","209","204"]
PALE_TURQUOISE              = ["175","238","238"]
AQUA_MARINE                 = ["127","255","212"]
POWDER_BLUE                 = ["176","224","230"]
CADET_BLUE                  = ["95","158","160"]
STEEL_BLUE                  = ["70","130","180"]
CORN_FLOWER_BLUE            = ["100","149","237"]
DEEP_SKY_BLUE               = ["0","191","255"]
DODGER_BLUE                 = ["30","144","255"]
LIGHT_BLUE                  = ["173","216","230"]
SKY_BLUE                    = ["135","206","235"]
LIGHT_SKY_BLUE              = ["135","206","250"]
MIDNIGHT_BLUE               = ["25","25","112"]
NAVY                        = ["0","0","128"]
DARK_BLUE                   = ["0","0","139"]
MEDIUM_BLUE                 = ["0","0","205"]
BLUE                        = ["0","0","255"]
ROYAL_BLUE                  = ["65","105","225"]
BLUE_VIOLET                 = ["138","43","226"]
INDIGO                      = ["75","0","130"]
DARK_SLATE_BLUE             = ["72","61","139"]
SLATE_BLUE                  = ["106","90","205"]
MEDIUM_SLATE_BLUE           = ["123","104","238"]
MEDIUM_PURPLE               = ["147","112","219"]
DARK_MAGENTA                = ["139","0","139"]
DARK_VIOLET                 = ["148","0","211"]
DARK_ORCHID                 = ["153","50","204"]
MEDIUM_ORCHID               = ["186","85","211"]
PURPLE                      = ["128","0","128"]
THISTLE                     = ["216","191","216"]
PLUM                        = ["221","160","221"]
VIOLET                      = ["238","130","238"]
MAGENTA                     = ["255","0","255"]
FUCHSIA                     = ["255","0","255"]
ORCHID                      = ["218","112","214"]
MEDIUM_VIOLET_RED           = ["199","21","133"]
PALE_VIOLET_RED             = ["219","112","147"]
DEEP_PINK                   = ["255","20","147"]
HOT_PINK                    = ["255","105","180"]
LIGHT_PINK                  = ["255","182","193"]
PINK                        = ["255","192","203"]
ANTIQUE_WHITE               = ["250","235","215"]
BEIGE                       = ["245","245","220"]
BISQUE                      = ["255","228","196"]
BLANCHED_ALMOND             = ["255","235","205"]
WHEAT                       = ["245","222","179"]
CORN_SILK                   = ["255","248","220"]
LEMON_CHIFFON               = ["255","250","205"]
LIGHT_GOLDEN_ROD_YELLOW     = ["250","250","210"]
LIGHT_YELLOW                = ["255","255","224"]
SADDLE_BROWN                = ["139","69","19"]
SIENNA                      = ["160","82","45"]
CHOCOLATE                   = ["210","105","30"]
PERU                        = ["205","133","63"]
SANDY_BROWN                 = ["244","164","96"]
BURLY_WOOD                  = ["222","184","135"]
TAN                         = ["210","180","140"]
ROSY_BROWN                  = ["188","143","143"]
MOCCASIN                    = ["255","228","181"]
NAVAJO_WHITE                = ["255","222","173"]
PEACH_PUFF                  = ["255","218","185"]
MISTY_ROSE                  = ["255","228","225"]
LAVENDER_BLUSH              = ["255","240","245"]
LINEN                       = ["250","240","230"]
OLD_LACE                    = ["253","245","230"]
PAPAYA_WHIP                 = ["255","239","213"]
SEA_SHELL                   = ["255","245","238"]
MINT_CREAM                  = ["245","255","250"]
SLATE_GRAY                  = ["112","128","144"]
LIGHT_SLATE_GRAY            = ["119","136","153"]
LIGHT_STEEL_BLUE            = ["176","196","222"]
LAVENDER                    = ["230","230","250"]
FLORAL_WHITE                = ["255","250","240"]
ALICE_BLUE                  = ["240","248","255"]
GHOST_WHITE                 = ["248","248","255"]
HONEYDEW                    = ["240","255","240"]
IVORY                       = ["255","255","240"]
AZURE                       = ["240","255","255"]
SNOW                        = ["255","250","250"]
BLACK                       = ["0","0","0"]
DIM_GRAY                    = ["105","105","105"]
DIM_GREY                    = ["105","105","105"]
GRAY                        = ["128","128","128"]
GREY                        = ["128","128","128"]
DARK_GRAY                   = ["169","169","169"]
DARK_GREY                   = ["169","169","169"]
SILVER                      = ["192","192","192"]
LIGHT_GRAY                  = ["211","211","211"]
LIGHT_GREY                  = ["211","211","211"]
GAINSBORO                   = ["220","220","220"]
WHITE_SMOKE                 = ["245","245","245"]
WHITE                       = ["255","255","255"]

def get_random():
    return choice([MAROON, DARK_RED, BROWN, FIREBRICK, CRIMSON, RED, TOMATO, CORAL, INDIAN_RED, LIGHT_CORAL, DARK_SALMON, SALMON, LIGHT_SALMON, ORANGE_RED, DARK_ORANGE, ORANGE, GOLD, DARK_GOLDEN_ROD, GOLDEN_ROD, PALE_GOLDEN_ROD, DARK_KHAKI, KHAKI, OLIVE, YELLOW, YELLOW_GREEN, DARK_OLIVE_GREEN, OLIVE_DRAB, LAWN_GREEN, CHART_REUSE, GREEN_YELLOW, DARK_GREEN, GREEN, FOREST_GREEN, LIME, LIME_GREEN, LIGHT_GREEN, PALE_GREEN, DARK_SEA_GREEN, MEDIUM_SPRING_GREEN, SPRING_GREEN, SEA_GREEN, MEDIUM_AQUA_MARINE, MEDIUM_SEA_GREEN, LIGHT_SEA_GREEN, DARK_SLATE_GRAY, TEAL, DARK_CYAN, AQUA, CYAN, LIGHT_CYAN, DARK_TURQUOISE, TURQUOISE, MEDIUM_TURQUOISE, PALE_TURQUOISE, AQUA_MARINE, POWDER_BLUE, CADET_BLUE, STEEL_BLUE, CORN_FLOWER_BLUE, DEEP_SKY_BLUE, DODGER_BLUE, LIGHT_BLUE, SKY_BLUE, LIGHT_SKY_BLUE, MIDNIGHT_BLUE, NAVY, DARK_BLUE, MEDIUM_BLUE, BLUE, ROYAL_BLUE, BLUE_VIOLET, INDIGO, DARK_SLATE_BLUE, SLATE_BLUE, MEDIUM_SLATE_BLUE, MEDIUM_PURPLE, DARK_MAGENTA, DARK_VIOLET, DARK_ORCHID, MEDIUM_ORCHID, PURPLE, THISTLE, PLUM, VIOLET, MAGENTA, ORCHID, MEDIUM_VIOLET_RED, PALE_VIOLET_RED, DEEP_PINK, HOT_PINK, LIGHT_PINK, PINK, ANTIQUE_WHITE, BEIGE, BISQUE, BLANCHED_ALMOND, WHEAT, CORN_SILK, LEMON_CHIFFON, LIGHT_GOLDEN_ROD_YELLOW, LIGHT_YELLOW, SADDLE_BROWN, SIENNA, CHOCOLATE, PERU, SANDY_BROWN, BURLY_WOOD, TAN, ROSY_BROWN, MOCCASIN, NAVAJO_WHITE, PEACH_PUFF, MISTY_ROSE, LAVENDER_BLUSH, LINEN, OLD_LACE, PAPAYA_WHIP, SEA_SHELL, MINT_CREAM, SLATE_GRAY, LIGHT_SLATE_GRAY, LIGHT_STEEL_BLUE, LAVENDER, FLORAL_WHITE, ALICE_BLUE, GHOST_WHITE, HONEYDEW, IVORY, AZURE, SNOW, BLACK, DIM_GRAY, GRAY, DARK_GRAY, SILVER, LIGHT_GRAY, GAINSBORO, WHITE_SMOKE, WHITE])


def gprint(message, rgb="default", new_line=True, rainbow_mode=False, return_me=False):
    """Allows to print with colors with the given string and array of RGB color code or NAME"""
    try:
        if len(rgb) != 3 and rgb != "default" and rgb != "RANDOM":
            raise rgb_string_not_valid
        if rainbow_mode:
            if return_me:
                temp_string = ""
                for char in message:
                    temp_string = temp_string + gprint(char, get_random(), new_line=False, return_me=True)
                return(temp_string)
            for char in message:
                gprint(char, get_random(), new_line=False)
            gprint("",new_line=True)
        else:
            if rgb == "RANDOM":
                rgb = get_random()
            else:
                code = "\033[38;2;"+str(rgb[0])+";"+str(rgb[1])+";"+str(rgb[2])+"m"
                if new_line == False and return_me == False:
                    if rgb == "default":
                        print(message, end= '')
                    else:
                        print(code+message+'\u001b[0m', end = '')
                elif new_line == True and return_me == False:
                    if rgb == "default":
                        print(message)
                    else:
                        print(code+message+'\u001b[0m')
                if return_me == True:
                    if rgb == "default":
                        return(message)
                    else:
                        return(code+message+'\u001b[0m') 

    except rgb_string_not_valid:
        print("Not valid String detected in rgb value, it only can take an array of 3 int ex.[0,0,0], a color code ex. BLUE, RED, GREEN, or either \"RANDOM\" or \"default\".")