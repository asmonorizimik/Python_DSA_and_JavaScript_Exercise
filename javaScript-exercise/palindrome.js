var readlineSync= require("readline-sync")
var num=readlineSync.questionInt("enter number: ")
var temp=num;
let s=""
while (temp!=0){
    var rem=temp%10;
    s+=rem
    temp= Math.floor(temp/10)
}
if (s==num){
    console.log("palindrome!")
}
else{
    console.log("Not Palindrome!")
}