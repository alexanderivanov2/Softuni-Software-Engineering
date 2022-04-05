def get_loading_bar(loading):
    bar = ["%" if i <= loading else "." for i in range(1, 11)]
    if loading == 10:
        return f"100% Complete!\n[{''.join(bar)}]"
    return f"{loading * 10}% [{''.join(bar)}]\nStill loading..."


loading = int(input())
loading = loading // 10
print(get_loading_bar(loading))