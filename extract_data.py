import pandas as pd
import numpy as np
import utils

print(f'loading {utils.raw_filename}')
data = pd.read_excel(utils.raw_filename)
print(f'loaded {utils.raw_filename}')

# # # =================== Extract data ===========================
print('extracting data')

# ### Extract info from 'Tag5'
print('\textracting Tag5')
data['Tag_SoldPrice'] = data['Tag5'].str.extract('(?:.*for\s)([0-9.,$]+)')
data['Tag_SoldDate'] = data['Tag5'].str.extract('(?:.*on\s)([0-9 + % a-zA-Z /,]+)')
print('\textracted Tag5')

# ### Extract info from 'HomeFact'
# Fill HomeFactsAndPrice to HomeFacts and PriceInsights if null
print('\textracting HomeFact')
data.loc[pd.isnull(data.loc[:, 'HomeFacts']), 'HomeFacts'] = data.loc[:, 'HomeFactsAndPrice']
data.loc[pd.isnull(data.loc[:, 'PriceInsights']), 'PriceInsights'] = data.loc[:, 'HomeFactsAndPrice']
data['HomeFacts_Status'] = data['HomeFacts'].str.extract('(?:.*Status\s)([a-zA-Z /,]+)')
data['HomeFacts_OfferReviewDate'] = data['HomeFacts'].str.extract('(?:.*Offer Review Date\s)([0-9 + % a-zA-Z /,]+)')
data['HomeFacts_PropertyType'] = data['HomeFacts'].str.extract('(?:.*Property Type\s)([a-zA-Z /,]+)')
data['HomeFacts_YearBuilt'] = data['HomeFacts'].str.extract('(?:.*Year Built\s)([0-9]+)')
data['HomeFacts_Style'] = data['HomeFacts'].str.extract('(?:.*Style\s)([a-zA-Z /,]+)')
data['HomeFacts_Community'] = data['HomeFacts'].str.extract('(?:.*Community\s)([a-zA-Z /,]+)')
data['HomeFacts_LotSize'] = data['HomeFacts'].str.extract('(?:.*Lot Size\s)([0-9 +,.]+)')
data['HomeFacts_LotSizeUnit'] = data['HomeFacts'].str.extract('(?:.*Lot Size\s[0-9 ,.]+)([a-zA-Z /.]+)')
data['HomeFacts_MLS'] = data['HomeFacts'].str.extract('(?:.*MLS#\s)([0-9 +,.]+)')
print('\textracted HomeFact')

# ### Extract info from 'PriceInsight'
print('\textracting PriceInsight')
data['PriceInsights_RedfinEstimate'] = data['PriceInsights'].str.extract('(?:.*Redfin Estimate\s)([0-9 + % a-zA-Z$ /,]+)')
data['PriceInsights_PricePerSqFt'] = data['PriceInsights'].str.extract('(?:.*Price/Sq.Ft.\s)([0-9 + % a-zA-Z$ /,]+)')
print('\textracted PriceInsight')

# ### Extract info from 'property_detail'
# Parking Info
print('\textracting property_detail')
data['ParkingTotal'] = data['property_detail'].str.extract('(?:.*Parking Total:\s)([0-9]+)')
data['ParkingFeatures'] = data['property_detail'].str.extract('(?:.*Parking Features:\s)([a-zA-Z /,]+)')
print('\textracted property_detail')

# School Info
# data validation with school columns
print('\textracting School Info')
data['ElementarySchool'] = data['property_detail'].str.extract('(?:.*Elementary School:\s)([a-zA-Z /,]+)')
data['MiddleOrJuniorHighSchool'] = data['property_detail'].str.extract('(?:.*Middle Or Junior High School:\s)([a-zA-Z /]+)')
data['HighSchool'] = data['property_detail'].str.extract('(?:.*High School:\s)([a-zA-Z /,]+)')
data['HighSchoolDistrict'] = data['property_detail'].str.extract('(?:.*High School District:\s)([a-zA-Z /,]+)')
print('\textracted School Info')

#Interior Features
#Bedroom Info
print('\textracting Bedroom Info')
data['NumberOfBedrooms'] = data['property_detail'].str.extract('(?:.*# of Bedrooms:\s)([0-9]+)')
data['NumberOfBedsUpper'] = data['property_detail'].str.extract('(?:.*# of Beds Upper:\s)([0-9]+)')
data['NumberOfBedsMain'] = data['property_detail'].str.extract('(?:.*# of Bedrooms Main:\s)([0-9]+)')
print('\textracted Bedroom Info')

#Basement Info
print('\textracting Basement Info')
data['BasementFeatures'] = data['property_detail'].str.extract('(?:.*Basement Features:\s)([a-zA-Z /,]+)')
print('\textracted Basement Info')

