from director import Director
from contretebuilder1 import ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()

director.builder = builder

print("\nProdukt podstawowy")
director.build_minimal_version()
builder.product.list_parts()

print("\nProdukt pełny")
director.build_full_version()
builder.product.list_parts()

print("\nProdukt użytkownika...")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
