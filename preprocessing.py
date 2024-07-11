import numpy as np
import pandas as pd
from parsivar import Normalizer

class pre:
    def preprocess():
        # converting txt to csv & necessary changes
        with open ("plates.txt" , "r") as f:
            txt = f.readlines()
            
        with open ("plates_data.csv" , "w") as f:
            for line in txt:
                line = line.replace(" ",",")
                line = line.replace("	" , ",")
                f.write(line)
        
        ## read csv
        data = pd.read_csv("plates_data.csv", on_bad_lines="skip" , encoding="UTF-8")
        
        ## renaming
        data = data.rename(columns={"21":"city_num",
                                    "961416005##20181221_095657.jpg##NR##1.jpg" : "img_names" ,
                                    "833" : "3num" , "ن" : "alphabet" , 
                                    "69" : "2num" })
        
        
        print("--------basic informations--------")
        print(data.shape)
        print("**************")
        print(data.head)
        print("**************")
        data_describe=data.describe()
        print(data_describe)
        print("**************")
        print(data.info())
        
        
        ## missing data
        print("missing data: \n",data.isnull().sum())
        
        ## dropna base on main columns in data
        data.dropna(subset=["city_num","alphabet"],inplace=True)
        print(data.shape)
        print(data.isnull().sum())
        
        ## astype converting for normalizing
        data["city_num"] = data["city_num"].astype(str)
        data["3num"] = data["3num"].astype(str)
        data["2num"] = data["2num"].astype(str)
        
        ## normalizing numerical persian data to eng
        normalizer = Normalizer()
        data["city_num"] = data["city_num"].apply(normalizer.normalize).astype(int)
        data["3num"] = data["3num"].apply(normalizer.normalize)
        data["2num"] = data["2num"].apply(normalizer.normalize)
        
        ## ############outliers
        
        #medaian
        med=data["city_num"].quantile(0.5)
        
        #Q1
        Q1=data["city_num"].quantile(0.25)
        
        #Q3
        Q3=data["city_num"].quantile(0.75)
        
        #IQR
        IQR=Q3-Q1
        
        #lower extreme
        lower_ex=Q1-(1.5*(IQR))
        # print("lower_ex = ",lower_ex)
        
        #upper extreme
        upper_ex=Q3+(1.5*(IQR))
        # print("upper_ex = " ,upper_ex)
        
        data["city_num"]=data.city_num[(data.city_num<upper_ex) & (data.city_num>lower_ex)]
        data.dropna(subset=["city_num"],inplace=True)
        
        ## index 
        data.rename(index=data.img_names ,inplace = True)
        data.drop("img_names" , axis =1 , inplace = True)
        
        ## drop duplicates
        data.drop_duplicates(inplace=True)
        print("shape after drop duplicates: ",data.shape)
        
        ## locationing just base on city_numbers
        from locations import location
        mylocation = location.location_city()
        
        data["location"] = data["city_num"].map(mylocation)
        data.dropna(subset=["location"],inplace=True)
        print(data.isnull().sum())
        
        ## exact locationing base on alphabets
        def condition(data):
            
            if data.city_num ==15:
                return "tabriz"
            elif data.city_num ==25:
                if data.alphabet =="س":
                    return "ahar"
                elif data.alphabet =="ی":
                    return "azar shahr"
                elif data.alphabet =="م":
                    return "bostan abad"
                elif data.alphabet =="ل":
                    return "bonab"
                elif data.alphabet =="ط":
                    return "jolfa"
                elif data.alphabet =="ص":
                    return "sarab"
                elif data.alphabet =="ن":
                    return "shabestar"
                elif data.alphabet =="و":
                    return "klibar"
                elif data.alphabet =="ب":
                    return "maraghe"
                elif data.alphabet =="ج":
                    return "marand"
                elif data.alphabet =="د":
                    return "miyane"
                elif data.alphabet =="ه":
                    return "haris"
                elif data.alphabet =="ق":
                    return "hashtrood"
                elif data.alphabet =="ع":
                    return "tabriz"
                else:
                    return "tabriz"
                
            elif data.city_num ==35:
                if data.alphabet =="ب":
                    return "osko"
                elif data.alphabet =="ل":
                    return "tabriz"
                elif data.alphabet =="م":
                    return "tabriz"
                elif data.alphabet =="ط":
                    return "tabriz"
                elif data.alphabet =="س":
                    return "char oimagh"
                elif data.alphabet =="د":
                    return "ajab shir"
                elif data.alphabet =="ص":
                    return "malekan"
                elif data.alphabet =="ج":
                    return "varzaghan"
                else:
                    return "tabriz"
                
            if data.city_num ==17:
                return "urumie"
            elif data.city_num ==27:
                if data.alphabet =="ن":
                    return "bokan"
                elif data.alphabet =="ج":
                    return "mahabad"
                elif data.alphabet =="م":
                    return "sardasht"
                elif data.alphabet =="ب":
                    return "khoi"
                elif data.alphabet =="س":
                    return "salmas"
                elif data.alphabet =="ص":
                    return "naghadeh"
                elif data.alphabet =="ط":
                    return "miyan doab"
                elif data.alphabet =="و":
                    return "piranshahr"
                elif data.alphabet =="ی":
                    return "eshnaviye"
                elif data.alphabet =="ل":
                    return "shahin dejh"
                elif data.alphabet =="د":
                    return "mako"
                elif data.alphabet =="ق":
                    return "takab"
                elif data.alphabet =="ه":
                    return "chaldoran"
                elif data.alphabet =="ع":
                    return "azarbaijan gharbi"
                else:
                    return "urumie"
                
            elif data.city_num ==37:
                if data.alphabet =="ب":
                    return "khoi"
                elif data.alphabet =="ص":
                    return "mahabad"
                elif data.alphabet =="ل":
                    return "mako"
                elif data.alphabet =="ق":
                    return "salmas"
                elif data.alphabet =="ط":
                    return "bokan"
                elif data.alphabet =="ج":
                    return "miyan doab"
                else:
                    return "urumie"
            
            if data.city_num ==91:
                return "ardabil"
        
            if data.city_num ==13:
                return "esfahan"
            elif data.city_num ==53:
                return "esfahan"
            elif data.city_num ==67:
                return "esfahan"
            elif data.city_num ==43:
                if data.alphabet =="س":
                    return "aran ,bidgol ,kashan"
                elif data.alphabet =="ج":
                    return "mobarakeh"
                elif data.alphabet =="د":
                    return "shahin shahr"
                elif data.alphabet =="ص":
                    return "tiran , kron"
                elif data.alphabet =="ب":
                    return "chadegan"
                elif data.alphabet =="ط":
                    return "mobarakeh"
                elif data.alphabet =="ع":
                    return "esfahan"
                elif data.alphabet =="ق":
                    return "dehaghan"
                elif data.alphabet =="ل":
                    return "meymeh"
                elif data.alphabet =="م":
                    return "najaf abad"
                elif data.alphabet =="ن":
                    return "khomeini shahr"
                elif data.alphabet =="و":
                    return "kashan"
                elif data.alphabet =="ه":
                    return "folad shahr"
                elif data.alphabet =="ی":
                    return "felaverjan"
                else:
                    return "esfahan"
                
            elif data.city_num ==23:
                if data.alphabet =="س":
                    return "khomeini shahr"
                elif data.alphabet =="ه":
                    return "flaverjan"
                elif data.alphabet =="ی":
                    return "zarin shahr"
                elif data.alphabet =="ب":
                    return "kashan"
                elif data.alphabet =="ج":
                    return "najaf abad"
                elif data.alphabet =="د":
                    return "shahreza"
                elif data.alphabet =="م":
                    return "nayiin"
                elif data.alphabet =="ط":
                    return "natanz"
                elif data.alphabet =="ن":
                    return "samiram"
                elif data.alphabet =="ي":
                    return "folad shahr"
                elif data.alphabet =="ت":
                    return "esfahan"
                elif data.alphabet =="ص":
                    return "golpaigan"
                elif data.alphabet =="ع":
                    return "esfahan"
                elif data.alphabet =="ق":
                    return "ardestan"
                elif data.alphabet =="ل":
                    return "khansar"
                elif data.alphabet =="و":
                    return "fereidon shahr"
                else:
                    return "esfahan"
             
            if data.city_num ==68:
                return "karaj"
            elif data.city_num ==21:
                if data.alphabet =="و":
                    return "karaj"
                elif data.alphabet =="ص":
                    return "karaj"
            elif data.city_num ==38:
                if data.alphabet =="ب":
                    return "karaj"
                elif data.alphabet =="د":
                    return "fardis"
                elif data.alphabet =="س":
                    return "eshtehard"
                elif data.alphabet =="م":
                    return "charbagh"
                elif data.alphabet =="ن":
                    return "savjebelagh"
                elif data.alphabet =="ه":
                    return "taleghan"
                elif data.alphabet =="هـ":
                    return "taleghan"
                elif data.alphabet =="ج":
                    return "shahriyar"
                elif data.alphabet =="ط":
                    return "malard"
                elif data.alphabet =="و":
                    return "ghods"
                elif data.alphabet =="ص":
                    return "varamin,pishva,gharchak"
                elif data.alphabet =="ق":
                    return "eslam shahr"
                elif data.alphabet =="ل":
                    return "robatkarim,baharestan"
                elif data.alphabet =="ع":
                    return "tehran,karaj"
                elif data.alphabet =="ی":
                    return "nazar abad"
                else:
                    return "tehran,alborz"
                
            elif data.city_num ==78:
                if data.alphabet =="ط":
                    return "karaj"
                elif data.alphabet =="ع":
                    return "alborz"
                elif data.alphabet =="م":
                    return "parand"
                elif data.alphabet =="ی":
                    return "eslam shahr"
                elif data.alphabet =="ب":
                    return "eslam shahr"
                elif data.alphabet =="ت":
                    return "alborz"
                elif data.alphabet =="د":
                   return "shahriyar,malard"
                elif data.alphabet =="ص":
                    return "damavand"
                elif data.alphabet =="ق":
                    return "firozkooh"
                elif data.alphabet =="ل":
                    return "pakdasht"
                elif data.alphabet =="و":
                    return "shemiranat"
                else:
                    return "alborz"
                
            if data.city_num ==98:
                return "ilam"
            
            if data.city_num ==48:
                return "boshehr"
            elif data.city_num ==58:
                if data.alphabet =="س":
                    return "tangestan"
                elif data.alphabet =="ب":
                    return "dashtestan"
                elif data.alphabet =="ص":
                    return "dashti"
                elif data.alphabet =="ط":
                    return "deir"
                elif data.alphabet =="ق":
                    return "deilam"
                elif data.alphabet =="د":
                    return "kangan"
                elif data.alphabet =="ج":
                    return "genaveh"
                else:
                    return "boshehr"
                
            if data.city_num ==11:
                return "tehran"
            elif data.city_num ==22:
                return "tehran"
            elif data.city_num ==33:
                return "tehran"
            elif data.city_num ==44:
                return "tehran"
            elif data.city_num ==55:
                return "tehran"
            elif data.city_num ==66:
                return "tehran"
            elif data.city_num ==77:
                return "tehran"
            elif data.city_num ==88:
                return "tehran"
            elif data.city_num ==99:
                return "tehran"
            elif data.city_num ==10:
                return "tehran"
            elif data.city_num ==20:
                return "tehran"
            elif data.city_num ==30:
                return "tehran"
            elif data.city_num ==40:
                return "tehran"
            elif data.city_num ==50:
                return "tehran"
            elif data.city_num ==60:
                return "tehran"
            elif data.city_num ==70:
                return "tehran"
            elif data.city_num ==80:
                return "tehran"
            elif data.city_num ==90:
                return "tehran"
            
            elif data.city_num ==21:
                if data.alphabet != "ص":
                    return "tehran"
                elif data.alphabet != "و":
                    return "tehran"
                
            if data.city_num ==78:
                if data.alphabet =="ی":
                    return "eslam shahr"
                elif data.alphabet =="ب":
                    return "eslam shahr"
                elif data.alphabet =="و":
                    return "oshan va fasham"
                elif data.alphabet =="ل":
                    return "pakdasht"
                elif data.alphabet =="ص":
                    return "damavand , rodehen"
                elif data.alphabet =="د":
                    return "shahriayar"
                elif data.alphabet =="ه":
                    return "shahriayar"
                elif data.alphabet =="ج":
                    return "robat karim"
                elif data.alphabet =="ن":
                    return "rey"
                elif data.alphabet =="ط":
                    return "taleghan va savjbelagh"
                elif data.alphabet =="ق":
                    return "firozkoh"
                elif data.alphabet =="س":
                    return "varamin"
                else:
                    return "tehran"
                
            if data.city_num ==38:
                if data.alphabet =="ی":
                    return "nazar abad"
                elif data.alphabet =="ل":
                    return "baharestan"
                elif data.alphabet =="ص":
                    return "varamin , pishva , gharchak"
                elif data.alphabet =="ه":
                    return "taleghan"
                elif data.alphabet =="ج":
                    return "shahriyar"
                elif data.alphabet =="ن":
                    return "savjblagh"
                elif data.alphabet =="ط":
                    return "malard"
                elif data.alphabet =="ق":
                    return "eslamshahr"
            
            if data.city_num ==71:
                return "shahre kord"
            if data.city_num ==81:
                if data.alphabet =="ج":
                    return "ardal"
                elif data.alphabet =="ب":
                    return "brojen"
                elif data.alphabet =="د":
                    return "farsan"
                else:
                    return "charmahl bakhtiari"
                
            if data.city_num ==26:
                if data.alphabet =="ج":
                    return "bojnord"
                elif data.alphabet =="ب":
                    return "bojnord"
                elif data.alphabet =="د":
                    return "bojnord"
                elif data.alphabet =="س":
                    return "bojnord"
                elif data.alphabet =="ق":
                    return "esfarayen"
                elif data.alphabet =="و":
                    return "garme, mane, jajrm"
                elif data.alphabet =="ص":
                    return "shirvan"
                elif data.alphabet =="م":
                    return "farooj" 
                else:
                    return "khorasan shomali"
                
            if data.city_num ==74:
                if data.alphabet =="ج":
                    return "bojnord"
            
            if data.city_num ==12:
                return "mashhad"
            elif data.city_num ==74:
                return "mashhad"
            if data.city_num ==32:
                if data.alphabet =="د":
                    return "birjand , sarakhs"
                elif data.alphabet =="ص":
                    return "torbate jam"
                elif data.alphabet =="ل":
                    return "torbate heidarie"
                elif data.alphabet =="ج":
                    return "sabzevar"
                elif data.alphabet =="ط":
                    return "ghochan"
                elif data.alphabet =="م":
                    return "kashmar"
                elif data.alphabet =="ق":
                    return "gonabad"
                elif data.alphabet =="ب":
                    return "neyshabor"
                elif data.alphabet =="ه":
                    return "taibad"
                else:
                    return "khorasan"
                
            if data.city_num ==36:
                if data.alphabet =="ی":
                    return "torbate jam"
                elif data.alphabet =="ن":
                    return "torbate heidarie"
                elif data.alphabet =="م":
                    return "sabzevar"
                elif data.alphabet =="ق":
                    return "kashmar"
                elif data.alphabet =="ل":
                    return "neyshabor"
                else:
                    return "mashhad"
                
            if data.city_num ==42:
                if data.alphabet =="ل":
                    return "bord skan"
                elif data.alphabet =="م":
                    return "rashtkhar"
                elif data.alphabet =="ص":
                    return "khaf"
                elif data.alphabet =="ج":
                    return "mashhad"
                elif data.alphabet =="ق":
                    return "esfarayen"
                else:
                    return "khorasan razavi,shomali"
                
            if data.city_num ==52:
                return "birjand"
            
            if data.city_num ==14:
                return "ahvaz"
            elif data.city_num ==24:
                return "khozestan"
            elif data.city_num ==34:
                return "khozestan"
            
            if data.city_num ==87:
                return "zanjan"
            if data.city_num ==97:
                if data.alphabet =="ب":
                    return "abhar"
                elif data.alphabet =="ج":
                    return "khodabandeh"
                elif data.alphabet =="د":
                    return "khoramdeh"
                else:
                    return "zanjan"
              
            if data.city_num ==86:
                return "semnan"
            if data.city_num ==96:
                if data.alphabet =="ب":
                    return "damghan"
                elif data.alphabet =="ج":
                    return "shahrood"
                elif data.alphabet =="د":
                    return "garmsar"
                elif data.alphabet =="ص":
                    return "shahrood"
                else:
                    return "semnan"
            
            if data.city_num ==85:
                return "zahedan"
            if data.city_num ==95:
                return "chabahar"
            
            if data.city_num ==63:
                return "shiraz"
            if data.city_num ==93:
                return "shiraz"
            if data.city_num ==73:
                return "fars"
            if data.city_num ==83:
                return "fars"
            
            if data.city_num ==79:
                return "ghazvin"
            if data.city_num ==89:
                return "ghazvin"
            
            if data.city_num ==16:
                return "ghom"
            
            if data.city_num ==51:
                return "sanandaj"
        
            if data.city_num ==61:
                if data.alphabet =="د":
                    return "baneh"
                elif data.alphabet =="ج":
                    return "bijar"
                elif data.alphabet =="ط":
                    return "divandareh"
                elif data.alphabet =="ل":
                    return "sarv abad"
                elif data.alphabet =="ب":
                    return "saghez"
                elif data.alphabet =="س":
                    return "ghorveh"
                elif data.alphabet =="ق":
                    return "kamyaran"
                elif data.alphabet =="ص":
                    return "marivan"
                else:
                    return "kordestan"
                
            if data.city_num ==45:
                return "kerman"
            if data.city_num ==75:
                return "kerman"
            if data.city_num ==65:
                if data.alphabet =="س":
                    return "baft"
                elif data.alphabet =="م":
                    return "bordsir"
                elif data.alphabet =="ج":
                    return "bam"
                elif data.alphabet =="ص":
                    return "jiroft"
                elif data.alphabet =="ه":
                    return "ravar"
                elif data.alphabet =="ب":
                    return "rafsanjan"
                elif data.alphabet =="ط":
                    return "zarand"
                elif data.alphabet =="د":
                    return "sirjan"
                elif data.alphabet =="ل":
                    return "shahre babak"
                elif data.alphabet =="و":
                    return "anbar abad"
                elif data.alphabet =="ق":
                    return "khnoj"
                elif data.alphabet =="ن":
                    return "manojan"
                else:
                    return "kerman"
                
            if data.city_num ==19:
                return "kermanshah"
            if data.city_num ==29:
                return "kermanshah"
            if data.city_num ==39:
                return "kermanshah"
            
            if data.city_num ==49:
                return "kohkiloye va boyerahmad"
            
            if data.city_num ==59:
                return "gorgan"
            if data.city_num ==69:
                return "golestan"
            
            if data.city_num ==46:
                return "rasht"
            if data.city_num ==56:
                if data.alphabet =="و":
                    return "amlash"
                elif data.alphabet =="ب":
                    return "bandar anzali"
                elif data.alphabet =="د":
                    return "astara"
                elif data.alphabet =="س":
                    return "talesh"
                elif data.alphabet =="ن":
                    return "rezvanshahr"
                elif data.alphabet =="ط":
                    return "rodbar"
                elif data.alphabet =="ص":
                    return "rodsar"
                elif data.alphabet =="ق":
                    return "somesara"
                elif data.alphabet =="ل":
                    return "foman"
                elif data.alphabet =="ج":
                    return "lahijan"
                elif data.alphabet =="م":
                    return "langerod"
                else:
                    return "gilan"
                
            if data.city_num ==76:
                if data.alphabet =="ج":
                    return "astaneh ashrafie"
                elif data.alphabet =="ب":
                    return "siyahkal"
                elif data.alphabet =="س":
                    return "bandar anzali"
                elif data.alphabet =="ن":
                    return "lahijan"
                elif data.alphabet =="ع":
                    return "gilan"
                else:
                    return "gilan"
            
            if data.city_num ==31:
                return "khoram abad"
            if data.city_num ==41:
                if data.alphabet =="ب":
                    return "brojerd"
                elif data.alphabet =="د":
                    return "dorod"
                elif data.alphabet =="ج":
                    return "aligodarz"
                else:
                    return "lorestan"
            
            if data.city_num ==62:
                return "sari"
            if data.city_num ==92:
                return "mazandaran"
            if data.city_num ==82:
                return "ghaem shahr,savadkoh"
            
            if data.city_num ==72:
                if data.alphabet =="و":
                    return "mahmood abad"
                elif data.alphabet =="ب":
                    return "amol"
                elif data.alphabet =="د":
                    return "tonekabon"
                elif data.alphabet =="س":
                    return "ramsar"
                elif data.alphabet =="ن":
                    return "chalos"
                elif data.alphabet =="ط":
                    return "noor"
                elif data.alphabet =="ص":
                    return "noshahr"
                elif data.alphabet =="ق":
                    return "beh shahr"
                elif data.alphabet =="ل":
                    return "ghaem shahr"
                elif data.alphabet =="ج":
                    return "babol"
                elif data.alphabet =="م":
                    return "babolsar"
                elif data.alphabet =="ی":
                    return "joybar"
                elif data.alphabet =="ه":
                    return "neka"
                else:
                    return "mazandaran"
            
            if data.city_num ==47:
                return "arak"
            if data.city_num ==57:
                if data.alphabet =="س":
                    return "tafrsh"
                elif data.alphabet =="د":
                    return "mahalat"
                elif data.alphabet =="ب":
                    return "saveh"
                elif data.alphabet =="ق":
                    return "shazand"
                else:
                    return "markazi"
                
                
            if data.city_num ==84:
                return "bandar abbas"
            if data.city_num ==94:
                return "hormozgan"
            
            if data.city_num ==18:
                return "hamedan"
            if data.city_num ==28:
                return "hamedan"
            
            if data.city_num ==54:
                return "yazd"
            if data.city_num ==64:
                if data.alphabet =="ب":
                    return "ardakan"
                elif data.alphabet =="د":
                    return "meybod"
                elif data.alphabet =="ص":
                    return "mehriz"
                elif data.alphabet =="ق":
                    return "tabas"
                elif data.alphabet =="ل":
                    return "harat"
                elif data.alphabet =="ج":
                    return "taft"
                elif data.alphabet =="م":
                    return "sedogh"
                else:
                    return "yazd"
        
        
        data["city"] = data.apply(condition, axis=1)
        data.dropna(subset=["city"],inplace=True)
        print(data.isnull().sum())
        print(data.shape)
        
        data.to_csv("complete_plates_data.csv",index=True)
        ## now we have a complete plates csv file
        
        
        
        
        





























