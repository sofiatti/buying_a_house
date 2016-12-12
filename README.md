# Introduction
This project is a tool created to help me buy a house in the upcoming year. It will provide me historic house pricing information on Bay Area neighborhoods, informing how well a property holds its value and suggest a bidding price for when I put in an offer for a house.

Currently, I've implement the first of the three goals and I am working on the last.

See website here: http://howmuchshouldyoubid-env.us-west-2.elasticbeanstalk.com/history

# Final Project Details

## Lecture topics 
- Webframes: website created with Flask + Python and hosted at AWS elastic beanstalk
- Interactive Plotting: Made plots with MPLD3. Used highlighting and tooltips plugins
- API: Accessed Zillow's API. Used bs4.
- Virtual environments: used pyvenv
- dataframes: created dataframe from Zillow app

## Future implementation
- I am currently working on getting a price prediction model working

## Feedback

- Please send ideas, recommendation and suggestions to c.sofiatti@gmail.com  
 
# Task List

- [x] Set up barebones Flask website
    - [x] Add LinkedIn button
- [x] Create virtualenv at `~/eb-virt/` (used pyvenv - caution: [pip bug](http://askubuntu.com/questions/488529/pyvenv-3-4-error-returned-non-zero-exit-status-1))
- [x] Get requirement.txt file
- [x] Host Flask site on AWS Elastic Beanstalk
- [x] Which neighborhoods hold their value in financial crisis? 
    - [x] Use 4 bedroom median price data to create MPLD3 plot with highlighting and line tooltip
    - [x] Same as above, but with percentage difference from 1998
    - [ ] Create metric for ranking neighborhoods that 'hold their value'
    - [ ] Generate table for website with info above (for future: create a geo heat map!)
    - [x] Finalize webpage that will hold this session (for future: two items above)
- [x] Get access to Zillow API
- [ ] Create database 
- [ ] Set up query bar in website
- [ ] Model "How much should you offer?"
    -[ ] Select Features
    -[ ] Create training, test and validation sets
    -[ ] Train model. CNN? 
    -[ ] Get confusion matrix
- [ ] Update README.md with examples. Make it look something like this:[Pagers' Readme.md](https://github.com/sindresorhus/pageres)
- [ ] Make Unit Tests
- [ ] Travis (Integration Test)
- [ ] Delete Task List! 


