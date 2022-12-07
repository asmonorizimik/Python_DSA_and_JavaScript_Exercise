// let n = 5;
// let string = "";
// // External loop
// for (let i = 1; i <= n; i++) {
//   // creating spaces
//   for (let j = 1; j <= n - i; j++) {
//     string += " ";
//   }
//   // creating numbers
//   for (let k = 1; k <= 2 * i - 1; k++) {
//     string += k;
//   }
//   string += "\n";
// }
// console.log(string);





/** 1
   123
  12345
 1234567
123456789 */





let n=5;
let s="";
let i= 1;
while (i<=n){
  let j=1;
  while (j<=n-i){
    s+=" ";
    j++
  }
  let k=1;
  while (k<=2*i-1){
    s+=k
    k++
  }
  i++
  s+='\n'
}
console.log(s)
