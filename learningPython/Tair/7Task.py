def custom_greeting(*, name: str, greeting: str) -> str:
   return f"{greeting}, {name}"

print(custom_greeting(greeting="Good morning", name="Tair"))

