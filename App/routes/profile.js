// import React from 'react';

// const profile = () => {
//   return 
//   (<div className= 'container'>
//       <div className='overlap'/>
// </div>);
// };

// export default profile;

var express = require('express');
var router = express.Router();


/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render({});
});

module.exports = router;