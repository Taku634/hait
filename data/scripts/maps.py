# Building map (address keyword -> building, campus, operator) and group keyword map
# IHH Singapore campuses: Mount Elizabeth Orchard (MEH + Mount Elizabeth Medical Centre), Mount Elizabeth Novena (MNH + Mount Elizabeth Novena Specialist Centre),
# Gleneagles (GEH + Gleneagles Medical Centre / Annexe), Parkway East (PEH + Parkway East Medical Centre)
import re

BUILDINGS = [
    # (regex on address, building label, campus, IHH-campus?)
    (r"3 Mount Elizabeth\b|Mount Elizabeth Medical Centre", "Mount Elizabeth Medical Centre (3 Mount Elizabeth)", "MEH", True),
    (r"38 Irrawaddy|Mount Elizabeth Novena Specialist Centre", "Mount Elizabeth Novena Specialist Centre (38 Irrawaddy Rd)", "MNH", True),
    (r"6 Napier Road|Gleneagles Medical Centre", "Gleneagles Medical Centre (6 Napier Rd)", "GEH", True),
    (r"6A Napier Road|Gleneagles Hospital Annexe|Annexe Block", "Gleneagles Hospital Annexe (6A Napier Rd)", "GEH", True),
    (r"319 Joo Chiat|Parkway East Medical Centre", "Parkway East Medical Centre (319 Joo Chiat Pl)", "PEH", True),
    (r"321 Joo Chiat|Parkway East Hospital", "Parkway East Hospital (321 Joo Chiat Pl)", "PEH", True),
    (r"101 Irrawaddy|Royal Square", "Royal Square at Novena (101 Irrawaddy Rd)", "Novena-other", False),
    (r"10 Sinaran|Novena Medical Cent", "Novena Medical Center (10 Sinaran Dr)", "Novena-other", False),
    (r"8 Sinaran|Novena Specialist Cent", "Novena Specialist Center (8 Sinaran Dr)", "Novena-other", False),
    (r"290 Orchard|Paragon", "Paragon Medical (290 Orchard Rd)", "Orchard-other", False),
    (r"1 Orchard Boulevard|Camden Medical", "Camden Medical Centre (1 Orchard Blvd)", "Orchard-other", False),
    (r"304 Orchard|Lucky Plaza", "Lucky Plaza (304 Orchard Rd)", "Orchard-other", False),
    (r"1 Farrer Park Station|Connexion|Farrer Park Medical", "Farrer Park Medical Centre / Connexion", "Farrer Park", False),
    (r"820 Thomson|Mount Alvernia", "Mount Alvernia Medical Centre (820 Thomson Rd)", "Mt Alvernia", False),
    (r"339 Thomson|Thomson Medical Centre", "Thomson Medical Centre (339 Thomson Rd)", "Thomson", False),
    (r"585 North Bridge|Raffles Hospital|Raffles Specialist", "Raffles Hospital / Specialist Centre", "Raffles", False),
    (r"Parkway MediCentre|MediCentre|Woodleigh Mall|Bidadari Park", "Parkway MediCentre (IHH community clinic)", "IHH-community", True),
    (r"HMI Medical Centre|Farrer Park Station|12 Farrer Par", "HMI Medical Centre / Farrer Park (12 Farrer Park Station Rd)", "Farrer Park", False),
    (r"Mount Elizabeth Royal Square|Royal Square @ Novena \(IHH", "Mount Elizabeth Royal Square", "Novena-other", True),
]

def building(addr):
    if not addr:
        return ("(no address)", "unknown", False)
    for rx, label, campus, ihh in BUILDINGS:
        if re.search(rx, addr, re.I):
            return (label, campus, ihh)
    return ("Other: " + addr, "other", False)

