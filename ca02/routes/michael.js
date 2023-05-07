/*
  This utilizes ChatGPT
*/
const express = require('express');
const router = express.Router();
const axios = require('axios');

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

router.get('/michael', isLoggedIn, (req,res) => {
    res.render('michael')
})

router.post('/api/v1/prompt/michael', isLoggedIn, async (req,res) => {
  if (!req.body.prompt) {res.status(400).json({error: 'prompt is required'}).send(); return}
  const response = await axios.post('http://gracehopper.cs-i.brandeis.edu:3500/openai',
  {prompt:req.body.prompt})
  res.status(200).send(response.data.choices[0]['message']['content']);
  return;
  })

  module.exports = router;
