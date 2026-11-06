"""Chemistry reference packet data (SHULL-CHG-0058). Every value here goes through
verify-content before the packet ships. Sources are noted per table."""

# Z, symbol, name, average atomic mass (2 decimals; [n] = mass number of the longest-lived
# isotope for elements with no standard atomic weight). IUPAC standard atomic weights.
ELEMENTS = [
 (1,"H","Hydrogen","1.01"),(2,"He","Helium","4.00"),(3,"Li","Lithium","6.94"),(4,"Be","Beryllium","9.01"),
 (5,"B","Boron","10.81"),(6,"C","Carbon","12.01"),(7,"N","Nitrogen","14.01"),(8,"O","Oxygen","16.00"),
 (9,"F","Fluorine","19.00"),(10,"Ne","Neon","20.18"),(11,"Na","Sodium","22.99"),(12,"Mg","Magnesium","24.31"),
 (13,"Al","Aluminum","26.98"),(14,"Si","Silicon","28.09"),(15,"P","Phosphorus","30.97"),(16,"S","Sulfur","32.06"),
 (17,"Cl","Chlorine","35.45"),(18,"Ar","Argon","39.95"),(19,"K","Potassium","39.10"),(20,"Ca","Calcium","40.08"),
 (21,"Sc","Scandium","44.96"),(22,"Ti","Titanium","47.87"),(23,"V","Vanadium","50.94"),(24,"Cr","Chromium","52.00"),
 (25,"Mn","Manganese","54.94"),(26,"Fe","Iron","55.85"),(27,"Co","Cobalt","58.93"),(28,"Ni","Nickel","58.69"),
 (29,"Cu","Copper","63.55"),(30,"Zn","Zinc","65.38"),(31,"Ga","Gallium","69.72"),(32,"Ge","Germanium","72.63"),
 (33,"As","Arsenic","74.92"),(34,"Se","Selenium","78.97"),(35,"Br","Bromine","79.90"),(36,"Kr","Krypton","83.80"),
 (37,"Rb","Rubidium","85.47"),(38,"Sr","Strontium","87.62"),(39,"Y","Yttrium","88.91"),(40,"Zr","Zirconium","91.22"),
 (41,"Nb","Niobium","92.91"),(42,"Mo","Molybdenum","95.95"),(43,"Tc","Technetium","[98]"),(44,"Ru","Ruthenium","101.07"),
 (45,"Rh","Rhodium","102.91"),(46,"Pd","Palladium","106.42"),(47,"Ag","Silver","107.87"),(48,"Cd","Cadmium","112.41"),
 (49,"In","Indium","114.82"),(50,"Sn","Tin","118.71"),(51,"Sb","Antimony","121.76"),(52,"Te","Tellurium","127.60"),
 (53,"I","Iodine","126.90"),(54,"Xe","Xenon","131.29"),(55,"Cs","Cesium","132.91"),(56,"Ba","Barium","137.33"),
 (57,"La","Lanthanum","138.91"),(58,"Ce","Cerium","140.12"),(59,"Pr","Praseodymium","140.91"),(60,"Nd","Neodymium","144.24"),
 (61,"Pm","Promethium","[145]"),(62,"Sm","Samarium","150.36"),(63,"Eu","Europium","151.96"),(64,"Gd","Gadolinium","157.25"),
 (65,"Tb","Terbium","158.93"),(66,"Dy","Dysprosium","162.50"),(67,"Ho","Holmium","164.93"),(68,"Er","Erbium","167.26"),
 (69,"Tm","Thulium","168.93"),(70,"Yb","Ytterbium","173.05"),(71,"Lu","Lutetium","174.97"),(72,"Hf","Hafnium","178.49"),
 (73,"Ta","Tantalum","180.95"),(74,"W","Tungsten","183.84"),(75,"Re","Rhenium","186.21"),(76,"Os","Osmium","190.23"),
 (77,"Ir","Iridium","192.22"),(78,"Pt","Platinum","195.08"),(79,"Au","Gold","196.97"),(80,"Hg","Mercury","200.59"),
 (81,"Tl","Thallium","204.38"),(82,"Pb","Lead","207.20"),(83,"Bi","Bismuth","208.98"),(84,"Po","Polonium","[209]"),
 (85,"At","Astatine","[210]"),(86,"Rn","Radon","[222]"),(87,"Fr","Francium","[223]"),(88,"Ra","Radium","[226]"),
 (89,"Ac","Actinium","[227]"),(90,"Th","Thorium","232.04"),(91,"Pa","Protactinium","231.04"),(92,"U","Uranium","238.03"),
 (93,"Np","Neptunium","[237]"),(94,"Pu","Plutonium","[244]"),(95,"Am","Americium","[243]"),(96,"Cm","Curium","[247]"),
 (97,"Bk","Berkelium","[247]"),(98,"Cf","Californium","[251]"),(99,"Es","Einsteinium","[252]"),(100,"Fm","Fermium","[257]"),
 (101,"Md","Mendelevium","[258]"),(102,"No","Nobelium","[259]"),(103,"Lr","Lawrencium","[266]"),(104,"Rf","Rutherfordium","[267]"),
 (105,"Db","Dubnium","[268]"),(106,"Sg","Seaborgium","[269]"),(107,"Bh","Bohrium","[270]"),(108,"Hs","Hassium","[269]"),
 (109,"Mt","Meitnerium","[278]"),(110,"Ds","Darmstadtium","[281]"),(111,"Rg","Roentgenium","[282]"),(112,"Cn","Copernicium","[285]"),
 (113,"Nh","Nihonium","[286]"),(114,"Fl","Flerovium","[289]"),(115,"Mc","Moscovium","[290]"),(116,"Lv","Livermorium","[293]"),
 (117,"Ts","Tennessine","[294]"),(118,"Og","Oganesson","[294]"),
]

