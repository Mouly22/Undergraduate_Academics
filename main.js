let name = 'Umme Abira Azmary (Mouly)'
let age = 23
const birthday = 22012000

console.log(`my name is ${name} and age is ${age}`)
console.log(name.length)
console.log(name.substring(0,7).toUpperCase())
console.log(name.split(''))
console.log(name.split(' '))
//array
const movie = ['Avengers:Endgame', 'Your Lie in April', 'Princess Mononoke', 'Happy New Year']
console.log(movie)
console.log(movie[3])
console.log(movie.length)
movie.push('Iron Man') //add a value at the last position of the list
console.log(movie)
//for adding a value at the first position of a list,
movie.unshift('How to lose a guy in 10 days')
console.log(movie)
//to remove something from the array
movie.pop()
console.log(movie)
//to check whether something is an array or not
console.log(Array.isArray(movie))
console.log(Array.isArray(name)) //cause name is not an array
console.log(movie.indexOf('Princess Mononoke'))

//object literals
const store = {
    eggs : 2,
    vegetables: ['onion', 'papaya', 'chili', 'ginger'],
    dairy:{
        milk: 2,
        cheese: 'Cube'
    }
}
console.log(store)
console.log(store.vegetables[1])
console.log(store.dairy.cheese)

const todos=[
    {
        Id: 1,
        Name: 'Mandina',
        Profession: 'Teacher',
        Vaccine: true
    },
    {
        Id: 2,
        Name: 'Thenos',
        Profession: 'Genetor',
        Vaccine: false

    },
    {
        Id: 3,
        Name: 'Leo',
        Profession: 'Player',
        Vaccine: true
    }
]
console.log(todos[1].id)

//for sending a data into a server, we need to convert it into the json format. we can convert a js format into a JSON format following below procedures:
const todoJSON = JSON.stringify(todos)
console.log(todoJSON)

//for loop
for (let i=0; i<2; i++){
    console.log(i)
}
let i = 5
while( i<8){
    console.log(i)
    i++
}
//for loop through array
for (let x of todos){
    console.log(x.profession)
}
//***HighOrder Array Method***
//forEach - it prints which particular value we seek to see
todos.forEach(function(x){
    console.log(x.Vaccine)
})

//map - it takes a particular values through loop and returns as a different list
const todoID = todos.map(function(x){
    return(x.Id)
}
)
console.log(todoID)

//filter - it returns only those values whose satisfies conditions
const todoVaccine = todos.filter(function(x){
    return(x.Vaccine === true)
}
)
console.log(todoVaccine)

//but I can now, print this particular satisfied values into a seperate array
const todoVaccine1 = todos.filter(function(x){
    return(x.Vaccine === true)
}).map(function(y){
    return(y.Id)
})
console.log(todoVaccine1)

//Conditionals
const x = 7
if(x === 5){
    console.log('It is 5')
} else if(x > 5){
    console.log("More than 5")
} else {
    console.log("Less than 5")
}

//or, and
const p = 10
const q = 6
if (p> 9 || q < 2){
    console.log("Satisfies")
} else{
    console.log("No luck")
}
if (p> 9 && q < 2){
    console.log("Satisfies")
} else{
    console.log("No luck")
}
//ternary operator
const val = 10
const color =(val>5) ? 'red':'blue'
console.log(color)

//function
function savingUp(b1, b2){
    if (b1>10){
        b1 += 5
        return b1
    } else {
        return b2
    }
}
console.log(savingUp(7, 30))

//creating function
//constructor
function Courses(c1, c2, doe){
    this.c1 = c1
    this.c2 = c2
    this.doe = new Date(doe)

    this.getName = function() {
        return `${this.c1} ${this.c2}`
    }
   
}

Courses.prototype.getDate = function(){
    return this.doe.getFullYear()
}
//instantiate object
const crs1 = new Courses("CSE471","CSE440","10-01-2023")
const crs2 = new Courses("CSE331","CSE340","12-01-2022")
console.log(crs1)
console.log(crs2.c2)
console.log(crs2.doe)
console.log(crs1.doe)
console.log(crs1.getName())
console.log(crs2.getDate())

class Course{
    constructor(n1, n2){
        this.n1 = n1
        this.n2 = n2
    }
    getNum(){
        return `${this.n1} and ${this.n2}`

    }   

}
const var1 = new Course(32, 55)
console.log(var1)
console.log(var1.getNum())

//DOM -> Document Object Model
