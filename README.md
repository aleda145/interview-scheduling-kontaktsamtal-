# Interview scheduling for career fair

Some career fairs have interviews during the fair day. This is typical in Sweden, where they are called "kontaktsamtal".
Since most career fairs are only one day it is hard to create a schedule that works for all companies as well as the students. 
To further complicate things, students that are chosen for one interview are usually also chosen for another, making 
it very hard to successfully schedule this. When updating one student, the errors will cascade and 
it will be a big mess. 

This optimization script solves this problem mathematically. It was used for one of the biggest student career fairs 
in Sweden and the schedule had no errors. Before this script two people would spend 20h+ a few days before 
the fair to get an "ok" schedule. If a solution exists where all students can have an interview with 
all the companies that have selected them then this script will find it. 

## The problem
The problem can be summarized as the following optimization model:

![model](model.png)
