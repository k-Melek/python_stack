// Given an array of strings
// return the number of times each string occurs (a frequency / hash table)


const arr1 = ["a", "a", "a"];
const expected1 = {
a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
a: 2,
b: 1,
c: 3,
B: 1,
d: 1,
};

const arr3 = [];
const expected3 = {};

function makeFrequencyTable(arr) {
    var expected ={};
    for (var i = 0; i < arr.length; i++){
        // if(expected.hasOwnProperty(arr[i])){
            if(expected[arr[i]]){
            expected[arr[i]] += 1
        } else {
            expected[arr[i]] = 1
        }
    }
    console.log(expected);
    return expected
}

makeFrequencyTable(arr1)
makeFrequencyTable(arr2)