#Fireplace Info
print('\textracting Fireplace Info')
data['NumberOfFireplaces'] = data['property_detail'].str.extract('(?:.*# of Fireplaces:\s)([0-9]+)')
print('\textracted Fireplace Info')

#Heating & Cooling
print('\textracting Heating & Cooling')
data['HeatingCoolingType'] = data['property_detail'].str.extract('(?:.*Heating Cooling Type:\s)([0-9 + % a-zA-Z /,]+)')
print('\textracted Heating & Cooling')

#Interior Features
# if 'AppliancesIncluded' > 'Appliances', use 'AppliancesIncluded'
print('\textracting Appliances Info')
data['Appliances'] = data['property_detail'].str.extract('(?:.*Appliances:\s)([a-zA-Z /,]+)')
data['AppliancesIncluded'] = data['property_detail'].str.extract('(?:.*Appliances Included:\s)([a-zA-Z /,]+)')
data['Flooring'] = data['property_detail'].str.extract('(?:.*Flooring:\s)([a-zA-Z /,]+)')
print('\textracted Appliances Info')

# Exterior Features
#Building Info
print('\textracting Building Info')
data['BuildingInformation'] = data['property_detail'].str.extract('(?:.*Building Information:\s)([a-zA-Z /,]+)')
data['Roof'] = data['property_detail'].str.extract('(?:.*Roof:\s)([a-zA-Z /,]+)')
print('\textracted Building Info')

# Exterior Features
print('\textracting Exterior Features')
data['ExteriorFeatures'] = data['property_detail'].str.extract('(?:.*Exterior Features:\s)([a-zA-Z /,]+)')
print('\textracted Exterior Features')

#Utilities, Taxes / Assessments, Financing, Location Details
#Utility Information
print('\textracting Utility Information')
data['WaterSource'] = data['property_detail'].str.extract('(?:.*Water Source:\s)([a-zA-Z /,]+)')
data['Sewer'] = data['property_detail'].str.extract('(?:.*Sewer:\s)([a-zA-Z /,]+)')
data['WaterHeaterLocation'] = data['property_detail'].str.extract('(?:.*Water Heater Location:\s)([a-zA-Z /,]+)')
data['WaterHeaterType'] = data['property_detail'].str.extract('(?:.*Water Heater Type:\s)([a-zA-Z /,]+)')
print('\textracted Utility Information')

# Tax Info
print('\textracting Tax Info')
data['TaxAnnualAmount'] = data['property_detail'].str.extract('(?:.*Tax Annual Amount:\s)([$0-9,]+)')
data['TaxYear'] = data['property_detail'].str.extract('(?:.*Tax Year:\s)([0-9]+)')
print('\textracted Tax Info')

# Financing
print('\textracting Financing')
data['BuyerFinancing'] = data['property_detail'].str.extract('(?:.*Buyer Financing:\s)([a-zA-Z /,]+)')
print('\textracted Financing')

# Home Info
print('\textracting Home Info')
data['LivingArea'] = data['property_detail'].str.extract('(?:.*Living Area:\s)([$0-9,]+)')
data['LivingAreaUnits'] = data['property_detail'].str.extract('(?:.*Living Area Units:\s)([a-zA-Z /,]+)')
data['FoundationDetails'] = data['property_detail'].str.extract('(?:.*Foundation Details:\s)([a-zA-Z /,]+)')
data['YearBuiltEffective'] = data['property_detail'].str.extract('(?:.*Year Built Effective:\s)([$0-9,]+)')
data['Levels'] = data['property_detail'].str.extract('(?:.*Levels:\s)([a-zA-Z /,]+)')
print('\textracted Home Info')

#Property Info
print('\textracting Property Info')
data['EnergySource'] = data['property_detail'].str.extract('(?:.*Energy Source:\s)([a-zA-Z /,]+)')
data['SqFtFinished'] = data['property_detail'].str.extract('(?:.*Sq. Ft. Finished:\s)([$0-9,]+)')
data['Style'] = data['property_detail'].str.extract('(?:.*Style Code:\s[0-9 ]+ - )([0-9 a-zA-Z/ -]+)')
data['StyleCode'] = data['property_detail'].str.extract('(?:.*Style Code:\s)([0-9]+)')
data['StyleAndCode'] = data['property_detail'].str.extract('(?:.*Style Code:\s)([a-zA-Z$/0-9, -]+)')
data['PropertyType'] = data['property_detail'].str.extract('(?:.*Property Type:\s)([a-zA-Z /,]+)')
data['PropertySubType'] = data['property_detail'].str.extract('(?:.*Property Sub Type:\s)([a-zA-Z /,]+)')
data['HasView'] = data['property_detail'].str.extract('(?:.*Has Vie)([a-zA-Z /,]+)')
data.loc[data['HasView'] == 'w', 'HasView'] = '1'
print('\textracted Property Info')

