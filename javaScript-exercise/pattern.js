/**
0  
0 1  
0 2 4  
0 3 6 9  
0 4 8 12 16
 */



let i=0;
let s="";
while (i<5){
    let j=0;
    while (j<=i){
        s+=(i*j)+" "
        j++
    }
    i++
    s+='\n'
}
console.log(s)







/**  
  1
 234
56789 
*/


// let n = 3;
// let count = 1;
// let string = "";
// for (let i = 1; i <= n; i++) {
//   // creating spaces
//   for (let j = 1; j <= n - i; j++) {
//     string += " ";
//   }
//   for (let k = 1; k <= 2 * i - 1; k++) {
//     string += count;
//     count++;
//   }
//   string += "\n";
// }
// console.log(string);



// let n=3;
// let c=1;
// let s='';
// let i=1
// while (i<=n){
//     let j=1;
//     while (j<=n-i){
//         s+=" "
//         j++
//     }
//     let k=1
//     while (k<=2*i-1){
//         s+=c;
//         c++
//         k++
//     }
//     i++
//     s+='\n'
// }
// console.log(s)
