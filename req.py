import requests

chemical_ids = [
"ATP",
"01G",
"03B",
"03F",
"03M",
"03P",
"05R",
"07V",
"09L",
"0A1",
"0CK",
"0DY",
"0ED",
"0FW",
"0HO",
"0IT",
]


with open('chem_comp_info_all.txt', 'a') as file:
    for chemical_id in chemical_ids:
        url = f"https://data.rcsb.org/rest/v1/core/chemcomp/{chemical_id}"
        response = requests.get(url)

        if response.status_code == 200:
            try:
                data = response.json()

        
                chem_comp_info = data.get('chem_comp', {})
                chem_comp_id = chem_comp_info.get('id', 'N/A')
                chem_comp_name = chem_comp_info.get('name', 'N/A')
                chem_comp_formula = chem_comp_info.get('formula', 'N/A')
                chem_comp_formula_weight = chem_comp_info.get('formula_weight', 'N/A')
                
             
                file.write(f"{chem_comp_id}\t{chem_comp_name}\t{chem_comp_formula}\t{chem_comp_formula_weight}\n")

                print(f"Data for {chemical_id} added to chem_comp_info_all.txt")

            except ValueError:
                print("Failed to decode JSON response.")
        else:
            print(f"Failed to retrieve data for {chemical_id}. Status code: {response.status_code}")

print("All data written to chem_comp_info_all.txt")