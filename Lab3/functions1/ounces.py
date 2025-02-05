def convert (grams):
    ounces = grams / 28.3495231
    print(f"{grams} grams in ounces : {ounces:.4f}")
grams = int(input("enter grams to convert ounces: "))
convert (grams)
