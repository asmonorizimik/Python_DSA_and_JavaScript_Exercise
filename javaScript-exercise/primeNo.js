//  Write a program to check whether a number is prime or not.
// var readlineSync = require("readline-sync")
// var num=readlineSync.questionInt("enter number: ")
// var count=0
// var num1= num
// var i=1
// while (i<=num){
//     if (num%i==0 && num%num1==0){
//         count+=1
//     }
//     i++
// }
// if (count==2){
//     console.log("prime number")
// }
// else{
//     console.log("not prime number")
// }





//// prime number between two given numbers...
// var readlineSync=require("readline-sync")
// var first=readlineSync.questionInt("enter start number: ")
// var sec= readlineSync.questionInt("enter last number: ")
// var count=0
// while (first<=sec){
//     var i=1
//     var c=0
//     while (i<first){
//         if (first%i==0){
//             c+=1
//         }
//         i++
//     }
//     if(c==1){
//         console.log(first)
//     }
//     first++
// }






// prime number from 1 to 100
var i=1
while (i<=100){
    var j=1
    var c=0
    while (j<=100){
        if (i%j==0){
            c+=1
        }
        j++
    }
    if (c==2){
        console.log(i)
    }
    i++
}
