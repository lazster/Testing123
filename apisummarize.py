import os
import openai

openai.api_key = ""

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Summarize this for an 8 year old in 2 sentences:\n\nJupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.",
  temperature=0.7,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.5
)

print(response + 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)