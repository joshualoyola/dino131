#travelX/schema.py
import strawberry
from typing import List
from data.types import Person, PersonInput, PersonPartialInput
from strawberry_django import mutations, field

@strawberry.type
class Query:
    person: Person = strawberry.django.field()
    persons: List[Person] = strawberry.django.field()


@strawberry.type
class Mutation:
  
  create_person: Person = strawberry.django.mutations.create(PersonInput)
  create_persons: List[Person] = mutations.create(PersonInput)
  update_persons: List[Person] = mutations.update(PersonPartialInput)
  delete_persons: List[Person] = mutations.delete()


schema = strawberry.Schema(query=Query, mutation=Mutation)





##GraphQL Examples

#query myQ{
#  persons{
#    firstname
#    lastname
#  }
#}

#mutation myM{
#  createPerson(data:{firstname:"Alex", lastname:"Zones"}){
#    firstname
#    lastname
#  }
#}

#mutation myMC{
#  createPersons(data:[{firstname:"Alex", lastname:"Zones"}{firstname:"Alexis", lastname:"Zones"}]){
#    firstname
#    lastname
 # }
#  }

#Search Specific ID
#query myQs{
#  person(pk: 16){
#    firstname
#    lastname
#  }
#}

# Filter Example
#query myQ {
#  fruits(filters: {name: {contains: "berry"}}) {
#    id
#    name
#    color {
#      id
#    }
#  }
#}