# Pauling electronegativity, from Wikipedia "Electronegativities of the elements (data page)",
# read 2026-11-06. Shown to 2 decimals. Noble gases left blank (user decision, SHULL-CHG-0058).
# Elements with no tabulated value (Pm, Eu, Yb, Z >= 104) are blank. Fr is given there as
# ">0.79"; Pauling's 0.7 is used.
EN = {"H":2.20,"Li":0.98,"Be":1.57,"B":2.04,"C":2.55,"N":3.04,"O":3.44,"F":3.98,
 "Na":0.93,"Mg":1.31,"Al":1.61,"Si":1.90,"P":2.19,"S":2.58,"Cl":3.16,
 "K":0.82,"Ca":1.00,"Sc":1.36,"Ti":1.54,"V":1.63,"Cr":1.66,"Mn":1.55,"Fe":1.83,"Co":1.88,"Ni":1.91,
 "Cu":1.90,"Zn":1.65,"Ga":1.81,"Ge":2.01,"As":2.18,"Se":2.55,"Br":2.96,
 "Rb":0.82,"Sr":0.95,"Y":1.22,"Zr":1.33,"Nb":1.6,"Mo":2.16,"Tc":1.9,"Ru":2.2,"Rh":2.28,"Pd":2.20,
 "Ag":1.93,"Cd":1.69,"In":1.78,"Sn":1.96,"Sb":2.05,"Te":2.1,"I":2.66,
 "Cs":0.79,"Ba":0.89,"La":1.1,"Hf":1.3,"Ta":1.5,"W":2.36,"Re":1.9,"Os":2.2,"Ir":2.20,"Pt":2.28,
 "Au":2.54,"Hg":2.00,"Tl":1.62,"Pb":2.33,"Bi":2.02,"Po":2.0,"At":2.2,
 "Fr":0.7,"Ra":0.9,"Ac":1.1,
 "Ce":1.12,"Pr":1.13,"Nd":1.14,"Sm":1.17,"Gd":1.2,"Tb":1.21,"Dy":1.22,"Ho":1.23,"Er":1.24,"Tm":1.25,"Lu":1.27,
 "Th":1.3,"Pa":1.5,"U":1.38,"Np":1.36,"Pu":1.28,"Am":1.3,"Cm":1.28,"Bk":1.3,"Cf":1.3,"Es":1.3,"Fm":1.3,
 "Md":1.3,"No":1.3,"Lr":1.3}
NOBLE = {"He","Ne","Ar","Kr","Xe","Rn","Og"}

# (group, period) for the main table; La and Ac sit in group 3, Ce-Lu and Th-Lr in the f rows.
def position(z):
    if z == 1: return 1, 1
    if z == 2: return 18, 1
    for start, period in ((3, 2), (11, 3)):
        if start <= z < start + 8:
            i = z - start
            return (i + 1 if i < 2 else i + 11), period
    if 19 <= z <= 36: return z - 18, 4
    if 37 <= z <= 54: return z - 36, 5
    for base, period in ((55, 6), (87, 7)):
        if z in (base, base + 1): return z - base + 1, period
        if z == base + 2: return 3, period                     # La, Ac
        if base + 3 <= z <= base + 16: return ("f", period, z - base - 3)
        if base + 17 <= z <= base + 31: return z - base - 13, period
    raise ValueError(z)