# Group keyword map: regex on clinic name -> group (brand under the group)
GROUPS = [
    # Tamarind Health (Templewater / 65 Equity Partners)
    (r"Parkway Cancer Centre|TalkMed|Singapore Cancer Centre", "Tamarind Health", "Parkway Cancer Centre / TalkMed"),
    (r"OncoCare", "Tamarind Health", "OncoCare"),
    (r"Novena Heart", "Tamarind Health", "Novena Heart Centre"),
    (r"Solis Breast|Luma Women|Singapore Breast Surgery", "Tamarind Health", "Solis / Luma"),
    (r"Rare Cancer Centre", "Tamarind Health", "Rare Cancer Centre"),
    # HMI Medical (EQT)
    (r"Harley Street", "HMI Medical", "Harley Street Heart & Vascular / Oncology"),
    (r"Eagle Eye", "HMI Medical", "Eagle Eye Centre"),
    (r"Advanced Urology", "HMI Medical", "Advanced Urology Associates"),
    (r"StarMed", "HMI Medical", "StarMed Specialist Centre"),
    (r"HMI Medical|HMI Group", "HMI Medical", "HMI"),
    # Foundation Healthcare (SGX: listed 2026)
    (r"PanAsia Surg", "Foundation Healthcare", "PanAsia Surgery"),
    (r"Pinnacle Orthopaedic|Pinnacle Ortho", "Foundation Healthcare", "Pinnacle Orthopaedic"),
    (r"The Heart Practice|Heart Matters|Heart Specialist International|The Heart Doctors|Gramercy Heart", "Foundation Healthcare", "Cardiology brands"),
    (r"Lang Eye", "Foundation Healthcare", "Lang Eye Centre"),
    (r"Neurosurgery Partners", "Foundation Healthcare", "Neurosurgery Partners"),
    (r"Colorectal Clinic Associates|Digestive Surgery|Nexus Surgical|NSG Medical", "Foundation Healthcare", "Surgery brands"),
    (r"Hand Surgery Holdings|HHJ ENT|Rhinoplasty Clinic|Winston Tan", "Foundation Healthcare", "Other brands"),
    (r"Orchard Surgery Cent|Care IVF|Aspire Centre for Women|Singapore Women'?s Medical|Singapore Children'?s Medical", "Foundation Healthcare", "Women/children/IVF brands"),
    (r"Capernaum Neurology|Ascension Medical|Abel Soh|Paul Wong AICM|Orthopaedic Associates Medical Group|Foundation Healthcare|Serene Leo", "Foundation Healthcare", "Other brands"),
    # SMG (Singapore Medical Group; CHA Healthcare)
    (r"\bSMG\b|Singapore Medical Group|Lifescan|LSC Eye|Astra Women|The Cancer Centre|The Breast Clinic|The Obstetrics & Gynaecology Centre|The Obstetrics And Gynaecology Centre|Kids Clinic|The Dental Studio|SW1 Clinic|Annabelle|Cardiac Centre International|Beng Surgery|Wellness Gynaecology", "Singapore Medical Group (SMG)", "SMG"),
    # Icon (EQT)
    (r"Icon Cancer", "Icon Group", "Icon Cancer Centre"),
    # Curie
    (r"Curie Oncology", "Curie Oncology", "Curie"),
    # gutCARE
    (r"gutCARE|Gut Care", "gutCARE", "gutCARE"),
    # HC Surgical
    (r"HC Surgical|HC Endoscopy|HC Ming|HC Orthopaedic|Heah Colorectal|Heah Endoscopy|Lai Endoscopy|Goh Minghui Endoscopy|Jason Lim Endoscopy|The Ming Clinic|Total Orthopaedic Care|LS Lee Surgery|Tampines Endoscopy|Endoscopy, Veins & Piles|ACMS Medical", "HC Surgical Specialists", "HC Surgical"),
    # OUE Healthcare / O2 / Healthway
    (r"O2 Healthcare|O2 Lung|The Respiratory Practice|Healthway|Nobel|Cura Day|Urohealth", "OUE Healthcare / Healthway", "OUE"),
    # Beyond Medical
    (r"Beyond Medical|Beyond Cardiac|Beyond Surgical|Beyond Ortho|Assure Urology|Cadence Heart|Aglow ENT|Advanced Brain and Spine", "Beyond Medical Group", "Beyond"),
    # Thomson
    (r"Thomson Medical|Thomson Specialist|Thomson Women|Thomson Paediatric|Thomson Surgical|Thomson Fertility", "Thomson Medical Group", "Thomson"),
    # Raffles
    (r"Raffles Medical|Raffles Hospital|Raffles Specialist", "Raffles Medical Group", "Raffles"),
    # Singapore O&G
    (r"Singapore O&G|SOG\b", "Singapore O&G", "SOG"),
    # Cardiac Care Partners / Alfa Medicus / others
    (r"Cardiac Care Partners", "Cardiac Care Partners", "CCP"),
    (r"Alfa Medicus|Novena Surgery|Aptus Surgery|Oxford Orthopaedics|Aurora Eye|Alfa Lasik|Novaptus", "Alfa Medicus (ICG)", "Alfa"),
    (r"Orthopaedics International", "Orthopaedics International", "OI"),
    (r"Asian Healthcare Specialists|Doctor Anywhere", "Doctor Anywhere / AHS", "AHS"),
    (r"Royal Healthcare", "Royal Healthcare (Sojitz)", "Royal"),
    (r"Livingstone", "Livingstone Health", "Livingstone"),
    (r"Paincare", "Singapore Paincare", "Paincare"),
    (r"ISEC|Asia Pacific Eye", "ISEC Healthcare (Aier)", "ISEC"),
    (r"Virtus Fertility", "Virtus Health", "Virtus"),
    (r"AARO|Asian Alliance Radiation", "AARO", "AARO"),
    (r"The ENT Clinic|Fullerton", "Fullerton Health", "Fullerton"),
    (r"Specialist Dental Group", "Specialist Dental Group", "SDG"),
    (r"Eye & Retina Surgeons", "Eye & Retina Surgeons", "ERS"),
    (r"Ascle", "Ascle Healthcare", "Ascle"),
    (r"Radiology Department|Department of Radiology|Parkway Radiology|Parkway Laborator|Mount Elizabeth Proton|Mount Elizabeth Genomic|Mount Elizabeth Fertility|Mount Elizabeth Haematology", "IHH hospital department / centre", "IHH"),
]

def group_for_clinic(name):
    if not name:
        return None
    for rx, g, brand in GROUPS:
        if re.search(rx, name, re.I):
            return (g, brand)
    return None
