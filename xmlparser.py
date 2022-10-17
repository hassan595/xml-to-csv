

import csv
import xmltodict

with open('CustomerMgmt.xml') as file:
    filedata = file.read()
    
data = xmltodict.parse(filedata)

rows = []
headers = ['tpcdi', 'actionType', 'actionTS', 'c_dob', 'c_gndr', 'c_id', 'c_tax_id', 'c_tier', 'customer_name', 'c_f_name', 'c_l_name', 'c_m_name', 'c_adline1', 'c_adline2', 'c_city', 'c_ctry', 'c_state_prov', 'c_zipcode', 'c_prim_email', 'c_alt_email', 'c_phone_1_c_ctry_code', 'c_phone_1_c_area_code', 'c_phone_1_c_local', 'c_phone_1_c_ext', 'c_phone_2_c_ctry_code', 'c_phone_2_c_area_code', 'c_phone_2_c_local', 'c_phone_2_c_ext', 'c_phone_3_c_ctry_code', 'c_phone_3_c_area_code', 'c_phone_3_c_local', 'c_phone_3_c_ext', 'c_lcl_tx_id', 'c_nat_tx_id', 'ca_id', 'ca_tax_st', 'ca_b_id', 'ca_name']
rows.append (headers)

tpcdi = data['TPCDI:Actions']['@xmlns:TPCDI'] #0
actions = data['TPCDI:Actions']['TPCDI:Action']

count = 0
for action in data['TPCDI:Actions']['TPCDI:Action']:
    try:
        actionTYPE = action['@ActionType'] #1
    except:
        actionTYPE=''

    try:
        actionTS = action['@ActionTS'] #2
    except:
        actionTS=''

    try:
        customer = action['Customer']
    except:
        customer=''

    try:
        c_dob = customer['@C_DOB'] #3
    except:
        c_dob=''

    try:
        c_gndr = customer['@C_GNDR'] #4
    except:
        c_gndr=''

    try:
        c_id = customer['@C_ID'] #5
    except:
        c_id=''

    try:
        c_tax_id = customer['@C_TAX_ID'] #6
    except:
        c_tax_id=''

    try:
        c_tier = customer['@C_TIER'] #7  
    except:
        c_tier=''

    try:
        customer_name = customer['Name'] #8
    except:
        customer_name=''

    try:
        c_f_name = customer_name['C_F_NAME'] #9
    except:
        c_f_name=''

    try:
        c_l_name = customer_name['C_L_NAME'] #10
    except:
        c_l_name=''

    try:
        c_m_name = customer_name['C_M_NAME'] #11  
    except:
        c_m_name=''

    try:
        customer_address = customer['Address']
    except:
        customer_address=''

    try:
        c_adline1 = customer_address['C_ADLINE1'] #12
    except:
        c_adline1=''

    try:
        c_adline2 = customer_address['C_ADLINE2'] #13
    except:
        c_adline2=''

    try:
        c_city = customer_address['C_CITY'] #14
    except:
        c_city=''

    try:
        c_ctry = customer_address['C_CTRY'] #15
    except:
        c_ctry=''

    try:
        c_state_prov = customer_address['C_STATE_PROV'] #16
    except:
        c_state_prov=''

    try:
        c_zipcode = customer_address['C_ZIPCODE'] #17
    except:
        c_zipcode=''

    try:
        customer_contactinfo = customer['ContactInfo']
    except:
        customer_contactinfo=''

    try:
        c_prim_email = customer_contactinfo['C_PRIM_EMAIL'] #18
    except:
        c_prim_email=''

    try:
        c_alt_email = customer_contactinfo['C_ALT_EMAIL'] #19
    except:
        c_alt_email=''

    try:
        c_phone_1_c_ctry_code = customer_contactinfo['C_PHONE_1']['C_CTRY_CODE'] #20
    except:
        c_phone_1_c_ctry_code=''

    try:
        c_phone_1_c_area_code = customer_contactinfo['C_PHONE_1']['C_AREA_CODE'] #21
    except:
        c_phone_1_c_area_code=''

    try:
        c_phone_1_c_local = customer_contactinfo['C_PHONE_1']['C_LOCAL'] #22
    except:
        c_phone_1_c_local=''

    try:
        c_phone_1_c_ext = customer_contactinfo['C_PHONE_1']['C_EXT'] #23
    except:
        c_phone_1_c_ext=''

    try:
        c_phone_2_c_ctry_code = customer_contactinfo['C_PHONE_2']['C_CTRY_CODE'] #24
    except:
        c_phone_2_c_ctry_code=''

    try:
        c_phone_2_c_area_code = customer_contactinfo['C_PHONE_2']['C_AREA_CODE'] #25
    except:
        c_phone_2_c_area_code=''

    try:
        c_phone_2_c_local = customer_contactinfo['C_PHONE_2']['C_LOCAL'] #26
    except:
        c_phone_2_c_local=''

    try:
        c_phone_2_c_ext = customer_contactinfo['C_PHONE_2']['C_EXT'] #27
    except:
        c_phone_2_c_ext=''

    try:
        c_phone_3_c_ctry_code = customer_contactinfo['C_PHONE_3']['C_CTRY_CODE'] #28
    except:
        c_phone_3_c_ctry_code=''

    try:
        c_phone_3_c_area_code = customer_contactinfo['C_PHONE_3']['C_AREA_CODE'] #29
    except:
        c_phone_3_c_area_code=''

    try:
        c_phone_3_c_local = customer_contactinfo['C_PHONE_3']['C_LOCAL'] #30
    except:
        c_phone_3_c_local=''

    try:
        c_phone_3_c_ext = customer_contactinfo['C_PHONE_3']['C_EXT'] #31
    except:
        c_phone_3_c_ext=''

    try:
        customer_taxinfo = customer['TaxInfo']
    except:
        customer_taxinfo=''

    try:
        c_lcl_tx_id = customer_taxinfo['C_LCL_TX_ID'] #32
    except:
        c_lcl_tx_id=''

    try:
        c_nat_tx_id = customer_taxinfo['C_NAT_TX_ID'] #33
    except:
        c_nat_tx_id=''

    try:
        customer_account = customer['Account']
    except:
        customer_account=''

    try:
        ca_id = customer_account['@CA_ID'] #34
    except:
        ca_id=''

    try:
        ca_tax_st = customer_account['@CA_TAX_ST'] #35  
    except:
        ca_tax_st=''

    try:
        ca_b_id = customer_account['CA_B_ID'] #36
    except:
        ca_b_id=''

    try:
        ca_name = customer_account['CA_NAME'] #37
    except:
        ca_name=''

    
    rows.append ([tpcdi,actionTYPE, actionTS, c_dob, c_gndr, c_id, c_tax_id, c_tier, customer_name, c_f_name, c_l_name, c_m_name, c_adline1, c_adline2, c_city, c_ctry, c_state_prov, c_zipcode, c_prim_email, c_alt_email, c_phone_1_c_ctry_code, c_phone_1_c_area_code, c_phone_1_c_local, c_phone_1_c_ext, c_phone_2_c_ctry_code, c_phone_2_c_area_code, c_phone_2_c_local, c_phone_2_c_ext, c_phone_3_c_ctry_code, c_phone_3_c_area_code, c_phone_3_c_local, c_phone_3_c_ext, c_lcl_tx_id, c_nat_tx_id, ca_id, ca_tax_st, ca_b_id, ca_name])
    count += 1
    print(count)

with open('C:\\Users\\\THINK\\Downloads\\data.csv', 'w',newline="") as f:
    write = csv.writer(f)
    write.writerows(rows)
    
    
    
    
    