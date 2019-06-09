create (person0:Person {person_id: 0,
        first_name: "Emelen",
        last_name: "Hankinson",
        gender: "Male",
        email: "ehankinson0@ebay.com",
        phone: "+387 328 406 2762",
        workplace: "Moen-Stamm",
        university: "Universiti Teknologi Petronas",
        hobby: "Aquatics",
        date_of_birth: "21/03/1956",
        age: 63
}), (person1:Person {person_id: 1,
        first_name: "Tanhya",
        last_name: "McGlaud",
        gender: "Female",
        email: "tmcglaud1@patch.com",
        phone: "+86 670 559 6776",
        workplace: "Rau, Krajcik and Klein",
        university: "Universität Liechtenstein",
        hobby: "JVM",
        date_of_birth: "16/04/1995",
        age: 24
}), (person2: Person {person_id: 2,
        first_name: "Galina",
        last_name:"Try",
        gender: "Female",
        email: "gtry6@macromedia.com",
        phone: "+55 968 267 2670",
        workplace: "Frami Inc",
        university: "Yaroslavl State University",
        hobby: "Sh",
        date_of_birth: "20/03/1996",
        age: 23
}), (person3: Person {person_id: 3,
        first_name: "Alena",
        last_name:"Try",
        gender: "Female",
        email: "wildishj@unblog.fr",
        phone: "+55 968 267 2642",
        workplace: "Kub Group",
        university: "Yaroslavl State University",
        hobby: "Hicking",
        date_of_birth: "21/05/1973",
        age: 46
})

match (a:Person), (b:Person)
where a.first_name = 'Galina' and b.first_name = 'Alena'
create (a)-[r:daughter {warmness: 95}]->(b)
return type(r)

match (a:Person), (b:Person)
where a.first_name = 'Alena' and b.first_name = 'Galina'
create (a)-[r:mother {warmness: 95}]->(b)
return type(r)

match (a:Person), (b:Person)
where a.first_name = 'Alena' and b.first_name = 'Emelen'
create (a)-[r:girlfriend {warmness: 80}]->(b)
return type(r)

match (a:Person), (b:Person)
where a.first_name = 'Emelen' and b.first_name = 'Alena'
create (a)-[r:boyfriend {warmness: 81}]->(b)
return type(r)

match (a:Person), (b:Person)
where a.first_name = 'Tanhya' and b.first_name = 'Galina'
create (a)-[r:friend {warmness: 67}]->(b)
return type(r)

match (a:Person), (b:Person)
where a.first_name = 'Galina' and b.first_name = 'Tanhya'
create (a)-[r:friend {warmness: 64}]->(b)
return type(r)

match (a:Person), (b:Person)
where a.first_name = 'Emelen' and b.first_name = 'Tanhya'
create (a)-[r:teacher {warmness: 14}]->(b)
return type(r)

match (a:Person), (b:Person)
where a.first_name = 'Tanhya' and b.first_name = 'Emelen'
create (a)-[r:student {warmness: 12}]->(b)
return type(r)

MATCH (n:Person { first_name: "Emelen" })
RETURN n

match (a:Person {first_name: 'Tanhya'})
detach delete a

MATCH (n:Person { first_name: "Alena" })
SET n.last_name = 'Hankinson'
SET n.workplace = 'Moen-Stamm'
RETURN n.first_name, n.workplace

MATCH (n:Person)
RETURN count(n)

MATCH (n:Person)
with min(n.age) as min_age, max(n.age) as max_age, avg(n.age) as avg_age 
RETURN min_age, max_age, avg_age
