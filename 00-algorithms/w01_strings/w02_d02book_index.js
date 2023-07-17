/* 
Book Index

Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums
span a consecutive range.
*/

const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

const nums2 = [5, 6, 7, 8, 9];
const expected2 = "5-9";

const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
const expected3 = "1-3, 7, 9, 15-17";
const nums4 = [2,7,8,9,10,16,21,22,23,24,30,32,33,34,]

function bookIndex(nums) {
    myString =""
    for(var i = 0; i < nums.length; i++ ){
        if( nums[i] != nums[i - 1] + 1) {
            if(i != 0){
                myString +=', '
            }
            
            myString += nums[i]
            } else if ( nums[i] != nums[i + 1] - 1) {
                myString += '-' + nums[i];
            }
    }
    return myString
}


console.log(bookIndex(nums3));