const Import = require('../index.js')

const f = new Import(
    "https://raw.githubusercontent.com/pranavbaburaj/poop/main/project/prompt.js",
    "mod"
)

const data = require(f.file())