# 37 polyatomic ions, grouped by charge; True = memorize (the 15). SHULL-CHG-0058.
# Formula markup: digits after a letter or ")" are subscripts; ^ starts the charge.
POLYATOMIC = [
 ("1+", [("ammonium","NH4^+",True),("hydronium","H3O^+",True)]),
 ("2+", [("mercury(I)","Hg2^2+",False)]),
 ("1−", [("acetate","C2H3O2^-",True),("hydrogen carbonate (bicarbonate)","HCO3^-",True),
         ("chlorate","ClO3^-",True),("cyanide","CN^-",True),("hydroxide","OH^-",True),
         ("nitrate","NO3^-",True),("nitrite","NO2^-",True),("permanganate","MnO4^-",True),
         ("perchlorate","ClO4^-",False),("chlorite","ClO2^-",False),("hypochlorite","ClO^-",False),
         ("bromate","BrO3^-",False),("iodate","IO3^-",False),("periodate","IO4^-",False),
         ("hydrogen sulfate (bisulfate)","HSO4^-",False),("hydrogen sulfite (bisulfite)","HSO3^-",False),
         ("hydrogen sulfide (bisulfide)","HS^-",False),("dihydrogen phosphate","H2PO4^-",False),
         ("thiocyanate","SCN^-",False),("cyanate","OCN^-",False)]),
 ("2−", [("carbonate","CO3^2-",True),("chromate","CrO4^2-",True),("sulfate","SO4^2-",True),
         ("sulfite","SO3^2-",True),("dichromate","Cr2O7^2-",False),("hydrogen phosphate","HPO4^2-",False),
         ("oxalate","C2O4^2-",False),("peroxide","O2^2-",False),("thiosulfate","S2O3^2-",False),
         ("silicate","SiO3^2-",False)]),
 ("3−", [("phosphate","PO4^3-",True),("phosphite","PO3^3-",False),("arsenate","AsO4^3-",False),
         ("borate","BO3^3-",False)]),
]

# Metals with more than one common charge, then fixed-charge exceptions. SHULL-CHG-0058.
MULTI_CHARGE = [
 ("Copper", [("Cu^+","copper(I)"),("Cu^2+","copper(II)")]),
 ("Iron", [("Fe^2+","iron(II)"),("Fe^3+","iron(III)")]),
 ("Lead", [("Pb^2+","lead(II)"),("Pb^4+","lead(IV)")]),
 ("Tin", [("Sn^2+","tin(II)"),("Sn^4+","tin(IV)")]),
 ("Mercury", [("Hg2^2+","mercury(I)"),("Hg^2+","mercury(II)")]),
 ("Cobalt", [("Co^2+","cobalt(II)"),("Co^3+","cobalt(III)")]),
 ("Nickel", [("Ni^2+","nickel(II)"),("Ni^3+","nickel(III)")]),
 ("Chromium", [("Cr^2+","chromium(II)"),("Cr^3+","chromium(III)")]),
 ("Manganese", [("Mn^2+","manganese(II)"),("Mn^3+","manganese(III)")]),
 ("Gold", [("Au^+","gold(I)"),("Au^3+","gold(III)")]),
]
FIXED_CHARGE = [("Silver","Ag^+"),("Zinc","Zn^2+"),("Cadmium","Cd^2+")]

