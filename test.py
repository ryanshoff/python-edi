import string
import random
from datetime import datetime

import pythonedi

g = pythonedi.EDIGenerator()
g.element_delimiter = "*"
#g.segment_delimiter = "\n"
#g.data_delimiter = "`"

interchange_control_number = 12345
group_control_number = 23456
transaction_control_number = 1


#pythonedi.explain("856", "ITA")
edi_data = {
    "ISA": [
        "00", # Authorization Information Qualifier
        "           ", # Authorization Information
        "00", # Security Information Qualifier
        "           ", # Security Information
        "ZZ", # Interchange Sender ID Qualifier
        "B4209T0", # Interchange Sender ID
        "ZZ", # Interchange Receiver ID Qualifier
        "005070479SJ", # Interchange Receiver ID
        datetime(2018, 6, 24, 10, 00), # Interchange Date
        datetime(2018, 6, 24, 10, 00), # Interchange Time
        "U", # Interchange Control Standards Identifier
        "00200", # Interchange Control Version Number
        interchange_control_number, # Interchange Control Number
        "0", # Acknowledgment Requested
        "P", # Usage Indicator
        ">" # Component Element Separator
    ],
    "GS": [
        "SH", # Functional Identifier Code
        "B4209T0", # Application Sender's Code
        "SJ", # Application Receiver's Code
        datetime(2018, 6, 24, 10, 00), # Date
        datetime(2018, 6, 24, 10, 00), # Time
        group_control_number, # Group Control Number
        "X", # Responsible Agency Code
        "003020", # Version/Release/Industry Identifier Code
    ],
    "ST": [
        "856", # Transaction Set Identifier Code: Invoice
        transaction_control_number # Transaction Set Control Number
    ],
    "BSN": [
        "00",  # 00 original  05 replace
        "shippernumber",
        datetime(2018, 6, 24, 10, 00), # Date
        datetime(2018, 6, 24, 10, 00), # Time
    ],
    "L_DTM": [
    {
    "DTM": [
        "011", # Date/Time Qualifier:  011  shipped
        datetime(2018, 6, 20, 10, 00), # Date
        datetime(2018, 6, 20, 10, 00) # Date
    ],
    },
    {
    "DTM": [
        "017", # Date/Time Qualifier:  017 estimaged arrival
        datetime(2018, 6, 20, 10, 00),# Date
        datetime(2018, 6, 20, 10, 00) # Date
    ],
    }
    ],
    "HL": [
        "1",
        None,
        "S"
    ],
    "MEA": [
        "PD",  #physical dimensions
        "G",   #gross weight
        "12345",  #value
        "LB"      # unit
    ],
    "TD1": [ #carrier details
        "RCK71",    # container
        "19"        # qty
    ],
    "TD5": [
        "B",        # origin
        "2",        # 2 SCAC code 92 Cat code
        "E451",     # code
        "T"         # method or type of transport
    ],
    "REF": [        # heat code could be here
        "CN",       # pro #
        "FREIGHT COLLECT"
    ],
    "FOB": [
        "CC"        # cc collect po prepaid only pp prepaid (by seller)
    ],
    "L_N1": [
        {
            "N1": [
                "SF", # ship from
                None, # Name
                "16", # ID Code Qualifier: Assigned by seller
                "61548" # ID number
            ],
        },
        {
            "N1": [
                "SU", # supplier
                None, # Name
                "91", # ID Code Qualifier: Assigned by seller
                "US" # ID number
            ],
        },
        {
            "N1": [
                "SF", # ship from
                None, # Name
                "92", # ID Code Qualifier: Assigned by seller
                "A12340" # ID number
            ],
        }
    ],
    "L_HL": [
        {
            "HL": [ 
                "2",    # hl number
                "1",    # parent
                "I",   # item
            ],
            "LIN": [
                None,
                "BP",
                "2762414",  # buyer's part number
                "CH",    # country of origin
                "US",
                "EC",    # ec
                "04"
            ],
            "SN1": [
                None,
                "285",  # qty
                "EA"    # uom
            ],
            "PRF": [
                "55500012345",   # po
                None,
                None,
                None,
                "1"             # po line number
            ],
            "REF": [
                "PK",
                "S0073885",      # packing list number
            ],
            "CLD": [
                "19",       # number of containers
                "15",       # qty in one container
                "RCK71",    # container code
            ],
            "L_REF2": [
                {
                    "REF": [
                        "LS",
                        "123434354"   # container barcode
                    ],
                },
                {
                    "REF": [
                        "LS",
                        "123434355"
                    ],
                }
            ]
        }
    ],
    "CTT": [
        "0",
        "0",
    ],
    "SE": [
        "0",
        transaction_control_number
    ],
    "GE": [
        "1",
        group_control_number
    ],
    "IEA": [
        "1",
        interchange_control_number
    ],
}

message = g.build(edi_data)
print("\n\n" + message)
