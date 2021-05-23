cat_name = input()
cat_gender = input()

cats = {"British Shorthair": {"m": 13, "f": 14}, "Siamese": {"m": 15, "f": 16}, "Persian": {"m": 14, "f": 15},
        "Ragdoll": {"m": 16, "f": 17}, "American Shorthair": {"m": 12, "f": 13}, "Siberian": {"m": 11, "f": 12}}

if cat_name in cats:
    years = cats[cat_name][cat_gender]
    cat_months = years * 12 // 6
    print(f"{cat_months} cat months")
else:
    print(f"{cat_name} is invalid cat!")
