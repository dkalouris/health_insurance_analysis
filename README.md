# Health Insurance Marketplace kaggle dataset analysis

## Data
Due to size restrictions data is not uploaded and can be found in the challenge page: https://www.kaggle.com/datasets/hhs/health-insurance-marketplace. All data should be stored with the same names in the /data folder for the explorer classes to work.

### Table descriptions:
- Network (Ntwrk-PUF) – Issuer-level data identifying provider network URLs.
- Benefits and Cost Sharing PUF (BenCS-PUF) – Plan variant-level data on essential health benefits, coverage limits, and cost sharing.
- Business Rules PUF (BR-PUF) – Plan-level data on rating business rules, such as maximum age for a dependent, and allowed dependent relationships.
- Plan Attributes PUF (Plan-PUF) – Plan-level data on maximum out of pocket payments, deductibles, HSA eligibility, and other plan attributes.
- Rate PUF (Rate-PUF) – Plan-level data on rates based on an eligible subscriber’s age, tobacco use, and geographic location; and family-tier rates.
- Service Area PUF (SA-PUF) – Issuer-level data on geographic service areas including state, county, and zip code.

### Secondary tables

- Us_State_Abbrevations.csv: US State abbrevations was retrieved from: https://www.50states.com/abbreviations.htm, pasted into LibreOffice Calc and saved as csv to be used as dictionary for looking up abbrevations.

### Questions to answer:

- [X] How do plan rates and benefits vary across states?
- [ ] How do plan benefits relate to plan rates?
- [X] How do plan rates vary by age?
- [ ] How do plans vary across insurance network providers?