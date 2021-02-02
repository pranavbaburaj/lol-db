# Poop.js
A simple javascript libraries for connecting to modules on the internet

## How to use it?
After installing poop.js create a node js project
`npm init` or `npm init -y`
Create a folder where all other modules should be kept
`mkdir mod`
Create an `index.js` file
`index.js`:
```javascript
const Import = require('poop.js')

// the folder should be a child directory of the 
// project directory
const module = new Import("import/url", "the/folder/created")

const moduleName = require(module.file())

// hello() => function in the file
// call the functions

// just call the function name
// don't use moduleName.functionName
```