# Solubility in water at about 25 °C. S = soluble (more than 1 g per 100 mL), SS = slightly
# soluble (0.1-1 g), I = insoluble (less than 0.1 g), X = reacts with water or does not form.
ANIONS = ["NO3^-","C2H3O2^-","ClO3^-","Cl^-","Br^-","I^-","SO4^2-","OH^-","CO3^2-","PO4^3-","S^2-"]
ANION_NAMES = ["nitrate","acetate","chlorate","chloride","bromide","iodide","sulfate","hydroxide","carbonate","phosphate","sulfide"]
SOLUBILITY = [  #            NO3 Ac  ClO3 Cl  Br  I   SO4 OH  CO3 PO4 S
 ("NH4^+",  "ammonium",   "S   S   S   S   S   S   S   S   S   S   S"),
 ("Na^+",   "sodium",     "S   S   S   S   S   S   S   S   S   S   S"),
 ("K^+",    "potassium",  "S   S   S   S   S   S   S   S   S   S   S"),
 ("Mg^2+",  "magnesium",  "S   S   S   S   S   S   S   I   I   I   X"),
 ("Ca^2+",  "calcium",    "S   S   S   S   S   S   SS  SS  I   I   X"),
 ("Sr^2+",  "strontium",  "S   S   S   S   S   S   I   SS  I   I   X"),
 ("Ba^2+",  "barium",     "S   S   S   S   S   S   I   S   I   I   X"),
 ("Al^3+",  "aluminum",   "S   S   S   S   S   S   S   I   X   I   X"),
 ("Mn^2+",  "manganese(II)","S S   S   S   S   S   S   I   I   I   I"),
 ("Fe^2+",  "iron(II)",   "S   S   S   S   S   S   S   I   I   I   I"),
 ("Fe^3+",  "iron(III)",  "S   S   S   S   S   X   S   I   X   I   X"),
 ("Co^2+",  "cobalt(II)", "S   S   S   S   S   S   S   I   I   I   I"),
 ("Ni^2+",  "nickel(II)", "S   S   S   S   S   S   S   I   I   I   I"),
 ("Cu^2+",  "copper(II)", "S   S   S   S   S   X   S   I   I   I   I"),
 ("Zn^2+",  "zinc",       "S   S   S   S   S   S   S   I   I   I   I"),
 ("Ag^+",   "silver",     "S   SS  S   I   I   I   SS  I   I   I   I"),
 ("Hg2^2+", "mercury(I)", "S   SS  S   I   I   I   I   I   I   I   I"),
 ("Pb^2+",  "lead(II)",   "S   S   S   SS  SS  I   I   I   I   I   I"),
]
SOLUBILITY_RULES = [
 "Compounds of Group 1 ions and NH<sub>4</sub><sup>+</sup> are soluble. So are all nitrates and chlorates, and nearly all acetates.",
 "Chlorides, bromides and iodides are soluble, except with Ag<sup>+</sup>, Hg<sub>2</sub><sup>2+</sup> and Pb<sup>2+</sup>.",
 "Sulfates are soluble, except with Sr<sup>2+</sup>, Ba<sup>2+</sup>, Pb<sup>2+</sup> and Hg<sub>2</sub><sup>2+</sup>. Ca<sup>2+</sup> and Ag<sup>+</sup> sulfates are slightly soluble.",
 "Hydroxides are insoluble, except with Group 1, NH<sub>4</sub><sup>+</sup> and Ba<sup>2+</sup>. Ca<sup>2+</sup> and Sr<sup>2+</sup> hydroxides are slightly soluble.",
 "Carbonates, phosphates and sulfides are insoluble, except with Group 1 and NH<sub>4</sub><sup>+</sup>.",
]

# Activity series, most active first.
ACTIVITY_METALS = [
 ("Reacts with cold water, steam and acids", ["Li","K","Ba","Sr","Ca","Na"]),
 ("Reacts with steam and acids", ["Mg","Al","Mn","Zn","Cr","Fe","Cd"]),
 ("Reacts with acids", ["Co","Ni","Sn","Pb"]),
 (None, ["H<sub>2</sub>"]),
 ("Does not replace hydrogen from acids", ["Cu","Hg","Ag","Pt","Au"]),
]
ACTIVITY_HALOGENS = ["F<sub>2</sub>","Cl<sub>2</sub>","Br<sub>2</sub>","I<sub>2</sub>"]

STRONG_ACIDS = [("HCl","hydrochloric acid"),("HBr","hydrobromic acid"),("HI","hydroiodic acid"),
                ("HNO3","nitric acid"),("H2SO4","sulfuric acid"),("HClO4","perchloric acid")]
STRONG_BASES = [("LiOH","lithium hydroxide"),("NaOH","sodium hydroxide"),("KOH","potassium hydroxide"),
                ("RbOH","rubidium hydroxide"),("CsOH","cesium hydroxide"),("Ca(OH)2","calcium hydroxide"),
                ("Sr(OH)2","strontium hydroxide"),("Ba(OH)2","barium hydroxide")]

# Specific heat, J/(g·°C), near room temperature (water phases at their own temperatures).
SPECIFIC_HEATS = [
 ("Water (liquid)","4.184"),("Ice","2.06"),("Steam","2.01"),("Ethanol","2.44"),
 ("Aluminum","0.897"),("Glass","0.84"),("Granite","0.79"),("Iron","0.449"),("Nickel","0.444"),
 ("Zinc","0.388"),("Copper","0.385"),("Brass","0.380"),("Silver","0.235"),("Tin","0.228"),
 ("Lead","0.129"),("Gold","0.129"),
]
