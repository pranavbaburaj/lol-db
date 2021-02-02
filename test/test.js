const Import = require('../index.js')
const hello = require('./mod/testfile.js')

const f = new Import(
    "https://raw.githubusercontent.com/pranavbaburaj/poop.js/master/testfiles/testfile.js",
    "mod"
)


var d = require(f.file())


console.log(hello())