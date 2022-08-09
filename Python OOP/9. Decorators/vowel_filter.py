def vowel_filter(function):
    def wrapper():
        result = function()
        vowels = ["a", "e", "i", "y", "o", "u"]
        vowels_filtrate = [ch for ch in result if ch.lower() in vowels]
        return vowels_filtrate
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())