# Lot Info
print('\textracting Lot Info')
data['LotSizeAcres'] = data['property_detail'].str.extract('(?:.*Lot Size Acres:\s)([$0-9,.]+)')
data['LotSizeUnits'] = data['property_detail'].str.extract('(?:.*Lot Size Units:\s)([a-zA-Z /,]+)')

# Land Sq. Ft: 12,096, Acres: 0.2777
data['LotLandSqFt'] = data['property_detail'].str.extract('(?:.*Land Sq. Ft:\s)([$0-9,.]+)')
data['LotAcres'] = data['property_detail'].str.extract('(?:.*Acres:\s)([$0-9,.]+)')
print('\textracted Lot Info')

#PublicFacts
#3.	AddPublicFacts_LotSize_Unit: if PublicFacts_LotSize <10, unit Acres, otherwise sqft
print('\textracting PublicFacts')
data['PublicFacts_Beds'] = data['PublicFacts'].str.extract('(?:.*Beds\n)([$0-9,.]+)')
data['PublicFacts_Baths'] = data['PublicFacts'].str.extract('(?:.*Baths\n)([$0-9,.]+)')
data['PublicFacts_SqFt'] = data['PublicFacts'].str.extract('(?:.*Sq. Ft.\n)([$0-9,.]+)')
data['PublicFacts_Stories'] = data['PublicFacts'].str.extract('(?:.*Stories\n)([$0-9,.]+)')
data['PublicFacts_LotSize'] = data['PublicFacts'].str.extract('(?:.*Lot Size\n)([a-zA-Z$/0-9,.]+)')
data['PublicFacts_Style'] = data['PublicFacts'].str.extract('(?:.*Style\s)([a-zA-Z /,]+)')
data['PublicFacts_YearBuilt'] = data['PublicFacts'].str.extract('(?:.*Year Built\n)([$0-9,.]+)')
data['PublicFacts_YearRenovated'] = data['PublicFacts'].str.extract('(?:.*Year Renovated\n)([$0-9,.]+)')
data['PublicFacts_APN'] = data['PublicFacts'].str.extract('(?:.*APN\n)([$0-9,. ]+)')
print('\textracted PublicFacts')

# extract sale history
print('\textracting sale history')
priceColumnName = ['Price1', 'Price2', 'Price3']
dateColumnName = ['Date1', 'Date2', 'Date3']
statusColumnName = ['Status1', 'Status2', 'Status3']
columnNames = []
columnNames.append(priceColumnName)
columnNames.append(dateColumnName)
columnNames.append(statusColumnName)

# init
for names in columnNames:
    for name in names:
        data[name] = ''
        
# process
for i in range(0, len(data['SaleHistory'])):
    # find recent 3 records. each record, it contains (price, date, status)
    recent = None
    history = data['SaleHistory'][i]
    try:
        recent = utils.extractHistory(history)
    except:
        # print(f'error in {i} row: {history}')
        print(f'error in {i} row')
    
    # process recent records
    if recent is not None and len(recent) == 3:
        for column_index in range(0, len(columnNames)):
            column = columnNames[column_index]
            
            # put prices (1st item of record) in 3 different cols
            for j in range(0, len(recent)):
                try:
                    if recent[j] is not None: 
                        data.at[i, column[j]] = recent[j][column_index]
                except:
                    print(f'error in {i} row and {j} item: {recent[j]}')
print('\textracted sale history')

# process pending data
print('\textracting pending data')
data['PendingDate'] = ''
data['PendingStatus'] = ''
for i in range(0, len(data['SaleHistory'])):
    # find recent 3 records. each record, it contains (price, date, status)
    recent = None
    history = data['SaleHistory'][i]
    try:
        recent = utils.extractPendingDate(history)
        
    except:
        print(f'error in {i} row: {history}')
        
    if recent is not None and len(recent) >= 1:
        data.at[i, 'PendingDate'] = recent[0][0]   
        data.at[i, 'PendingStatus'] = recent[0][1] 

print('\textracted pending data')
print('extracted data')

# ============== Drop columns ====================
print('Drop columns')
data_extract= data.drop(['HomeFacts','PriceInsights','property_detail','PublicFacts','Tag2','Tag3','Tag4', 'Tag5','detail1','detail2','detail3','detail4','detail5','HomeFactsAndPrice'], axis = 1)

data_extract['City']= utils.city
data_extract['ZipCode']= utils.zipcode
print('Droped columns')

print(f'Saving to {utils.extracted_filename}')
data_extract.to_excel(utils.extracted_filename, index = False)
print(f'Saved to {utils.extracted_filename}')