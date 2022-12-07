var n=5
var i=0
var s=""
while (i<n){
    var j=0
    while (j<n){
        if (i+j>=n-1){
            s+="* "
        }
        else{
            s+=" "
        }
        j++
    }
    i++
    s+="\n"
}
console.log(s)