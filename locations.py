import numpy as np
import pandas as pd
from parsivar import Normalizer

class location:
    def location_city():
        ## city numbers location
        location_dct = {15:"azarbaijan sharghi",
                    25:"azarbaijan sharghi",
                    35:"azarbaijan sharghi",
                    17:"azarbaijan gharbi",
                    27:"azarbaijan gharbi",
                    37:"azarbaijan gharbi",
                    91:"ardabil",
                    13:"esfahan",
                    53:"esfahan",
                    67:"esfahan",
                    43:"esfahan",
                    23:"esfahan",
                    68:"karaj",
                    21:"karaj , tehran",
                    38:"karaj",
                    78:"karaj , tehran",
                    98:"ilam",
                    48:"boshehr",
                    58:"boshehr",
                    11:"tehran",
                    22:"tehran",
                    33:"tehran",
                    44:"tehran",
                    55:"tehran",
                    66:"tehran",
                    77:"tehran",
                    88:"tehran",
                    99:"tehran",
                    10:"tehran",
                    20:"tehran",
                    30:"tehran",
                    40:"tehran",
                    50:"tehran",
                    60:"tehran",
                    70:"tehran",
                    80:"tehran",
                    90:"tehran",
                    71:"chaharmahal bakhtiari",
                    81:"chaharmahal bakhtiari",
                    26:"khorasan shomali",
                    74:"khorasan razavi , jonobi",
                    12:"khorasan razavi",
                    36:"khorasan razavi",
                    32:"khorasan razavi",
                    42:"khorasan razavi",
                    52:"khorasan jonobi",
                    14:"khozestan",
                    24:"khozestan",
                    34:"khozestan",
                    87:"zanjan",
                    97:"zanjan",
                    86:"semnan",
                    96:"semnan",
                    85:"sistan balochestan",
                    95:"sistan balochestan",
                    63:"fars",
                    93:"fars",
                    73:"fars",
                    83:"fars",
                    79:"ghazvin",
                    89:"ghazvin",
                    16:"ghom",
                    51:"kordestan",
                    61:"kordestan",
                    45:"kerman",
                    65:"kerman",
                    75:"kerman",
                    19:"kermanshah",
                    29:"kermanshah",
                    39:"kermanshah",
                    49:"kohkiloye va boyerahmad",
                    59:"golestan",
                    69:"golestan",
                    46:"gilan",
                    56:"gilan",
                    76:"gilan",
                    31:"lorestan",
                    41:"lorestan",
                    62:"mazandaran",
                    72:"mazandaran",
                    82:"mazandaran",
                    92:"mazandaran",
                    47:"markazi",
                    57:"markazi",
                    18:"hamedan",
                    28:"hamedan",
                    54:"yazd",
                    64:"yazd",
                    84:"hormozgan",
                    94:"hormozgan"
                    }
        return location_dct
    
    def exact_city(city_num , alphabet):
        ## exact locations
        if city_num ==15:
            return "tabriz"
        elif city_num ==25:
            if alphabet =="س":
                return "ahar"
            elif alphabet =="ی":
                return "azar shahr"
            elif alphabet =="م":
                return "bostan abad"
            elif alphabet =="ل":
                return "bonab"
            elif alphabet =="ط":
                return "jolfa"
            elif alphabet =="ص":
                return "sarab"
            elif alphabet =="ن":
                return "shabestar"
            elif alphabet =="و":
                return "klibar"
            elif alphabet =="ب":
                return "maraghe"
            elif alphabet =="ج":
                return "marand"
            elif alphabet =="د":
                return "miyane"
            elif alphabet =="ه":
                return "haris"
            elif alphabet =="ق":
                return "hashtrood"
            elif alphabet =="ع":
                return "tabriz"
            else:
                return "tabriz"
            
        elif city_num ==35:
            if alphabet =="ب":
                return "osko"
            elif alphabet =="ل":
                return "tabriz"
            elif alphabet =="م":
                return "tabriz"
            elif alphabet =="ط":
                return "tabriz"
            elif alphabet =="س":
                return "char oimagh"
            elif alphabet =="د":
                return "ajab shir"
            elif alphabet =="ص":
                return "malekan"
            elif alphabet =="ج":
                return "varzaghan"
            else:
                return "tabriz"
            
        if city_num ==17:
            return "urumie"
        elif city_num ==27:
            if alphabet =="ن":
                return "bokan"
            elif alphabet =="ج":
                return "mahabad"
            elif alphabet =="م":
                return "sardasht"
            elif alphabet =="ب":
                return "khoi"
            elif alphabet =="س":
                return "salmas"
            elif alphabet =="ص":
                return "naghadeh"
            elif alphabet =="ط":
                return "miyan doab"
            elif alphabet =="و":
                return "piranshahr"
            elif alphabet =="ی":
                return "eshnaviye"
            elif alphabet =="ل":
                return "shahin dejh"
            elif alphabet =="د":
                return "mako"
            elif alphabet =="ق":
                return "takab"
            elif alphabet =="ه":
                return "chaldoran"
            elif alphabet =="ع":
                return "azarbaijan gharbi"
            else:
                return "urumie"
            
        elif city_num ==37:
            if alphabet =="ب":
                return "khoi"
            elif alphabet =="ص":
                return "mahabad"
            elif alphabet =="ل":
                return "mako"
            elif alphabet =="ق":
                return "salmas"
            elif alphabet =="ط":
                return "bokan"
            elif alphabet =="ج":
                return "miyan doab"
            else:
                return "urumie"
        
        if city_num ==91:
            return "ardabil"
    
        if city_num ==13:
            return "esfahan"
        elif city_num ==53:
            return "esfahan"
        elif city_num ==67:
            return "esfahan"
        elif city_num ==43:
            if alphabet =="س":
                return "aran ,bidgol ,kashan"
            elif alphabet =="ج":
                return "mobarakeh"
            elif alphabet =="د":
                return "shahin shahr"
            elif alphabet =="ص":
                return "tiran , kron"
            elif alphabet =="ب":
                return "chadegan"
            elif alphabet =="ط":
                return "mobarakeh"
            elif alphabet =="ع":
                return "esfahan"
            elif alphabet =="ق":
                return "dehaghan"
            elif alphabet =="ل":
                return "meymeh"
            elif alphabet =="م":
                return "najaf abad"
            elif alphabet =="ن":
                return "khomeini shahr"
            elif alphabet =="و":
                return "kashan"
            elif alphabet =="ه":
                return "folad shahr"
            elif alphabet =="ی":
                return "felaverjan"
            else:
                return "esfahan"
            
        elif city_num ==23:
            if alphabet =="س":
                return "khomeini shahr"
            elif alphabet =="ه":
                return "flaverjan"
            elif alphabet =="ی":
                return "zarin shahr"
            elif alphabet =="ب":
                return "kashan"
            elif alphabet =="ج":
                return "najaf abad"
            elif alphabet =="د":
                return "shahreza"
            elif alphabet =="م":
                return "nayiin"
            elif alphabet =="ط":
                return "natanz"
            elif alphabet =="ن":
                return "samiram"
            elif alphabet =="ي":
                return "folad shahr"
            elif alphabet =="ت":
                return "esfahan"
            elif alphabet =="ص":
                return "golpaigan"
            elif alphabet =="ع":
                return "esfahan"
            elif alphabet =="ق":
                return "ardestan"
            elif alphabet =="ل":
                return "khansar"
            elif alphabet =="و":
                return "fereidon shahr"
            else:
                return "esfahan"
         
        if city_num ==68:
            return "karaj"
        elif city_num ==21:
            if alphabet =="و":
                return "karaj"
            elif alphabet =="ص":
                return "karaj"
        elif city_num ==38:
            if alphabet =="ب":
                return "karaj"
            elif alphabet =="د":
                return "fardis"
            elif alphabet =="س":
                return "eshtehard"
            elif alphabet =="م":
                return "charbagh"
            elif alphabet =="ن":
                return "savjebelagh"
            elif alphabet =="ه":
                return "taleghan"
            elif alphabet =="هـ":
                return "taleghan"
            elif alphabet =="ج":
                return "shahriyar"
            elif alphabet =="ط":
                return "malard"
            elif alphabet =="و":
                return "ghods"
            elif alphabet =="ص":
                return "varamin,pishva,gharchak"
            elif alphabet =="ق":
                return "eslam shahr"
            elif alphabet =="ل":
                return "robatkarim,baharestan"
            elif alphabet =="ع":
                return "tehran,karaj"
            elif alphabet =="ی":
                return "nazar abad"
            else:
                return "tehran,alborz"
            
        elif city_num ==78:
            if alphabet =="ط":
                return "karaj"
            elif alphabet =="ع":
                return "alborz"
            elif alphabet =="م":
                return "parand"
            elif alphabet =="ی":
                return "eslam shahr"
            elif alphabet =="ب":
                return "eslam shahr"
            elif alphabet =="ت":
                return "alborz"
            elif alphabet =="د":
               return "shahriyar,malard"
            elif alphabet =="ص":
                return "damavand"
            elif alphabet =="ق":
                return "firozkooh"
            elif alphabet =="ل":
                return "pakdasht"
            elif alphabet =="و":
                return "shemiranat"
            else:
                return "alborz"
            
        if city_num ==98:
            return "ilam"
        
        if city_num ==48:
            return "boshehr"
        elif city_num ==58:
            if alphabet =="س":
                return "tangestan"
            elif alphabet =="ب":
                return "dashtestan"
            elif alphabet =="ص":
                return "dashti"
            elif alphabet =="ط":
                return "deir"
            elif alphabet =="ق":
                return "deilam"
            elif alphabet =="د":
                return "kangan"
            elif alphabet =="ج":
                return "genaveh"
            else:
                return "boshehr"
            
        if city_num ==11:
            return "tehran"
        elif city_num ==22:
            return "tehran"
        elif city_num ==33:
            return "tehran"
        elif city_num ==44:
            return "tehran"
        elif city_num ==55:
            return "tehran"
        elif city_num ==66:
            return "tehran"
        elif city_num ==77:
            return "tehran"
        elif city_num ==88:
            return "tehran"
        elif city_num ==99:
            return "tehran"
        elif city_num ==10:
            return "tehran"
        elif city_num ==20:
            return "tehran"
        elif city_num ==30:
            return "tehran"
        elif city_num ==40:
            return "tehran"
        elif city_num ==50:
            return "tehran"
        elif city_num ==60:
            return "tehran"
        elif city_num ==70:
            return "tehran"
        elif city_num ==80:
            return "tehran"
        elif city_num ==90:
            return "tehran"
        
        elif city_num ==21:
            if alphabet != "ص":
                return "tehran"
            elif alphabet != "و":
                return "tehran"
            
        if city_num ==78:
            if alphabet =="ی":
                return "eslam shahr"
            elif alphabet =="ب":
                return "eslam shahr"
            elif alphabet =="و":
                return "oshan va fasham"
            elif alphabet =="ل":
                return "pakdasht"
            elif alphabet =="ص":
                return "damavand , rodehen"
            elif alphabet =="د":
                return "shahriayar"
            elif alphabet =="ه":
                return "shahriayar"
            elif alphabet =="ج":
                return "robat karim"
            elif alphabet =="ن":
                return "rey"
            elif alphabet =="ط":
                return "taleghan va savjbelagh"
            elif alphabet =="ق":
                return "firozkoh"
            elif alphabet =="س":
                return "varamin"
            else:
                return "tehran"
            
        if city_num ==38:
            if alphabet =="ی":
                return "nazar abad"
            elif alphabet =="ل":
                return "baharestan"
            elif alphabet =="ص":
                return "varamin , pishva , gharchak"
            elif alphabet =="ه":
                return "taleghan"
            elif alphabet =="ج":
                return "shahriyar"
            elif alphabet =="ن":
                return "savjblagh"
            elif alphabet =="ط":
                return "malard"
            elif alphabet =="ق":
                return "eslamshahr"
        
        if city_num ==71:
            return "shahre kord"
        if city_num ==81:
            if alphabet =="ج":
                return "ardal"
            elif alphabet =="ب":
                return "brojen"
            elif alphabet =="د":
                return "farsan"
            else:
                return "charmahl bakhtiari"
            
        if city_num ==26:
            if alphabet =="ج":
                return "bojnord"
            elif alphabet =="ب":
                return "bojnord"
            elif alphabet =="د":
                return "bojnord"
            elif alphabet =="س":
                return "bojnord"
            elif alphabet =="ق":
                return "esfarayen"
            elif alphabet =="و":
                return "garme, mane, jajrm"
            elif alphabet =="ص":
                return "shirvan"
            elif alphabet =="م":
                return "farooj" 
            else:
                return "khorasan shomali"
            
        if city_num ==74:
            if alphabet =="ج":
                return "bojnord"
        
        if city_num ==12:
            return "mashhad"
        elif city_num ==74:
            return "mashhad"
        if city_num ==32:
            if alphabet =="د":
                return "birjand , sarakhs"
            elif alphabet =="ص":
                return "torbate jam"
            elif alphabet =="ل":
                return "torbate heidarie"
            elif alphabet =="ج":
                return "sabzevar"
            elif alphabet =="ط":
                return "ghochan"
            elif alphabet =="م":
                return "kashmar"
            elif alphabet =="ق":
                return "gonabad"
            elif alphabet =="ب":
                return "neyshabor"
            elif alphabet =="ه":
                return "taibad"
            else:
                return "khorasan"
            
        if city_num ==36:
            if alphabet =="ی":
                return "torbate jam"
            elif alphabet =="ن":
                return "torbate heidarie"
            elif alphabet =="م":
                return "sabzevar"
            elif alphabet =="ق":
                return "kashmar"
            elif alphabet =="ل":
                return "neyshabor"
            else:
                return "mashhad"
            
        if city_num ==42:
            if alphabet =="ل":
                return "bord skan"
            elif alphabet =="م":
                return "rashtkhar"
            elif alphabet =="ص":
                return "khaf"
            elif alphabet =="ج":
                return "mashhad"
            elif alphabet =="ق":
                return "esfarayen"
            else:
                return "khorasan razavi,shomali"
            
        if city_num ==52:
            return "birjand"
        
        if city_num ==14:
            return "ahvaz"
        elif city_num ==24:
            return "khozestan"
        elif city_num ==34:
            return "khozestan"
        
        if city_num ==87:
            return "zanjan"
        if city_num ==97:
            if alphabet =="ب":
                return "abhar"
            elif alphabet =="ج":
                return "khodabandeh"
            elif alphabet =="د":
                return "khoramdeh"
            else:
                return "zanjan"
          
        if city_num ==86:
            return "semnan"
        if city_num ==96:
            if alphabet =="ب":
                return "damghan"
            elif alphabet =="ج":
                return "shahrood"
            elif alphabet =="د":
                return "garmsar"
            elif alphabet =="ص":
                return "shahrood"
            else:
                return "semnan"
        
        if city_num ==85:
            return "zahedan"
        if city_num ==95:
            return "chabahar"
        
        if city_num ==63:
            return "shiraz"
        if city_num ==93:
            return "shiraz"
        if city_num ==73:
            return "fars"
        if city_num ==83:
            return "fars"
        
        if city_num ==79:
            return "ghazvin"
        if city_num ==89:
            return "ghazvin"
        
        if city_num ==16:
            return "ghom"
        
        if city_num ==51:
            return "sanandaj"
    
        if city_num ==61:
            if alphabet =="د":
                return "baneh"
            elif alphabet =="ج":
                return "bijar"
            elif alphabet =="ط":
                return "divandareh"
            elif alphabet =="ل":
                return "sarv abad"
            elif alphabet =="ب":
                return "saghez"
            elif alphabet =="س":
                return "ghorveh"
            elif alphabet =="ق":
                return "kamyaran"
            elif alphabet =="ص":
                return "marivan"
            else:
                return "kordestan"
            
        if city_num ==45:
            return "kerman"
        if city_num ==75:
            return "kerman"
        if city_num ==65:
            if alphabet =="س":
                return "baft"
            elif alphabet =="م":
                return "bordsir"
            elif alphabet =="ج":
                return "bam"
            elif alphabet =="ص":
                return "jiroft"
            elif alphabet =="ه":
                return "ravar"
            elif alphabet =="ب":
                return "rafsanjan"
            elif alphabet =="ط":
                return "zarand"
            elif alphabet =="د":
                return "sirjan"
            elif alphabet =="ل":
                return "shahre babak"
            elif alphabet =="و":
                return "anbar abad"
            elif alphabet =="ق":
                return "khnoj"
            elif alphabet =="ن":
                return "manojan"
            else:
                return "kerman"
            
        if city_num ==19:
            return "kermanshah"
        if city_num ==29:
            return "kermanshah"
        if city_num ==39:
            return "kermanshah"
        
        if city_num ==49:
            return "kohkiloye va boyerahmad"
        
        if city_num ==59:
            return "gorgan"
        if city_num ==69:
            return "golestan"
        
        if city_num ==46:
            return "rasht"
        if city_num ==56:
            if alphabet =="و":
                return "amlash"
            elif alphabet =="ب":
                return "bandar anzali"
            elif alphabet =="د":
                return "astara"
            elif alphabet =="س":
                return "talesh"
            elif alphabet =="ن":
                return "rezvanshahr"
            elif alphabet =="ط":
                return "rodbar"
            elif alphabet =="ص":
                return "rodsar"
            elif alphabet =="ق":
                return "somesara"
            elif alphabet =="ل":
                return "foman"
            elif alphabet =="ج":
                return "lahijan"
            elif alphabet =="م":
                return "langerod"
            else:
                return "gilan"
            
        if city_num ==76:
            if alphabet =="ج":
                return "astaneh ashrafie"
            elif alphabet =="ب":
                return "siyahkal"
            elif alphabet =="س":
                return "bandar anzali"
            elif alphabet =="ن":
                return "lahijan"
            elif alphabet =="ع":
                return "gilan"
            else:
                return "gilan"
        
        if city_num ==31:
            return "khoram abad"
        if city_num ==41:
            if alphabet =="ب":
                return "brojerd"
            elif alphabet =="د":
                return "dorod"
            elif alphabet =="ج":
                return "aligodarz"
            else:
                return "lorestan"
        
        if city_num ==62:
            return "sari"
        if city_num ==92:
            return "mazandaran"
        if city_num ==82:
            return "ghaem shahr,savadkoh"
        
        if city_num ==72:
            if alphabet =="و":
                return "mahmood abad"
            elif alphabet =="ب":
                return "amol"
            elif alphabet =="د":
                return "tonekabon"
            elif alphabet =="س":
                return "ramsar"
            elif alphabet =="ن":
                return "chalos"
            elif alphabet =="ط":
                return "noor"
            elif alphabet =="ص":
                return "noshahr"
            elif alphabet =="ق":
                return "beh shahr"
            elif alphabet =="ل":
                return "ghaem shahr"
            elif alphabet =="ج":
                return "babol"
            elif alphabet =="م":
                return "babolsar"
            elif alphabet =="ی":
                return "joybar"
            elif alphabet =="ه":
                return "neka"
            else:
                return "mazandaran"
        
        if city_num ==47:
            return "arak"
        if city_num ==57:
            if alphabet =="س":
                return "tafrsh"
            elif alphabet =="د":
                return "mahalat"
            elif alphabet =="ب":
                return "saveh"
            elif alphabet =="ق":
                return "shazand"
            else:
                return "markazi"
            
            
        if city_num ==84:
            return "bandar abbas"
        if city_num ==94:
            return "hormozgan"
        
        if city_num ==18:
            return "hamedan"
        if city_num ==28:
            return "hamedan"
        
        if city_num ==54:
            return "yazd"
        if city_num ==64:
            if alphabet =="ب":
                return "ardakan"
            elif alphabet =="د":
                return "meybod"
            elif alphabet =="ص":
                return "mehriz"
            elif alphabet =="ق":
                return "tabas"
            elif alphabet =="ل":
                return "harat"
            elif alphabet =="ج":
                return "taft"
            elif alphabet =="م":
                return "sedogh"
            else:
                return "yazd"
            
    def states(city_num):
        ## city numbers states
        state_dct = {15:"azarbaijan sharghi",
                    25:"azarbaijan sharghi",
                    35:"azarbaijan sharghi",
                    17:"azarbaijan gharbi",
                    27:"azarbaijan gharbi",
                    37:"azarbaijan gharbi",
                    91:"ardabil",
                    13:"esfahan",
                    53:"esfahan",
                    67:"esfahan",
                    43:"esfahan",
                    23:"esfahan",
                    68:"karaj",
                    21:"karaj , tehran",
                    38:"karaj",
                    78:"karaj , tehran",
                    98:"ilam",
                    48:"boshehr",
                    58:"boshehr",
                    11:"tehran",
                    22:"tehran",
                    33:"tehran",
                    44:"tehran",
                    55:"tehran",
                    66:"tehran",
                    77:"tehran",
                    88:"tehran",
                    99:"tehran",
                    10:"tehran",
                    20:"tehran",
                    30:"tehran",
                    40:"tehran",
                    50:"tehran",
                    60:"tehran",
                    70:"tehran",
                    80:"tehran",
                    90:"tehran",
                    71:"chaharmahal bakhtiari",
                    81:"chaharmahal bakhtiari",
                    26:"khorasan shomali",
                    74:"khorasan razavi , jonobi",
                    12:"khorasan razavi",
                    36:"khorasan razavi",
                    32:"khorasan razavi",
                    42:"khorasan razavi",
                    52:"khorasan jonobi",
                    14:"khozestan",
                    24:"khozestan",
                    34:"khozestan",
                    87:"zanjan",
                    97:"zanjan",
                    86:"semnan",
                    96:"semnan",
                    85:"sistan balochestan",
                    95:"sistan balochestan",
                    63:"fars",
                    93:"fars",
                    73:"fars",
                    83:"fars",
                    79:"ghazvin",
                    89:"ghazvin",
                    16:"ghom",
                    51:"kordestan",
                    61:"kordestan",
                    45:"kerman",
                    65:"kerman",
                    75:"kerman",
                    19:"kermanshah",
                    29:"kermanshah",
                    39:"kermanshah",
                    49:"kohkiloye va boyerahmad",
                    59:"golestan",
                    69:"golestan",
                    46:"gilan",
                    56:"gilan",
                    76:"gilan",
                    31:"lorestan",
                    41:"lorestan",
                    62:"mazandaran",
                    72:"mazandaran",
                    82:"mazandaran",
                    92:"mazandaran",
                    47:"markazi",
                    57:"markazi",
                    18:"hamedan",
                    28:"hamedan",
                    54:"yazd",
                    64:"yazd",
                    84:"hormozgan",
                    94:"hormozgan"
                    }
        state = state_dct[city_num]
        return state
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
