var s=""
var n=5
var i=1
while (i<=n){
    var j=1
    while (j<=n-i){
        s+=" "
        j++
    }
    var k=i
    while (k>=1){
        s+=k
        k--
    }
    var l=2
    while (l<=i){
        s+=l
        l++
    }
    i++
    s+='\n'
}
console.log(s)



/** 1
   212
  32123
 4321234
543212345
 */