const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str) {
    var expected = ""
    if(str.length <= 1){
        return str
    }
    var counters =[]
    for( var i = 0; i < str.length ; i++){
        var currentChar = str[i]
        var counter = 1
    }
}