from transformers import PegasusForConditionalGeneration, PegasusTokenizer

tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

text = """
In mathematics, a complex number is an element of a number system that contains the real numbers and a specific element denoted i, called the imaginary unit, and satisfying the equation i2 = −1. Moreover, every complex number can be expressed in the form a + bi, where a and b are real numbers. Because no real number satisfies the above equation, i was called an imaginary number by René Descartes. For the complex number a + bi, a is called the real part and b is called the imaginary part.
"""

tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

print(tokens)

summary = model.generate(**tokens)

print(summary[0])

print(tokenizer.decode(summary[0]))
