/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each result capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
// * FIRST METHOD

const str4 = "  global   information tracker    ";
const expected4 = "GIT";
var expected = ""
var testArr =[]
function acronymize(str) {
    testArr = str.split(" ");
    console.log(testArr);
    for(var i =0; i<testArr.length; i++ ){
        if(testArr[i] != ""){
            expected += testArr[i][0].toUpperCase()
        }
    }
    return expected
}
acronymize(str4)
console.log(expected);

// * SECOND METHOD Without Split() METHOD

function acronymize2(str) {
    var result =""
    if(str[0] !=" "){
        result+=str[0].toUpperCase()
    }
    for(var i = 1; i<str.length-2; i++){
        if(str[i] == " " && str[i+1] != " "){
            result += str[i+1].toUpperCase()
        }
    }
    return result
}

console.log(acronymize2(str4));

