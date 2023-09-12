

def get_label_ld(unique_keys, scheme="bio"):
    # print("starting")
    # unique_keys = set()
    # unique_keys.add(key)
    key_list = list(set(unique_keys))
    # print(key_list)
    key_list.sort()

    label_list = ["O-OTHERS"]
    for key in key_list:
        if scheme == "bio":
            label_list.append("B-" + key)
            label_list.append("I-" + key)
        elif scheme == "bioes":
            label_list.append("B-" + key)
            label_list.append("I-" + key)
            label_list.append("E-" + key)
            label_list.append("S-" + key)
        else:
            raise NotImplementedError

    label_dict = {l: i for i, l in enumerate(label_list)}
    import json
    with open("./labels.json", "w") as outfile:
        json.dump(label_dict, outfile)
    with open("./labels.txt", "w") as label:
        for l in label_list:
            label.write(l)
            label.write('\n')
    return label_list, label_dict


# data = {
#    "vertica":"FW",
#    "insurer":"HDFC",
#    "policytype":"OD",
#    "businessType":"NEW",
#    "classes":{
#       "INSURER":{
#          "isMandatory":True
#       },
#       "REGISTRATIONNO":{
#          "isMandatory":True
#       },
#       "COMMUNICATIONSTATE":{
#          "isMandatory":True
#       },
#       "COMMUNICATIONADDRESS":{
#          "isMandatory":True
#       },
#       "COMMUNICATIONCITY":{
#          "isMandatory":True
#       },
#       "COMMUNICATIONPINCODE":{
#          "isMandatory":True
#       },
#       "POLICYPROPOSERFNAME":{
#          "isMandatory":True
#       },
#       "POLICYPROPOSERLNAME":{
#          "isMandatory":True
#       },
#       "POLICYPROPOSERTITLE":{
#          "isMandatory":True
#       },
#       "RISKENDDATE":{
#          "isMandatory":True
#       },
#       "RISKSTARTDATE":{
#          "isMandatory":True
#       },
#       "ISSUANCEDATE":{
#          "isMandatory":True
#       },
#       "POLICYNUMBER":{
#          "isMandatory":True
#       },
#       "CC":{
#          "isMandatory":True
#       },
#       "CHASSISNO":{
#          "isMandatory":True
#       },
#       "ENGINENO":{
#          "isMandatory":True
#       },
#       "MANUFACTUREYEAR":{
#          "isMandatory":True
#       },
#       "RTOLOCATION":{
#          "isMandatory":True
#       },
#       "SEATINGCAPACITY":{
#          "isMandatory":True
#       },
#       "VEHICLETYPE":{
#          "isMandatory":True
#       },
#       "BASICTPPREMIUM":{
#          "isMandatory":True
#       },
#       "GROSSPREMIUM":{
#          "isMandatory":True
#       },
#       "CGST":{
#          "isMandatory":True
#       },
#       "SGST":{
#          "isMandatory":True
#       },
#       "NETPREMIUM":{
#          "isMandatory":True
#       },
#       "SERVICETAX":{
#          "isMandatory":True
#       },
#       "TPPREMIUM":{
#          "isMandatory":True
#       },
#       "NETODPREMIUM":{
#          "isMandatory":True
#       },
#       "ODPREMIUM":{
#          "isMandatory":True
#       },
#       "TOTALIDV":{
#          "isMandatory":True
#       },
#       "PREVNCB":{
#          "isMandatory":True
#       },
#       "FUEL":{
#          "isMandatory":True
#       },
#       "POLICYPROPOSEREMAIL":{
#          "isMandatory":True
#       },
#       "PREVPOLICYNUMBER":{
#          "isMandatory":True
#       },
#       "REGISTRATIONDATE":{
#          "isMandatory":True
#       },
#       "NCB":{
#          "isMandatory":True
#       },
#       "NCBVALUE":{
#          "isMandatory":True
#       },
#       "MAKE_MODEL_VARIANT":{
#          "isMandatory":True
#       },
#       "MAKE":{
#          "isMandatory":True
#       },
#       "MODEL":{
#          "isMandatory":True
#       },
#       "VARIANT":{
#          "isMandatory":True
#       },
#       "POLICYPROPOSERMOBILE":{
#          "isMandatory":True
#       },
#       "PREVINSURER":{
#          "isMandatory":True
#       },
#       "GVW":{
#          "isMandatory":True
#       },
#       "VEHICLESUBTYPE":{
#          "isMandatory":True
#       },
#       "ODRISKSTARTDATE":{
#          "isMandatory":True
#       },
#       "ODRISKENDDATE":{
#          "isMandatory":True
#       },
#       "TPRISKSTARTDATE":{
#          "isMandatory":True
#       },
#       "TPRISKENDDATE":{
#          "isMandatory":True
#       },
#       "TOTALADDON":{
#          "isMandatory":True
#       },
#       "ALTERNATEMOBILE":{
#          "isMandatory":True
#       }
#    }
# }

#Health

data = {
      "productCategory":"FW",
      "insurer":"HDFC",
      "coverType":"individual",
      "planType":"basic",
      "classes":{
      "INSURER":{
         "isMandatory":True
      },
      "FNAME":{
         "isMandatory":True
      },
      "COMMUNICATIONSTATE":{
         "isMandatory":True
      },
      "ADDRESS":{
         "isMandatory":True
      },
      "COMMUNICATIONCITY":{
         "isMandatory":True
      },
      "COMMUNICATIONPINCODE":{
         "isMandatory":True
      },
      "LNAME":{
         "isMandatory":True
      },
      "PRIMARYRMOBILE":{
         "isMandatory":True
      },
      "GENDER":{
         "isMandatory":True
      },
      "RISKENDDATE":{
         "isMandatory":True
      },
      "RISKSTARTDATE":{
         "isMandatory":True
      },
      "ISSUANCEDATE":{
         "isMandatory":True
      },
      "POLICYNUMBER":{
         "isMandatory":True
      },
      "DOB":{
         "isMandatory":True
      },
      "INCEPTIONDATE":{
         "isMandatory":True
      },
      "SUMINSURED":{
         "isMandatory":True
      },
      "POLICYTERM":{
         "isMandatory":True
      },
      "PLANNAME":{
         "isMandatory":True
      },
      "NETPREMIUM":{
         "isMandatory":True
      },
      "CGST":{
         "isMandatory":True
      },
      "SGST":{
         "isMandatory":True
      },
      "SERVICETAX":{
         "isMandatory":True
      },
      "GROSSPREMIUM":{
         "isMandatory":True
      },
      "EMAIL":{
         "isMandatory":True
      },
      "TBL-MEDICALHISTORY":{
         "isMandatory":True
      },
      "TBL-NOMINEE":{
         "isMandatory":True
      },
      "TBL-DOB":{
         "isMandatory":True
      },
      "TBL-FNAMELNAME":{
         "isMandatory":True
      },
      "TBL-GENDER":{
         "isMandatory":True
      },
      "TBL-RELATIONSHIP":{
         "isMandatory":True
      }


   }
}


field_list = data['classes'].keys()
label_list, label_dict = get_label_ld(field_list, scheme='bioes')