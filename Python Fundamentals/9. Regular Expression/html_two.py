print(f"<h1>\n    {input()}\n</h1>")
print(f"<article>\n    {input()}\n</article>")
div_data = input()
while not div_data == "end of comments":
    print(f"<div>\n    {div_data}\n</div>")
    div_data = input()