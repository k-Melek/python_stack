/* 
  Given a string,
  return a new string with the duplicates excluded

  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 */

function stringDedupe(str) {
    var result ="";
    for(var i = 0; i < str.length; i++ ){
        if( result.indexOf(str[i]) == -1 ) {
            result += str[i]
        }
    }
    return result
}

// console.log(stringDedupe(str1));
// console.log(stringDedupe(str2));
// console.log(stringDedupe(str3));
// console.log(stringDedupe(str4));

function stringDedupe1(str) {
    result = ""
    var freqDict= {}
    for(var i=0; i< str.length; i++){
        if(!freqDict[str[i]]){
            freqDict[str[i]] = true
            result += str[i]
        }
    }
    console.log(freqDict);
    return result
}

console.log(stringDedupe1(str1));
console.log(stringDedupe1(str2));
console.log(stringDedupe1(str3));
console.log(stringDedupe1(str4));